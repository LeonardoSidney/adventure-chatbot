
from fastapi import FastAPI
from adventure_chatbot.entities.RouterEntity import RouterEntity
from adventure_chatbot.infra.http.services.RoutesServices import RoutesServices
import os

class Routes():
    def __init__(self) -> None:
        path = os.path.dirname(__file__).replace(os.getcwd(), ".")
        self.service = RoutesServices(path)
        

    def execute(self, app: FastAPI):
        routes: list[RouterEntity] = self.service.getRoutes()
        for route in routes:
            route.execute(app)