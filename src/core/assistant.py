from src.core.config import Config
from src.core.event_bus import EventBus

from src.automation.action_engine import ActionEngine

from src.memory.history_manager import (
    HistoryManager
)


class TestAssistant:

    def __init__(self):

        self.config = Config()

        self.event_bus = EventBus()

        self.action_engine = ActionEngine()

        self.name = self.config.get_setting(
            "assistant_name",
            "TEST"
        )

        self.history_manager = (HistoryManager())

    def start(self):

        print("=" * 40)
        print(
            f"{self.name} Assistant Started"
        )
        print("=" * 40)

    def stop(self):

        print("Assistant stopped.")

    def process_command(
        self,
        command
    ):
        if command.lower() not in [
            "history",
            "last command"
        ]:
            self.history_manager.save_command(
                command
            )

        success, message = (
            self.action_engine.execute(
                command
            )
        )

        print(message)