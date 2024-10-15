import asyncio
import json


async def task_2(session, tasks):
    completed_tasks = {}

    for idx, task in enumerate(asyncio.as_completed(tasks), 1):
        result = await task
        completed_tasks[idx] = result

        if len(completed_tasks) == 2:

            for pending_task in tasks:
                if not pending_task.done():
                    pending_task.cancel()
            break

    return json.dumps(completed_tasks[2], indent=4, ensure_ascii=False)
