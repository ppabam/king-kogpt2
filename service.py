import torch
import bentoml
from bentoml.io import JSON
from pydantic import BaseModel

bento_image = bentoml.images.Image(python_version="3.11").python_packages(
    "torch", "transformers", "pydantic"
)

# 1. API 입력 데이터의 형식을 Pydantic 모델로 명확하게 정의합니다.
# 이렇게 하면 입력 데이터 검증과 자동 문서 생성이 쉬워집니다.
class GenerationInput(BaseModel):
    president_name: str
    prompt_text: str
    max_length: int = 128

# 2. 이전에 저장한 모델을 가져옵니다.
# 최신 BentoML에서는 모델을 Runner로 감싸는 것을 권장하지만,
# 이전 버전과의 호환성을 위해 현재 코드 스타일을 유지하며 수정합니다.
@bentoml.service(
    image=bento_image,
    resources={"cpu": "4"},  # 예시 리소스 설정
)
class PresidentGPTEndpoint: # 클래스 이름 변경 (선택사항)
    def __init__(self) -> None:
        # 이 부분은 기존과 동일합니다.
        model_ref = bentoml.models.get("president_gpt_endpoint:latest")
        
        # 모델과 토크나이저를 메모리에 로드합니다.
        self.model = bentoml.transformers.load_model(model_ref)
        self.tokenizer = model_ref.custom_objects["tokenizer"]
        
        # GPU 사용 설정
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model.to(self.device)
        self.model.eval()
        print(f"Model and tokenizer loaded successfully on '{self.device}'")

    # 3. API 엔드포인트 수정
    # 입력을 JSON(pydantic_model=GenerationInput)으로 받고, 출력을 JSON으로 보냅니다.
    @bentoml.api
    def generate(self, input_data: GenerationInput) -> dict:
        # 입력 데이터 추출
        president_name = input_data.president_name
        prompt = input_data.prompt_text
        max_len = input_data.max_length

        # 4. 핵심 로직: 스페셜 토큰을 포함한 최종 프롬프트 생성
        president_token = f"<|{president_name}|>"
        formatted_prompt = f"{president_token} {prompt}"
        
        inputs = self.tokenizer(formatted_prompt, return_tensors="pt").to(self.device)
        
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs, 
                max_length=max_len,
                repetition_penalty=2.0,
                do_sample=True,
                top_k=50,
            )
        
        # 생성된 텍스트 디코딩
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=False)

        # 5. 구조화된 JSON 형태로 결과 반환
        return {
            "president_name": president_name,
            "prompt_text": prompt,
            "full_generated_text": generated_text
        }