import unittest


class BarhopTestCase(unittest.TestCase):
    def login_client(self):
        self.sucess_test_params = []

        self.failure_test_params = []

    def login__mocked_server(self):
        self.sucess_test_params = []

        self.failure_test_params = []

    def signin_client(self):
        self.sucess_test_params = []

        self.failure_test_params = []

    def signin_unmocked_client(self):
        self.sucess_test_params = []

        self.failure_test_params = []


if __name__ == "__main__":
    unittest.main()
