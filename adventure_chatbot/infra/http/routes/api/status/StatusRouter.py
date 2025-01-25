from fastapi import FastAPI
from adventure_chatbot import RouterEntity, SettingsGateway


class StatusRouter(RouterEntity):
    def execute(self, app: FastAPI):
        settings = SettingsGateway()

        async def status():
            return settings.getFoldersLocation()

        app.add_api_route("/api/folders", status, methods=["GET"])