class ExecuteSqlFile:
    def __init__(self, db_conn, seed_data_file_path):
        self.seed_data_file_path = seed_data_file_path
        self.db_conn = db_conn

    def execute_sql(self):
        db_cursor = self.db_conn.cursor(dictionary=True)
        try:
            with open(self.seed_data_file_path, 'r') as sql_file:
                result_iterator = db_cursor.execute(sql_file.read(), multi=True)
                for res in result_iterator:
                    print("Running query: ", res)  # Will print out a short representation of the query
                    print(f"Affected {res.rowcount} rows")
        except:
            return
        finally:
            self.db_conn.commit()
            db_cursor.close()
            self.db_conn.close()
