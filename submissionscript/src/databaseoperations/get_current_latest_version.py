class CurrentLatestVersion:
    def __init__(self, db_conn):
        self.db_conn = db_conn

    def get_version(self):
        cursor = self.db_conn.cursor(dictionary=True)
        cursor.execute("SELECT max(version) as version FROM versionTable;")
        result = cursor.fetchone()['version']
        return result
