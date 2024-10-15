import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from main import app


client = TestClient(app=app)


class TestCalculationAPI(unittest.TestCase):

    @patch('utils.calculate_in_process')
    @patch('utils.random_time_sleep')
    @patch('multiprocessing.Pool')
    def test_calculate_success(self, mock_pool, mock_random_sleep, mock_calculate):

        mock_random_sleep.return_value = None
        mock_calculate.return_value = -0.7

        mock_pool_instance = MagicMock()
        mock_pool.return_value = mock_pool_instance
        mock_pool_instance.__enter__.return_value = mock_pool_instance
        mock_pool_instance.apply.return_value = -0.7

        response = client.get("/calculate?x=5&y=3")

        self.assertEqual(response.status_code, 200)

        expected_response = {
            "x": 5,
            "y": 3,
            "result": -0.7
        }

        self.assertEqual(response.json(), expected_response)

        mock_pool_instance.apply.assert_called_once_with(mock.ANY, args=(5, 3))


if __name__ == "__main__":
    unittest.main()
