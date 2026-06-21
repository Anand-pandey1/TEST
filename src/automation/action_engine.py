from src.automation.command_parser import CommandParser

from src.automation.app_control import open_app
from src.automation.process_control import close_app

from src.automation.file_search import FileSearcher
from src.automation.file_manager import FileManager


class ActionEngine:

    def __init__(self):

        self.parser = CommandParser()

        self.searcher = FileSearcher()

        self.file_manager = FileManager()

    def execute(self, command):

        intent = self.parser.parse(
            command
        )

        if not intent:
            return False, "Unknown command"

        action = intent["action"]

        if action == "open_app":

            return open_app(
                intent["target"]
            )

        if action == "close_app":

            return close_app(
                intent["target"]
            )

        if action == "find_file":

            results = self.searcher.search(
                intent["target"]
            )

            if results:

                return True, "\n".join(
                    results
                )

            return False, "File not found"

        if action == "list_files":

            return self.file_manager.list_files(
                intent["target"]
            )

        return False, "Unknown action"