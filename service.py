from __future__ import annotations
import bentoml

with bentoml.importing():
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch

MODEL_TAG = "president_gpt2_finetuned:latest"

@bentoml.service
class TextGeneration:
    def __init__(self) -> None:
        model_ref = bentoml.models.get(MODEL_TAG)
        self.model = AutoModelForCausalLM.from_pretrained(model_ref.path)
        self.model.eval()
        self.tokenizer = model_ref.custom_objects["tokenizer"]

    @bentoml.api
    def generate(self, prompt: str = "대한민국 대통령의 연설문은 다음과 같습니다. ") -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_new_tokens=100)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
