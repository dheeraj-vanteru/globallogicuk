from src.databaseoperations.table_exists import TableExists
from src.databaseoperations.execute_sql_file import ExecuteSqlFile
from src.databaseoperations.get_current_latest_version import CurrentLatestVersion
from src.databaseoperations.version_update import VersionUpdate
from src.fileoperations.directorycontents import DirectoryContents
from src.fileoperations.file_version import FileVersion


class DbUpdateEngine:
    def __init__(self, seed_dir_path, scripts_dir_path, db_conn):
        self.seed_dir_path = seed_dir_path
        self.db_conn = db_conn
        self.scripts_dir_path = scripts_dir_path

    def execute_seed_data(self):
        directory_content = DirectoryContents(self.seed_dir_path)
        table_exists = TableExists(self.db_conn.connect(), 'versionTable')
        if not table_exists:
            print('Seed Data')
            files = directory_content.get_files()
            for file in files:
                execute_sql_file = ExecuteSqlFile(self.db_conn.connect(), file)
                execute_sql_file.execute_sql()

    def execute_scripts_data(self):
        try:
            print('Version table exists in database')
            version = CurrentLatestVersion(self.db_conn.connect()).get_version()
            directory_content = DirectoryContents(self.scripts_dir_path)
            files = directory_content.get_files()
            for file in files:
                print(file)
                file_version = FileVersion(file).extract()
                if file_version.isnumeric() and int(file_version) > version:
                    execute_sql_file = ExecuteSqlFile(self.db_conn.connect(), file)
                    execute_sql_file.execute_sql()
                    VersionUpdate(self.db_conn.connect(), int(file_version)).update()
        except StopIteration:
            return