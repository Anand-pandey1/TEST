import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src.core.assistant import TestAssistant


def main():

    test = TestAssistant()

    test.start()

    while True:

        command = input("TEST > ").strip()

        if not command:
            continue

        if command.lower() == "exit":

            test.stop()

            break

        test.process_command(command)


if __name__ == "__main__":
    main()