from adventure_chatbot import (
    HuggingFaceGateway,
    ModelEntity,
    HubEntity,
    ModelInfo,
    ModelServices,
    ModelLoaderServices,
    FolderServices,
    FileServices,
)


class ModelLoaderInteractor:
    def __init__(self, modelInfo: ModelInfo) -> None:
        self.modelInfo: ModelInfo = modelInfo
        self.huggingFaceGateway: HubEntity = HuggingFaceGateway()
        self.modelServices: ModelServices = ModelServices()
        self.folderServices: FolderServices = FolderServices()
        self.service: ModelLoaderServices = ModelLoaderServices()
        self.FileServices: FileServices = FileServices()

    def execute(self) -> bool:
        if not self._verifyModelPath():
            self._downloadModel()
        if not self._verifyModelIntegrity():
            raise Exception("Model integrity check failed")
        return True

    def _verifyModelPath(self) -> bool:
        modelPath = self.modelServices.getModelPath(self.modelInfo)
        if not self._verifyPathIsValid(modelPath):
            return False
        return True

    def _downloadModel(self) -> str:
        return self.huggingFaceGateway.downloadModel(self.modelInfo)

    def _verifyModelIntegrity(self) -> bool:
        files: list[str] = self.huggingFaceGateway.getRepoFiles(self.modelInfo.model_id)
        if not files:
            raise Exception("Model repository is empty")
        modelFiles: list[str] = self.huggingFaceGateway.filterForModelFiles(files)
        if not self._filesExist(modelFiles):
            raise Exception("Model files do not exist")
        return True

    def _verifyPathIsValid(self, modelPath: str) -> bool:
        return self.folderServices.verifyFolderExists(modelPath)

    def _filesExist(self, files: list[str]) -> bool:
        for file in files:
            modelPath: str = self.modelServices.getModelPath(self.modelInfo)
            filePath: str = f"{modelPath}/{file}"
            if not self.FileServices.checkFileExists(filePath):
                return False
        return True
