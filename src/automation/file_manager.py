from pathlib import Path
import shutil


class FileManager:

    def create_folder(self, path):

        try:

            Path(path).mkdir(
                parents=True,
                exist_ok=True
            )

            return True, f"Created folder: {path}"

        except Exception as e:

            return False, str(e)

    def create_text_file(self, path):

        try:

            Path(path).touch()

            return True, f"Created file: {path}"

        except Exception as e:

            return False, str(e)

    def delete_file(self, path):

        try:

            Path(path).unlink()

            return True, f"Deleted: {path}"

        except Exception as e:

            return False, str(e)

    def delete_folder(self, path):

        try:

            shutil.rmtree(path)

            return True, f"Deleted folder: {path}"

        except Exception as e:

            return False, str(e)

    def move_file(self, source, destination):

        try:

            shutil.move(source, destination)

            return True, f"Moved {source} to {destination}"

        except Exception as e:

            return False, str(e)

    def list_files(self, path):

        try:

            files = []

            for item in Path(path).iterdir():

                files.append(
                    item.name
                )

            return True, "\n".join(files)

        except Exception as e:

            return False, str(e)