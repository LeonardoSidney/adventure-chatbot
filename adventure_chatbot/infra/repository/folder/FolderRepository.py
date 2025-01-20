from yaml import load, Loader
from adventure_chatbot import configType, configFileType

class FolderRepository:
    def __init__(self):
        self.configFileLocation = "config/config.yml"
        self.folderConfigTag = "folders"

    def getFoldersConfig(self) -> configType:
        configFile: configFileType = self._getConfigFile()
        config : configType = self._getConfig(configFile)
        return config

    def _getConfigFile(self) -> configFileType:
        with open(self.configFileLocation, "r") as rawFile:
            file: configFileType = load(rawFile, Loader=Loader)
        return file

    def _getConfig(self, configFile: configFileType) -> configType:
        return configFile[self.folderConfigTag]
