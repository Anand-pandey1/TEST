import re

from click import command

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

        if command.startswith("create folder "):
            return {
                "action": "create_folder",
                "target": command[14:]
            }

        if command.startswith("delete folder "):
            return {
                "action": "delete_folder",
                "target": command[14:]
            }

        if command.startswith("delete file "):
            return {
                "action": "delete_file",
                "target": command[12:]
            }

        if command.startswith("move "):
            parts = command[5:].split(" to ")
            if len(parts) == 2:
                return {
                    "action": "move_file",
                    "source": parts[0].strip(),
                    "destination": parts[1].strip()
                }

        if command.startswith("create file "):
            return {
                "action": "create_file",
                "target": command[12:]
            }

        if command.startswith("list files in "):
            return {
                "action": "list_files",
                "target": command.replace(
                    "list files in ",
                    ""
                )
            }
        if command.startswith("remember "):
            parts = command.replace(
                "remember ",
                ""
            )

            if "=" in parts:

                key, value = parts.split(
                    "=",
                    1
                )

                return {
                    "action": "remember",
                    "key": key.strip(),
                    "value": value.strip()
                }

        if command.startswith("recall "):

            key = command.replace(
                "recall ",
                ""
            ).strip()

            return {
                "action": "recall",
                "key": key
            }

        #day 4 logic
        if command.startswith(
            "set preference "
        ):

            content = command.replace(
                "set preference ",
                ""
            )

            if "=" in content:

                key, value = content.split(
                    "=",
                    1
                )

                return {
                    "action": "set_preference",
                    "key": key.strip(),
                    "value": value.strip()
                }


        if command.startswith(
            "get preference "
        ):

            key = command.replace(
                "get preference ",
                ""
            ).strip()

            return {
                "action": "get_preference",
                "key": key
            }


        if command == "list preferences":

            return {
                "action": "list_preferences"
            }
        

        if command == "history":

            return {
                "action": "history"
            }   


        if command == "last command":

            return {
                "action": "last_command"
            }
        

        
        return None