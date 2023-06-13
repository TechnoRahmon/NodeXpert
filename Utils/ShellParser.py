from Model.NodeVersion import NvmItem


def parse_active_version(item: str):
    if item.startswith('*'):
        version_name = item.split()[1]
        return NvmItem(version_name, True).to_dict()
    return NvmItem(item, False).to_dict()


def parse_nvm_list_command(output: str) -> list:
    version_filtered_list = filter(lambda v: v, [version.strip() for version in output.splitlines()])
    version_list = map(parse_active_version, version_filtered_list)
    return list(version_list)