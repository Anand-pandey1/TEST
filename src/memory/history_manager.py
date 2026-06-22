from src.memory.sqlite_memory import SQLiteMemory

MAX_HISTORY = 25

class HistoryManager:

    def __init__(self):

        self.db = SQLiteMemory()

    def save_command(
        self,
        command
    ):

        self.db.add_history(
            command
        )

    def get_history(self):

        history = self.db.get_history()

        if not history:

            return (
                False,
                "No history found."
            )

        commands = []

        for item in history:

            commands.append(
                item[0]
            )

        return (
            True,
            "\n".join(commands)
        )

    def get_last_command(self):

        history = self.db.get_history(
            limit=2
        )

        if len(history) >= 2:

            return (
                True,
                history[1][0]
            )

        return (
         False,
            "No previous command found."
        )
