from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from adventure_chatbot import RouterEntity


class StaticRouter(RouterEntity):
    def execute(self, app: FastAPI):
        # app.mount("/static", StaticFiles(directory="./adventure_chatbot/frontend/", html=True), name="index.js")
        pass