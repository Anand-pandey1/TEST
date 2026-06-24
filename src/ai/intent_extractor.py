import re

from click import command


class IntentExtractor:

    def extract(self, command):

        command = command.lower().strip()

        # OPEN MY EDITOR

        if command == "open my editor":
        
            return "open_preference editor"

# OPEN MY BROWSER

        if command == "open my browser":

            return "open_preference browser"

# OPEN MY WORKSPACE

        if command == "open my workspace":

            return "open_preference workspace"

# USE MY PREFERRED DRIVE

        if command == "use my preferred drive":

            return "show_preference favorite_drive"

        # CREATE FOLDER

        patterns = [
            r"make a folder called (.+?) on (.+)",
            r"create a folder called (.+?) on (.+)",
            r"create folder (.+?) in (.+)",
            r"make directory (.+?) on (.+)",
        ]

        for pattern in patterns:

            match = re.match(
                pattern,
                command
            )

            if match:

                folder = match.group(1).strip()
                drive = match.group(2).strip()

                return (
                    f"create folder {folder} in {drive}"
                )

        # FIND FILE

        patterns = [
            r"find (.+)",
            r"locate (.+)",
            r"search for (.+)"
        ]

        for pattern in patterns:

            match = re.match(
                pattern,
                command
            )

            if match:

                filename = match.group(1)

                return (
                    f"find {filename}"
                )

        return command