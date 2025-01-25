import os
import importlib
from types import ModuleType
from adventure_chatbot import RouterEntity, LoggerHelper

class RoutesServices:
    def __init__(self, routesPath: str) -> None:
        self.routesPath = routesPath
        self.logger = LoggerHelper()

    def getRoutes(self):
        routes: list[RouterEntity] = self._findRoutes(self.routesPath)
        return routes

    def _findRoutes(self, dir: str) -> list[RouterEntity]:
        routes: list[RouterEntity] = []
        files: list[str] = []
        for file in os.listdir(dir):
            if file.startswith("__"):
                continue
            if os.path.isdir(f"{dir}/{file}"):
                routes.extend(self._findRoutes(f"{dir}/{file}"))
                continue
            files.append(file)

        for file in files:
            if file.endswith("Router.py"):
                routes.append(self._importRouter(f"{dir}/{file}"))
                
        return routes
    
    def _importRouter(self, path: str) -> RouterEntity:
        className = self._getClassName(path)
        packagePath = self._getPackageFromPath(path)
        module = self._getModule(packagePath, className)
        self.logger.debug(f"Importing {className} from {packagePath}")
        return getattr(module, className)()

    def _getClassName(self, path: str) -> str:
        return path.split("/")[-1].replace(".py", "")
    
    def _getPackageFromPath(self, path: str) -> str:
        return path.replace(f".py", "").replace(".", "").replace('/', '.').replace('.', '', 1)
    
    def _getModule(self, path: str, className: str) -> ModuleType:
        return importlib.import_module(path, package=className)