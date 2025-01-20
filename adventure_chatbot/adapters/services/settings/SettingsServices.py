from adventure_chatbot import configType, FolderRepository


class SettingsServices:
    def __init__(self) -> None:
        self.folderRepository = FolderRepository()

    def getFoldersName(self, foldersConfig: configType) -> list[str]:
        foldersName: list[str] = []
        for folder in foldersConfig:
            foldersName.append(folder["name"])
        return foldersName

    def getFoldersLocation(self, foldersConfig: configType) -> list[str]:
        foldersLocation: list[str] = []
        for folder in foldersConfig:
            foldersLocation.append(folder["location"])
        return foldersLocation

    def getFoldersLayout(self, foldersConfig: configType) -> dict[str, list[str]]:
        foldersName = self.getFoldersName(foldersConfig)
        foldersLocation = self.getFoldersLocation(foldersConfig)
        foldersLayout: dict[str, list[str]] = {
            "Name": foldersName,
            "Location": foldersLocation,
        }
        return foldersLayout

    def getFoldersConfig(self) -> configType:
        folderConfig: configType = self.folderRepository.getFoldersConfig()
        return folderConfig
