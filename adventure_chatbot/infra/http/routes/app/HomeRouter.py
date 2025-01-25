from typing import Any
from adventure_chatbot import RouterEntity, HomeController
from reactpy.backend.fastapi import configure, Options


class HomeRouter(RouterEntity):
    def execute(self, app):
        homeController = HomeController()
        configure(
            app, 
            homeController.index(),
            Options(
                url_prefix="/app",
                head=homeController.page.header()
            )
        )