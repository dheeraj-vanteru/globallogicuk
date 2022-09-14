from src.databaseoperations.connect import DatabaseConnection


class TestDbConnect:
    def setup(self):
        self.connection = DatabaseConnection('mysql_container', 'dev', '123456', 'devopstt')

    def test_database_connection(self):
        result = connect()
        print(result.get_server_info())
        assert result.get_server_info()
        result.close()
