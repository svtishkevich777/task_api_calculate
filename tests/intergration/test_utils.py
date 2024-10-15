import unittest
from unittest.mock import patch
import json

from utils import calculate_in_process, get_formatted_results, generate_error_response


class TestCalculationFunctions(unittest.TestCase):

    @patch('random.randint', return_value=5)
    def test_calculate_in_process(self, mock_randint):
        x = 10
        y = 2

        result = calculate_in_process(x, y)
        expected_result = round((x / y) * 5, 2)

        self.assertEqual(result, expected_result)


    def test_generate_error_response(self):
        error_type = "ValidationError"
        message = "Value error, x не может быть меньше нуля!"
        x = -1
        y = 1

        response = generate_error_response(error_type, message, x, y)

        expected_response = {
            "Error": error_type,
            "ErrorMessage": message,
            "RequestData": "x = -1; y = 1"
        }

        self.assertEqual(response, expected_response)


    def get_formatted_results(label, results, start_idx, end_idx):
        formatted_result = {label: {}}

        for idx in range(start_idx, end_idx + 1):
            formatted_result[label][idx] = results[idx]

        return json.dumps(formatted_result, indent=3, ensure_ascii=False)


    def test_get_formatted_results(self):
        label = "Третий результат отрицательный!"
        results = {
            1: {
                "Error": "Ошибка в запросе",
                "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
                "RequestData": "x = 1.3; y = 2"
            },
            2: {
                "Error": "Ошибка в запросе",
                "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
                "RequestData": "x = w; y = -4"
            },
            3: {
                "x": 1,
                "y": 10,
                "result": -0.9
            }
        }

        formatted_result = get_formatted_results(label, results, 1, 3)

        expected_result = json.dumps({
            "Третий результат отрицательный!": {
                1: {
                    "Error": "Ошибка в запросе",
                    "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
                    "RequestData": "x = 1.3; y = 2"
                },
                2: {
                    "Error": "Ошибка в запросе",
                    "ErrorMessage": "Input should be a valid integer, unable to parse string as an integer",
                    "RequestData": "x = w; y = -4"
                },
                3: {
                    "x": 1,
                    "y": 10,
                    "result": -0.9
                }
            }
        }, indent=3, ensure_ascii=False)

        self.assertEqual(formatted_result, expected_result)


if __name__ == "__main__":
    unittest.main()
