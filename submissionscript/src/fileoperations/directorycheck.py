import os
from os import path


class DirectoryCheck:
    def __init__(self, scripts_path):
        self.scripts_path = scripts_path

    def check_if_exists(self):
        os.chdir('../../')
        return path.exists(str.format('/{0}', self.scripts_path))
