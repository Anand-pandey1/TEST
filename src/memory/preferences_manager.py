from src.memory.sqlite_memory import SQLiteMemory


class PreferencesManager:

    def __init__(self):

        self.db = SQLiteMemory()

    def set_preference(
        self,
        key,
        value
    ):

        self.db.set_preference(
            key,
            value
        )

        return (
            True,
            f"Preference '{key}' saved."
        )

    def get_preference(
        self,
        key
    ):

        value = self.db.get_preference(
            key
        )

        if value:

            return (
                True,
                f"{key} = {value}"
            )

        return (
            False,
            f"Preference '{key}' not found."
        )

    def list_preferences(self):

        preferences = (
            self.db.list_preferences()
        )

        if not preferences:

            return (
                False,
                "No preferences found."
            )

        output = []

        for key, value in preferences:

            output.append(
                f"{key} = {value}"
            )

        return (
            True,
            "\n".join(output)
        )