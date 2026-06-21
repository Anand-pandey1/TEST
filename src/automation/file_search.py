from pathlib import Path
import subprocess
import os


class FileSearcher:

    def search(self, filename):

        results = []

        # Strategy 1: Use Windows 'where' command (fastest)
        try:
            result = subprocess.run(
                ['where', '/R', 'C:\\', filename],
                capture_output=True,
                timeout=10,
                text=True
            )
            if result.returncode == 0:
                paths = result.stdout.strip().split('\n')
                results.extend([p for p in paths if p])
                return results
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        # Strategy 2: Search in common directories
        common_dirs = [
            "C:\\Users",
            "C:\\Program Files",
            "C:\\Program Files (x86)",
            "D:\\",
            "E:\\",
            "F:\\"
        ]

        for dir_path in common_dirs:
            path = Path(dir_path)
            if not path.exists():
                continue

            try:
                # Limit depth to 3 levels for speed
                for root, dirs, files in os.walk(path):
                    depth = root.replace(str(path), '').count(os.sep)
                    if depth > 3:
                        # Skip subdirectories to limit depth
                        dirs.clear()
                    
                    if filename.lower() in [f.lower() for f in files]:
                        full_path = Path(root) / filename
                        if full_path.exists():
                            results.append(str(full_path))

            except (PermissionError, Exception):
                pass

        return results