import asyncio
import json
from utils import get_formatted_results


async def task_3(session, tasks):
    completed_tasks = {}

    for idx, task in enumerate(asyncio.as_completed(tasks), start=1):
        result = await task
        completed_tasks[idx] = result

        if len(completed_tasks) == 3:
            third_result = completed_tasks[3]

            if "Error" in third_result or ('result' in third_result and third_result['result'] > 0):
                if "Error" in third_result:
                    third_msg = "Третий запрос завершился с ошибкой!"
                else:
                    third_msg = "Третий результат положительный!"

                remaining_tasks = tasks[3:]
                remaining_results = await asyncio.gather(*remaining_tasks)

                for i, remaining_result in enumerate(remaining_results, start=4):
                    completed_tasks[i] = remaining_result

                last_two_results = get_formatted_results("Последние два запроса!", completed_tasks, len(completed_tasks) - 1, len(completed_tasks))

                return json.dumps({
                    third_msg: third_result,
                    **json.loads(last_two_results)
                }, indent=4, ensure_ascii=False)

            elif 'result' in third_result and third_result['result'] < 0:
                first_two_results = get_formatted_results("Результат выполнения первых двух!", completed_tasks, 1, 2)

                return json.dumps({
                    "Третий результат отрицательный!": {
                        "3": third_result
                    },
                    **json.loads(first_two_results)
                }, indent=4, ensure_ascii=False)

    for task in tasks:
        if not task.done():
            task.cancel()
