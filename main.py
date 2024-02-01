import sys
from Utils.privileges import is_admin, run_as_admin
import os




def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)



if __name__ == '__main__':
    # Example usage
    if is_admin():
        import elevated_operations
        elevated_operations.main()
    else:
        run_as_admin()


# TODO:
# Stop all node instance

# v2
# install node version
# crud start/stop your npm project
# log error expand > show terminal section
