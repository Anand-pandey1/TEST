from src.ai.intent_extractor import (
    IntentExtractor
)


class NLU:

    def __init__(self):

        self.extractor = (
            IntentExtractor()
        )

    def process(
        self,
        command
    ):

        return self.extractor.extract(
            command
        )