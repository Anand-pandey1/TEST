from pathlib import Path


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