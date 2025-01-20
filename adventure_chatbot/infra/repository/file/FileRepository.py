import os

class FileRepository:
    def checkFileExists(self, file_path: str) -> bool:
        return os.path.exists(file_path)