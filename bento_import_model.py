import bentoml
from transformers import AutoModelForCausalLM, AutoTokenizer

# 훈련이 완료된 모델이 저장된 경로
# 사용자님의 로그에 나온 정확한 경로로 수정했습니다.
FINETUNED_MODEL_PATH = './note/fineTuning/specialtoken/tensorboard/all_presidents_gpt2_final'

# BentoML에 등록할 모델의 이름
BENTO_MODEL_NAME = 'president_gpt2_finetuned'

print(f"Importing model from {FINETUNED_MODEL_PATH}...")

model = AutoModelForCausalLM.from_pretrained(FINETUNED_MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(FINETUNED_MODEL_PATH)

bento_model = bentoml.transformers.save_model(
    BENTO_MODEL_NAME,
    model,
    custom_objects={"tokenizer": tokenizer},
    signatures={"generate": {"batchable": False}},
)

print(f"Successfully imported model: {bento_model}")