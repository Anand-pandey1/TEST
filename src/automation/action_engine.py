from src.automation.command_parser import CommandParser

from src.automation.app_control import open_app
from src.automation.process_control import close_app

from src.automation.file_search import FileSearcher
from src.automation.file_manager import FileManager
from src.automation.storage_resolver import StorageResolver

from src.memory.memory_manager import (
    MemoryManager
)

from src.memory.preferences_manager import (
    PreferencesManager
)


class ActionEngine:

    def __init__(self):

        self.parser = CommandParser()

        self.searcher = FileSearcher()

        self.file_manager = FileManager()

        self.storage_resolver = StorageResolver()

        self.memory_manager = (MemoryManager())

        self.preferences_manager = (PreferencesManager())



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

            target = intent["target"]
            resolved_path = self.storage_resolver.resolve(target)
            
            if resolved_path:
                return self.file_manager.list_files(resolved_path)
            
            return self.file_manager.list_files(target)

        if action == "create_folder":

            target = intent["target"]
            resolved_path = self.storage_resolver.resolve(target)

            if resolved_path:
                # Extract folder name and build full path
                folder_name = target.split()
                if folder_name:
                    folder_name = folder_name[0]
                    full_path = resolved_path + folder_name
                    return self.file_manager.create_folder(full_path)
            
            return self.file_manager.create_folder(target)

        if action == "create_file":

            target = intent["target"]
            resolved_path = self.storage_resolver.resolve(target)

            if resolved_path:
                # Extract file name and build full path
                file_name = target.split()
                if file_name:
                    file_name = file_name[0]
                    full_path = resolved_path + file_name
                    return self.file_manager.create_text_file(full_path)
            
            return self.file_manager.create_text_file(target)

        if action == "delete_folder":

            target = intent["target"]
            resolved_path = self.storage_resolver.resolve(target)

            if resolved_path:
                # Extract folder name and build full path
                folder_name = target.split()
                if folder_name:
                    folder_name = folder_name[0]
                    full_path = resolved_path + folder_name
                    return self.file_manager.delete_folder(full_path)
            
            return self.file_manager.delete_folder(target)

        if action == "delete_file":

            target = intent["target"]
            resolved_path = self.storage_resolver.resolve(target)

            if resolved_path:
                # Extract file name and build full path
                file_name = target.split()
                if file_name:
                    file_name = file_name[0]
                    full_path = resolved_path + file_name
                    return self.file_manager.delete_file(full_path)
            
            return self.file_manager.delete_file(target)

        if action == "move_file":

            source = intent["source"]
            destination = intent["destination"]
            
            # Build source path
            source_resolved = self.storage_resolver.resolve(source)
            if source_resolved:
                source_path = source.lower()
                for drive, drive_path in self.storage_resolver.DRIVES.items():
                    source_path = source_path.replace(drive + " ", "")
                source = source_resolved + source_path.replace(" ", "\\")
            
            # Build destination path
            dest_resolved = self.storage_resolver.resolve(destination)
            if dest_resolved:
                dest_path = destination.lower()
                for drive, drive_path in self.storage_resolver.DRIVES.items():
                    dest_path = dest_path.replace(drive + " ", "")
                destination = dest_resolved + dest_path.replace(" ", "\\")
            
            return self.file_manager.move_file(source, destination)
        
        if action == "remember":

            return self.memory_manager.remember(
                intent["key"],
                intent["value"]
            )

        if action == "recall":

            return self.memory_manager.recall(
                intent["key"]
            )
        
        #day4
        if action == "set_preference":

            return (
                self.preferences_manager
                .set_preference(
                    intent["key"],
                    intent["value"]
                )
            )


        if action == "get_preference":

            return (
                self.preferences_manager
                .get_preference(
                    intent["key"]
                )
            )


        if action == "list_preferences":

            return (
                self.preferences_manager
                .list_preferences()
            )

        return False, "Unknown action"