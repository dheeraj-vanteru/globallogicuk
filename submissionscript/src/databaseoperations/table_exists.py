class TableExists:
    def __init__(self, db_conn, table_name):
        self.db_conn = db_conn
        self.table_name = table_name

    def check(self):
        db_cursor = self.db_conn.cursor()
        try:
            db_cursor.execute("""
                SELECT COUNT(*)
                FROM information_schema.tables
                WHERE table_name = '{0}'
                """.format(self.table_name))
            if db_cursor.fetchone()[0] == 1:
                db_cursor.close()
                return True
        except:
            raise
        finally:
            db_cursor.close()
            self.db_conn.close()
            return False
