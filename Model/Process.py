import shlex
import subprocess
from enum import Enum


class CommandType(Enum):
    LIST = 'nvm list'
    USE = 'nvm use'


class Process:
    def __init__(self, command_type: CommandType):
        self.command: str = command_type.value

    def communicate(self) -> tuple[bool, str]:
        args = shlex.split(self.command)
        # Create subprocess and specify the shell as True to run in Windows PowerShell
        process = subprocess.Popen(args, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)

        # Wait for the process to finish and get the output
        stdout, stderr = process.communicate()

        # Check the output
        if stdout:
            # Process and handle the output as needed
            output = stdout.decode("utf-8")
            return True, output

        else:
            # Handle any errors or empty output
            error_message = stderr.decode("utf-8")
            return False, error_message
