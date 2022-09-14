from src.fileoperations.directorycheck import DirectoryCheck


class TestDirectory:
    def setup(self):
        self.directory = DirectoryCheck('scripts')

    def test_should_return_false_if_not_exists(self):
        result = self.directory.check_if_exists()
        assert result == 0

    def test_should_return_true_if_exists(self):
        self.directory = DirectoryCheck('/test/test_directory')
        result = self.directory.check_if_exists()
        assert result == 1
