import glob
import os


class DirectoryContents:
    def __init__(self, directory_path):
        self.path = directory_path

    def get_files(self):
        os.chdir(self.path)
        files = [os.path.join(os.getcwd(), f) for f in os.listdir(os.curdir) if os.path.isfile(f)]
        os.chdir('/')
        return files
