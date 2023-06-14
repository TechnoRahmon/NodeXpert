import sys

from Utils.privileges import is_admin, run_as_admin



if __name__ == '__main__':
    # Example usage
    if is_admin():
        import elevated_operations
        elevated_operations.main()
    else:
        run_as_admin()


# TODO:
# NVM version buttons : if NVM not installed > disable the table list
# Stop all node instance

# v2
# install node version
# crud start/stop your npm project
# log error expand > show terminal section
