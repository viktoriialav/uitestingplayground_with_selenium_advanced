from pathlib import Path

import project_tests


def abs_path_from_root(path):
    return Path(project_tests.__file__).parent.parent.joinpath(path).absolute().__str__()
