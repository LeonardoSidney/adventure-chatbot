from adventure_chatbot import SettingsGateway


class SettingsController:
    def __init__(self):
        self.gateway = SettingsGateway()

    def getFoldersName(self):
        return self.gateway.getFoldersLocation()