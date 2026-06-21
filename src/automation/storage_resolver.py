class StorageResolver:

    DRIVES = {
        "c drive": "C:\\",
        "d drive": "D:\\",
        "e drive": "E:\\",
        "f drive": "F:\\",
        "g drive": "G:\\"
    }

    def resolve(self, text):

        text = text.lower()

        for drive_name, path in self.DRIVES.items():

            if drive_name in text:

                return path

        return None