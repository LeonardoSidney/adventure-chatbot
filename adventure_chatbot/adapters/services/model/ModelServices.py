from adventure_chatbot import (
    EnumModelStrings,
    ModelInfo,
    EnumModelTypes,
    ModelTransformers,
    ModelEntity,
)


class ModelServices:
    def getModelPath(self, modelInfo: ModelInfo) -> str:
        modelName = modelInfo.model_id.split("/")[-1]
        modelPath = f"{modelInfo.model_path}{modelName}"
        return modelPath

    def isModelFile(self, file: str) -> bool:
        for modelExtension in EnumModelStrings.MODEL_FILES_EXTENSION.value:
            if file.endswith(modelExtension):
                return True
        return False

    def isConfigFile(self, file: str) -> bool:
        for configExtension in EnumModelStrings.MODEL_FILES_CONFIG_EXTENSION.value:
            if configExtension in file:
                return True
        return False

    def getModelType(self, modelInfo: ModelInfo) -> int:
        if modelInfo:
            return EnumModelTypes.TRANSFORMERS.value
        raise ValueError("Model type not found")

    def loadModel(self, modelInfo: ModelInfo, modelType: int) -> ModelEntity:
        if modelType == EnumModelTypes.TRANSFORMERS.value:
            model = ModelTransformers()
            model.load(self.getModelPath(modelInfo))
            return model
        raise ValueError("Model not loaded")
