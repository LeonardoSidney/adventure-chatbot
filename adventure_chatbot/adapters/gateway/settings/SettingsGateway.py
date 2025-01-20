from adventure_chatbot import configType, SettingsServices, FolderServices


class SettingsGateway:
    def __init__(self) -> None:
        self.service = SettingsServices()
        self.folderServices = FolderServices()

    def getFoldersLocation(self) -> configType:
        folderConfig: configType = self.service.getFoldersConfig()
        validFolders: configType = self.folderServices.getValidFolders(folderConfig)
        return validFolders