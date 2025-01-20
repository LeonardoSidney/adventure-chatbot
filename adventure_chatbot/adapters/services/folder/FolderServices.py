import os
from adventure_chatbot import configType


class FolderServices:
    def __init__(self) -> None:
        pass

    def verifyFolderExists(self, folderPath: str) -> bool:
        if not os.path.exists(folderPath):
            return False
        return True

    def getValidFolders(self, foldersConfig: configType) -> configType:
        validFolders: configType = []
        for folder in foldersConfig:
            if self.verifyFolderExists(folder["location"]):
                validFolders.append(folder)
        return validFolders
