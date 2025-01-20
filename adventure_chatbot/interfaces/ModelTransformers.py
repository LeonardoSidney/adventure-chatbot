from typing import Any
from adventure_chatbot import ModelEntity
from transformers import pipeline
import torch


class ModelTransformers(ModelEntity):
    def __init__(self):
        super().__init__()

    def load(self, model_path: str):
        self.model = pipeline(
            "text-generation",
            model=model_path,
            torch_dtype=torch.bfloat16,
            device_map="auto",
        )

    def generate(self, prompt: list[dict[str, str]]) -> Any:
        output = self.model(
            prompt,
            max_new_tokens=256,
        )
        return output