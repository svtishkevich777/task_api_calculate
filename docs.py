from fastapi import status


calculate_summary = "Выполнение вычисления"
calculate_description = """
Эндпоинт принимает два целых числа `x` и `y`, выполняет вычисление `(x / y) * случайное число` и возвращает результат.

- **x**: Число должно быть не меньше нуля.
- **y**: Число должно быть не равно нулю.
"""

calculate_response_description = "Результат вычисления"

validation_error_response = {
    status.HTTP_422_UNPROCESSABLE_ENTITY: {
        "description": "Ошибки валидации входных данных",
        "content": {
            "application/json": {
                "example": {
                    "Error": "ValidationError",
                    "ErrorMessage": "y должен быть не равен нулю",
                    "RequestData": "x = 1; y = 0"
                }
            }
        }
    }
}

internal_server_error_response = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: {
        "description": "Внутренняя ошибка сервера",
        "content": {
            "application/json": {
                "example": {
                    "Error": "InternalServerError",
                    "ErrorMessage": "Произошла внутренняя ошибка сервера",
                    "RequestData": "x = 1; y = 0"
                }
            }
        }
    }
}

calculate_responses = {
    **validation_error_response,
    **internal_server_error_response,
}

calculate_details = """
### Выполнение вычисления

Эндпоинт принимает два целых числа `x` и `y`, выполняет вычисление `(x / y) * случайное число` и возвращает результат.

- **x**: Число должно быть не меньше нуля.
- **y**: Число должно быть не равно нулю.

#### Пример запроса:

GET /calculate?x=10&y=2

bash
Copy code

#### Пример ответа:
```json
{
  "x": 10,
  "y": 2,
  "result": 5.0
}
"""
