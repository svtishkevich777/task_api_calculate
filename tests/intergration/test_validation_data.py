import unittest
from fastapi.testclient import TestClient
from main import app


client = TestClient(app=app)


class TestFieldValidatorAPI(unittest.TestCase):


    def test_x_less_than_zero(self):
        response = client.get("/calculate?x=-1&y=1")

        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Value error, x не может быть меньше нуля!",
            "RequestData": "x = -1; y = 1"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_y_equals_zero(self):
        response = client.get("/calculate?x=2&y=0")

        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Value error, y не может быть равен нулю!",
            "RequestData": "x = 2; y = 0"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_x_cannot_be_string(self):
        response = client.get("/calculate?x=hhh&y=5")

        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
            "RequestData": "x = hhh; y = 5"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_y_cannot_be_string(self):
        response = client.get("/calculate?x=2&y=hi man")

        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
            "RequestData": "x = 2; y = hi man"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_mixed_x_zero_and_y_string(self):
        response = client.get("/calculate?x=-1&y=hi man")

        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Value error, x не может быть меньше нуля!; Input should be a valid integer, unable to parse string as an integer",
            "RequestData": "x = -1; y = hi man"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_when_not_x(self):
        response = client.get("/calculate?y=3")
        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Field required",
            "RequestData": "x = None; y = 3"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


    def test_when_not_y(self):
        response = client.get("/calculate?x=5")
        self.assertEqual(response.status_code, 422)

        expected_error = {
            "Error": "ValidationError",
            "ErrorMessage": "Field required",
            "RequestData": "x = 5; y = None"
        }

        error_response = response.json()

        self.assertEqual(error_response["Error"], expected_error["Error"])
        self.assertEqual(error_response["ErrorMessage"], expected_error["ErrorMessage"])
        self.assertEqual(error_response["RequestData"], expected_error["RequestData"])


if __name__ == "__main__":
    unittest.main()
