import psutil
import pygetwindow as gw
import pyautogui
import time


PROCESS_MAP = {
    "calculator": ["calculatorapp.exe", "calc.exe"],
    "notepad": ["notepad.exe"],
    "paint": ["mspaint.exe"],
    "edge": ["msedge.exe"],
    "cmd": ["cmd.exe"],
    "powershell": ["powershell.exe"]
}


def close_app(app_name: str):

    app_name = app_name.lower().strip()

    # Strategy 1
    try:

        windows = gw.getWindowsWithTitle(app_name)

        for window in windows:

            if window.isVisible:
                window.close()

                return True, f"Closed {app_name}"

    except Exception:
        pass

    # Strategy 2
    if app_name in PROCESS_MAP:

        try:

            targets = PROCESS_MAP[app_name]

            for process in psutil.process_iter(
                ["pid", "name"]
            ):

                name = process.info["name"]

                if name and name.lower() in targets:

                    process.kill()

                    return True, f"Killed {app_name}"

        except Exception:
            pass

    # Strategy 3
    try:

        pyautogui.hotkey("alt", "f4")

        time.sleep(0.5)

        return True, "Sent Alt+F4"

    except Exception as e:

        return False, str(e)

    return False, f"Could not close {app_name}"