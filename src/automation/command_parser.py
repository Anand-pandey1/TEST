import re

class CommandParser:

    def parse(self, command):

        command = re.sub(r"\s+", " ", command.strip().lower())

        if command.startswith("open "):
            return {
                "action": "open_app",
                "target": command[5:]
            }

        if command.startswith("close "):
            return {
                "action": "close_app",
                "target": command[6:]
            }

        if command.startswith("find file "):
            return {
                "action": "find_file",
                "target": command[10:]
            }

        if command.startswith("find "):
            return {
                "action": "find_file",
                "target": command[5:]
            }

        if command.startswith("search for "):
            return {
                "action": "find_file",
                "target": command[11:]
            }

        if command.startswith("search "):
            return {
                "action": "find_file",
                "target": command[7:]
            }

        if command.startswith("list files in "):
            return {
                "action": "list_files",
                "target": command.replace(
                    "list files in ",
                    ""
                )
            }

        return None