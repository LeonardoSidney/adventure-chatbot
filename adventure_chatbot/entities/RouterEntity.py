from abc import ABC, abstractmethod

from fastapi import FastAPI

class RouterEntity(ABC):
    @abstractmethod
    def execute(self, app: FastAPI):
        pass