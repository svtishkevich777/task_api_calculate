import asyncio
import aiohttp
import os
from dotenv import find_dotenv, load_dotenv

from utils import generate_error_response
from task_1 import task_1
from task_2 import task_2
from task_3 import task_3


find_dotenv()
load_dotenv()

URL_HOST = os.getenv('URL_HOST', 'localhost')
URL_PORT = os.getenv('URL_PORT', '8000')


async def fetch_result(session, x, y):
    url = f"http://{URL_HOST}:{URL_PORT}/calculate?x={x}&y={y}"
    try:
        async with session.get(url) as response:
            if response.status == 200:
                result = await response.json()
                return result
            else:
                error = await response.json()
                return generate_error_response("Ошибка в запросе", error.get("ErrorMessage", "Произошла ошибка!"), x, y)
    except aiohttp.ClientError as e:
        return generate_error_response("ClientError", f"{e}", x, y)
    except Exception as e:
        return generate_error_response("GeneralError", f"{e}", x, y)


async def execute_task(session, task_num, tasks):
    if task_num == 1:
        result = await task_1(session, tasks)
    elif task_num == 2:
        result = await task_2(session, tasks)
    else:
        result = await task_3(session, tasks)

    return result


async def main():
    async with aiohttp.ClientSession() as session:
        while True:
            print("\nВыберите задачу для выполнения:")
            print("1 - Выполнить task_1 (печать результатов запросов по порядку.)")
            print("2 - Выполнить task_2 (печать второго выполненного запроса и отмена остальных.)")
            print("3 - Выполнить task_3 (обработка третьего завершившегося запроса.)")
            print("0 - Выйти.")

            user_input = input("Введите номер задачи (или 0 для выхода.): ")

            if user_input == "0":
                print("Завершение программы.")
                break
            elif user_input in {"1", "2", "3"}:
                task_num = int(user_input)

                tasks = [
                    asyncio.create_task(fetch_result(session, 1, 0)),
                    asyncio.create_task(fetch_result(session, 0, -34)),
                    asyncio.create_task(fetch_result(session, 20, "ggg")),
                    asyncio.create_task(fetch_result(session, 15.8, 2)),
                    asyncio.create_task(fetch_result(session, 5, -4)),
                ]

                result = await execute_task(session, task_num, tasks)
                print(f"Результат задачи {task_num}: {result}")
            else:
                print("Неверный ввод, попробуйте снова.")


if __name__ == "__main__":
    asyncio.run(main())
