import ctypes
import sys


def is_admin():
    try:
        # Check if the user is an administrator
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False


def run_as_admin():
    try:
        # Call ShellExecute with the "runas" verb to request elevation
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "elevated_operations.py", None, 1)
    except:
        # An error occurred or the user declined the elevation request
        print("Failed to run as administrator.")
