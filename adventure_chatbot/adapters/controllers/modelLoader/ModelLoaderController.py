from adventure_chatbot import ModelEntity, ModelLoaderInteractor, ModelInfo


class ModelLoaderController:
    def __init__(self, modelInfo: ModelInfo) -> None:
        self.modelInfo: ModelInfo = modelInfo
        self.interactor: ModelLoaderInteractor = ModelLoaderInteractor(modelInfo)

    def execute(self) -> ModelEntity | bool:
        return self.interactor.execute()
