from fastapi import FastAPI, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import multiprocessing

from schemas import ZeroFieldValidator, CalculationResponse, ErrorResponse
from utils import random_time_sleep, calculate_in_process
from docs import (
    calculate_summary,
    calculate_description,
    calculate_response_description,
    calculate_responses,
)


app = FastAPI(
    title="Calculator API",
    description="API для выполнения вычислений с валидацией входных данных.",
    version="v1",
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        field = error.get('loc')[-1]
        message = error.get('msg')
        errors.append({"field": field, "message": message})

    query_params = request.query_params
    x = query_params.get('x')
    y = query_params.get('y')

    error_response = ErrorResponse(
        Error="ValidationError",
        ErrorMessage="; ".join([error['message'] for error in errors]),
        RequestData=f"x = {x}; y = {y}"
    )

    return JSONResponse(content=error_response.model_dump(), status_code=422)


@app.get(
    "/calculate",
    response_model=CalculationResponse,
    summary=calculate_summary,
    description=calculate_description,
    response_description=calculate_response_description,
    responses=calculate_responses,
)

async def calculate(data: ZeroFieldValidator = Query(...)) -> CalculationResponse:
    with multiprocessing.Pool(processes=1) as pool:

        await random_time_sleep()
        result = pool.apply(calculate_in_process, args=(data.x, data.y))

        return CalculationResponse(x=data.x, y=data.y, result=result)
