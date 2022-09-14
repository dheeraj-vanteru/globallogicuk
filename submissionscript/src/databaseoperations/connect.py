import mysql.connector


class DatabaseConnect:
    def __init__(self, host, user, password, name):
        self.host = host
        self.user = user
        self.password = password
        self.name = name

    def connect(self):
        return mysql.connector.connect(host=self.host, user=self.user, passwd=self.password,
                                       database=self.name)
