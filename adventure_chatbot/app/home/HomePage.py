from reactpy import component, html, use_state

from adventure_chatbot.infra.helpers.enum.enumPageStrings import (
    enumLanguage,
    enumStringTabs,
)


class HomePage:
    def __init__(self):
        self.language = enumLanguage.PT_BR

    def header(self):
        return html.head(
            html.link(
                {
                    "href": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css",
                    "crossorigin": "anonymous",
                    "rel": "stylesheet",
                }
            ),
            html.script(
                {
                    "src": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js",
                    "crossorigin": "anonymous",
                }
            ),
            html.title("Adventure chatbot"),
        )

    @component
    def page(self):
        self.currentTab, self.setCurrentTab = use_state("tab-adventure")
        return html.div(
            {"class": "container-fluid"},
            self._home(),
        )

    def _home(self):
        self.tabs = [
            {
                "text": enumStringTabs.ADVENTURE.getStr(self.language),
                "id": "tab-adventure",
                "render": lambda: html.div("Adventure"),
            },
            {
                "text": enumStringTabs.SETTINGS.getStr(self.language),
                "id": "tab-settings",
                "render": lambda: html.div("Settings"),
            },
            {
                "text": enumStringTabs.MODEL.getStr(self.language),
                "id": "tab-model",
                "render": lambda: html.div("Model"),
            },
        ]
        return html.div(
            html.ul(
                {"class": "nav nav-tabs", "id": "tabs-panel", "role": "tablist"},
                self._tabs(self.tabs),
            ),
            html.div(
                {"class": "tab-content", "id": "tabs-content"},
                self._tabContent(self.tabs),
            ),
        )

    def _tabs(self, tabs):
        for tab in tabs:
            yield self._tabsName(tab["text"], tab["id"])

    def _tabsName(self, name, id):
        activeTag = "false"
        activeClass = ""
        if self.currentTab == id:
            activeTag = "true"
            activeClass = "active"

        return html.li(
            {"class": "nav-item"},
            html.li(
                {"class": "nav-item", "role": "presentation"},
                html.button(
                    {
                        "class": f"nav-link {activeClass}",
                        "id": f"{id}-tab",
                        "data-bs-toggle": "tab",
                        "data-bs-target": f"#{id}-tab-pane",
                        "type": "button",
                        "role": "tab",
                        "aria-controls": f"{id}-tab-pane",
                        "aria-selected": activeTag,
                    },
                    name,
                ),
            ),
        )

    def _tabContent(self, tabs):
        for tab in tabs:
            yield self._tabContentRender(
                tab["id"],
                tab["render"],
            )

    def _tabContentRender(self, id, render):
        activeClass = ""
        if self.currentTab == id:
            activeClass = "show active"
        
        return html.div(
            {
                "class": f"tab-pane fade {activeClass}",
                "id": f"{id}-tab-pane",
                "role": "tabpanel",
                "aria-labelledby": f"{id}-tab",
                "tabindex": "0",
            },
            render(),
        )
