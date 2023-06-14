import json
import os

import settings
from Model.NodeVersion import NodeVersion, NoteItem
from Model.Process import Process, CommandType
from Utils.ShellParser import parse_nvm_list_command, parse_nvm_use_command


class NvmController:
    def __init__(self):
        self.node_versions = NodeVersion()

    def get_node_versions_list(self):
        self.load_nvm_versions()
        self.load_notes()
        return self.node_versions.merge_all()

    def load_notes(self):
        """ load the notes from json, if the file not exist, then create JSON with the loaded
            NVM versions
        """
        try:
            with open(settings.nvm_file_path, 'r') as file:
                data = json.loads(file.read())
                self.node_versions.add_notes_list(data)
        except FileNotFoundError:
            self.check_file_center_dir()
            data ={}
            for item in self.node_versions.versions:
                data[item["version"]] = ""
            self.node_versions.add_notes_list(data)
            json_data = json.dumps(data)
            self.save_file(json_data)

    def update_notes(self, new_note: NoteItem):
        self.node_versions.notes[new_note.version] = new_note.notes
        json_data = json.dumps(self.node_versions.notes)
        self.save_file(json_data)

    def save_file(self, notes: str):
        # open file
        with open(settings.nvm_file_path, 'w') as file:
            file.write(notes)

    def load_nvm_versions(self) -> bool:
        process = Process(command_type=CommandType.LIST)
        success, output = process.communicate()
        if success:
            versions_list = parse_nvm_list_command(output)
            self.node_versions.add_versions_list(versions_list)

        return success

    def set_new_active_version(self, version_number: str) -> tuple[bool, str]:
        # prepare the nvm use command process
        process = Process(command_type=CommandType.USE, version_number=version_number)
        # execute the process
        success, output = process.communicate()
        # pares the output of the terminal
        return parse_nvm_use_command(output)

    def check_file_center_dir(self):
        directory = os.path.dirname(settings.nvm_file_path)

        # Check if the directory exists
        if not os.path.exists(directory):
            # Create the directory if it doesn't exist
            os.makedirs(directory)
