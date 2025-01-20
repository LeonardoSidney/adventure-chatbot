from adventure_chatbot import ModelEntity, ModelServices, ModelInfo


class ModelInteractor:
    def __init__(self, modelInfo: ModelInfo) -> None:
        self.services = ModelServices()
        self.modelInfo: ModelInfo = modelInfo

    def load(self) -> ModelEntity:
        modelType = self.services.getModelType(self.modelInfo)
        self.model: ModelEntity = self.services.loadModel(self.modelInfo, modelType)
        return self.model
