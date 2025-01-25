from reactpy import html

class SettingsPage:
    def __init__(self):
        pass

    def get(self):
        return html.div(
            {"class": "container-fluid"},
            "Settings"
        )