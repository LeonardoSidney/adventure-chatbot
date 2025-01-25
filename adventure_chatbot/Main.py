from typing import Any
from adventure_chatbot import ModelController, ModelInfo


class Main:
    def __init__(self) -> None:
        self.modelInfo = ModelInfo(
            model_id="meta-llama/Meta-Llama-3.1-8B-Instruct",
            model_path="models/",
        )
        self.model = ModelController(self.modelInfo)

    def execute(self):
        if not self.model.load():
            raise Exception("Model failed to load")
        messages = [
            {
                "role": "system",
                "content": "You are a pirate chatbot who always responds in pirate speak!",
            },
            {"role": "user", "content": "Who are you?"},
        ]
        result: Any = self.model.generate(messages)
        print(result[0]["generated_text"][-1])