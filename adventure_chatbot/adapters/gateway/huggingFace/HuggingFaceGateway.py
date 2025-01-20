from adventure_chatbot import ModelServices, HuggingFaceServices, ModelInfo, HubEntity


class HuggingFaceGateway(HubEntity):
    def __init__(self) -> None:
        self.service = HuggingFaceServices()
        self.modelServices = ModelServices()

    def downloadModel(self, modelInfo: ModelInfo) -> str:
        if not self._verifyRepoExists(modelInfo.model_id):
            raise Exception("Model does not exist")
        files: list[str] = self.getRepoFiles(modelInfo.model_id)
        if not files:
            raise Exception("Model repository is empty")
        modelFiles: list[str] = self.filterForModelFiles(files)
        savePath: str = self.modelServices.getModelPath(modelInfo)
        return self.service.downloadModel(modelInfo.model_id, savePath, modelFiles)

    def getRepoFiles(self, repo_id: str) -> list[str]:
        return self.service.listModel(repo_id)

    def filterForModelFiles(self, repoFiles: list[str]) -> list[str]:
        files: list[str] = []
        for file in repoFiles:
            if not self._isSubFolder(file):
                if self._isModelFile(file) or self._isConfigFile(file):
                    files.append(file)
        if not files:
            raise Exception("Can't find model files")
        return files

    def _verifyRepoExists(self, repo_id: str) -> bool:
        return self.service.verifyRepoExists(repo_id)

    def _isModelFile(self, file: str) -> bool:
        return self.modelServices.isModelFile(file)

    def _isConfigFile(self, file: str) -> bool:
        return self.modelServices.isConfigFile(file)

    def _isSubFolder(self, file: str) -> bool:
        return self.service.isHugSubFolder(file)
