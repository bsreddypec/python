# tests/test_my_function.py
import unittest
from unittest.mock import Mock
from function_app.my_function import main
import azure.functions as func

class TestMyFunction(unittest.TestCase):
    def test_main_name_john(self):
        # Create a mock HTTP request with 'John' in the query parameter
        req = func.HttpRequest(
            method='GET',
            url='/api/MyHttpTriggerFunction',
            headers={},
            params={'name': 'John'},
            route_params={},
            body=None
        )

        # Call the function
        resp = main(req)

        # Assert the response
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_body().decode(), 'Welcome, John!')

if __name__ == '__main__':
    unittest.main()
