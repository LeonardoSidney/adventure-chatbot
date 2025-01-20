from abc import ABC, abstractmethod
from adventure_chatbot import ModelInfo

class HubEntity(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def downloadModel(self, modelInfo: ModelInfo) -> str:
        pass

    @abstractmethod
    def getRepoFiles(self, repo_id: str) -> list[str]:
        pass
    
    @abstractmethod
    def filterForModelFiles(self, repoFiles: list[str]) -> list[str]:
        pass