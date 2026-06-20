from src.automation.app_control import open_app
from src.automation.process_control import close_app


class ActionEngine:

    def execute(self, command: str):

        command = command.strip().lower()

        if command.startswith("open "):

            app = command.replace(
                "open ",
                "",
                1
            ).strip()

            return open_app(app)

        if command.startswith("close "):

            app = command.replace(
                "close ",
                "",
                1
            ).strip()

            return close_app(app)

        return False, "Unknown command"