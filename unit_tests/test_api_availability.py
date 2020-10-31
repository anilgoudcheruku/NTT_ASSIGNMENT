import unittest
from tabulate import tabulate
from flask import Flask, session
from app_api import app_api
app = Flask(__name__)
app.register_blueprint(app_api)
stdout = []


class TestApi(unittest.TestCase):
    """
        test to ensure REST API endpoint names and its availability
    """
    def setUp(self):
        pass
        self.client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        print(tabulate(stdout, ["Test Description", "Remarks"],
                       tablefmt="grid"))

    def test_interfaces_api_is_available(self):
        """
        test to check api get method availability
        """
        pass
        response = self.client.get('/NTTGN/Interfaces')
        self.assertTrue(response.status_code == 200)
        stdout.append(["test to check api get method availability", "SUCCESS"])

    def test_interface_with_value_api_is_available(self):
        """
        test to check API GET method is available for Interface value
        """
        pass
        response = self.client.get('/NTTGN/Interfaces/incorect_value')
        self.assertTrue(response.status_code == 404)
        stdout.append(["test to check API GET method is available for "
                       "Interface INCORRECT value", "SUCCESS"])
        response = self.client.get('/NTTGN/Interfaces/GigabitEthernet0/0')
        self.assertTrue(response.status_code == 200)
        stdout.append(["test to check API GET method is available for "
                       "Interface CORRECT value", "SUCCESS"])

    def test_api_http_methods_eligibility(self):
        """
        test to check API POST, PUT and DELETE method is NOT available for
        Interfaces URL
        """
        response = self.client.post('/NTTGN/Interfaces')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API POST method is NOT available for "
                       "Interfaces URL", "SUCCESS"])
        response = self.client.put('/NTTGN/Interfaces')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API PUT method is NOT available for "
                       "Interfaces URL", "SUCCESS"])
        response = self.client.delete('/NTTGN/Interfaces')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API DELETE method is NOT available for "
                       "Interfaces URL", "SUCCESS"])

        response = self.client.post('/NTTGN/Interfaces/1')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API POST method is NOT available for "
                       "Interface URL", "SUCCESS"])
        response = self.client.put('/NTTGN/Interfaces/2')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API PUT method is NOT available for "
                       "Interfaces URL", "SUCCESS"])
        response = self.client.delete('/NTTGN/Interfaces/3')
        self.assertTrue(response.status_code == 405)
        stdout.append(["test to check API DELETE method is NOT available for "
                       "Interfaces URL", "SUCCESS"])


def suite():
    s = unittest.TestSuite()
    s.addTests(

        unittest.TestLoader().loadTestsFromTestCase(TestApi)

    )

    return s


if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
