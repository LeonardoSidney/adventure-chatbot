from adventure_chatbot import (
    ModelEntity,
    ModelInteractor,
    ModelLoaderInteractor,
    ModelInfo,
)


class ModelController:
    def __init__(self, modelInfo: ModelInfo) -> None:
        self.interactor = ModelInteractor(modelInfo)
        self.modelLoaderInteractor = ModelLoaderInteractor(modelInfo)
        self.modelInfo = modelInfo

    def load(self) -> bool:
        if not self.modelLoaderInteractor.execute():
            return False
        self.model: ModelEntity = self.interactor.load()
        return True

    def generate(self, messages) -> list[str] | None:
        return self.model.generate(messages)
