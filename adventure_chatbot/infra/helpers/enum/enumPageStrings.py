from enum import Enum

class enumLanguage(Enum):
    PT_BR = 0
    EN_US = 1

class enumString(Enum):
    def getStr(self, language: enumLanguage) -> str:
        return f"{self.value[language.value]}"

class enumStringTabs(enumString):
    ADVENTURE = ["Aventura", "Adventure"]
    SETTINGS = ["Configurações", "Settings"]
    MODEL = ["Modelo", "Model"]