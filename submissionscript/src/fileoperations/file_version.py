import re


class FileVersion:
    def __init__(self, file_name):
        self.file_name = file_name

    def extract(self):
        split_string = re.split(r"\ +|\.+", self.file_name)
        return split_string[0].split('/')[2]
