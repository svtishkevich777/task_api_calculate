import asyncio
import json


async def task_1(session, tasks):

    results = await asyncio.gather(*tasks, return_exceptions=True)
    formatted_results = {}

    for idx, result in enumerate(results, 1):
        formatted_results[idx] = result

    return json.dumps(formatted_results, indent=4, ensure_ascii=False)
