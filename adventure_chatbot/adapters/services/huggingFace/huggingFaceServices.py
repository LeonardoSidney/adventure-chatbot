from huggingface_hub import HfApi
from adventure_chatbot import EnumModelStrings


class HuggingFaceServices:

    def __init__(self) -> None:
        self.api: HfApi = HfApi()

    def downloadModel(self, repoId: str, savePath: str, files: list[str]) -> str:
        model_path = self.api.snapshot_download(
            repo_id=repoId, local_dir=savePath, allow_patterns=files
        )
        return model_path

    def listModel(self, repoId: str) -> list[str]:
        repoFiles: list[str] = self.api.list_repo_files(repo_id=repoId)
        return repoFiles

    def verifyRepoExists(self, repoId: str) -> bool:
        return self.api.repo_exists(repo_id=repoId)
    
    def isHugSubFolder(self, file: str) -> bool:
        for subFolder in EnumModelStrings.SUBFOLDER_SEPARATOR.value:
            if subFolder in file:
                return True
        return False