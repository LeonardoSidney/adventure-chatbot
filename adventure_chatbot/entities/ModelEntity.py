from abc import ABC, abstractmethod
from typing import Any

class ModelEntity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load(self, model_path: str):
        pass

    @abstractmethod
    def generate(self, prompt: list[dict[str, str]]) -> Any:
        pass