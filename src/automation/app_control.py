import subprocess
import shutil
import time
import pyautogui


WINDOWS_APP_MAP = {
    "calculator": "calc",
    "notepad": "notepad",
    "paint": "mspaint",
    "explorer": "explorer",
    "cmd": "cmd",
    "powershell": "powershell",
    "edge": "msedge"
}


def open_app(app_name: str):

    app_name = app_name.lower().strip()

    # Strategy 1
    if app_name in WINDOWS_APP_MAP:

        try:
            target = WINDOWS_APP_MAP[app_name]

            if target.startswith("start "):
                subprocess.Popen(target, shell=True)
            else:
                subprocess.Popen(target)

            return True, f"Opened {app_name}"

        except Exception:
            pass

    # Strategy 2
    executable = shutil.which(app_name)

    if executable:

        try:
            subprocess.Popen(executable)
            return True, f"Opened {app_name}"

        except Exception:
            pass

    # Strategy 3
    try:

        pyautogui.press("win")

        time.sleep(1)

        pyautogui.write(app_name)

        time.sleep(1)

        pyautogui.press("enter")

        return True, f"Attempted to open {app_name}"

    except Exception as e:

        return False, str(e)