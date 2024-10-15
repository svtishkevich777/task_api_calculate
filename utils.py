import random
import asyncio
import json


async def random_time_sleep() -> None:
    time_sleep = random.uniform(0, 3)
    await asyncio.sleep(time_sleep)


def calculate_in_process(x: int, y: int) -> float:
    random_num = random.randint(-10, 10)
    return round((x / y) * random_num, 2)


def generate_error_response(error_type, message, x, y):
    return {
        "Error": error_type,
        "ErrorMessage": message,
        "RequestData": f"x = {x}; y = {y}"
    }


def get_formatted_results(label, results, start_idx, end_idx):
    formatted_result = {label: {}}

    for idx in range(start_idx, end_idx + 1):
        formatted_result[label][idx] = results[idx]

    return json.dumps(formatted_result, indent=3, ensure_ascii=False)
