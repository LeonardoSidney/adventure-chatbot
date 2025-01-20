from adventure_chatbot import FileRepository


class FileServices:
    def __init__(self):
        self.repository = FileRepository()

    def checkFileExists(self, filePath: str) -> bool:
        return self.repository.checkFileExists(filePath)