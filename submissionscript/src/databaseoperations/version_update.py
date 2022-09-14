class VersionUpdate:
    def __init__(self, db_conn, version):
        self.db_conn = db_conn
        self.version = version

    def update(self):
        cursor = self.db_conn.cursor()
        try:
            cursor.execute("INSERT INTO versionTable (version) VALUES ({0});".format(self.version))
            self.db_conn.commit()
        except:
            raise
        finally:
            cursor.close()
            if self.db_conn.is_connected():
                self.db_conn.close()
