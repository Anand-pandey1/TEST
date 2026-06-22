from src.memory.sqlite_memory import SQLiteMemory


class MemoryManager:


    def __init__(self):

        self.memory = SQLiteMemory()

    def remember(
        self,
        key,
        value
    ):

        self.memory.save(
            key,
            value
        )

        return (
            True,
            f"Remembered {key}"
        )

    def recall(self, key):

        value = self.memory.get(key)

        if value:

            return (
                True,
                value
            )

        return (
            False,
            "No memory found"
        )