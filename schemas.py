from pydantic import BaseModel, field_validator, Field


class ErrorResponse(BaseModel):
    Error: str
    ErrorMessage: str
    RequestData: str


class ZeroFieldValidator(BaseModel):
    x: int = Field(..., description="x не может быть меньше нуля!")
    y: int = Field(..., description="y не может быть равен нулю!")

    @field_validator('x')
    def validate_x(cls, value):
        if value <= 0:
            raise ValueError("x не может быть меньше нуля!")
        return value

    @field_validator('y')
    def validate_y(cls, value):
        if value == 0:
            raise ValueError("y не может быть равен нулю!")
        return value


class CalculationResponse(BaseModel):
    x: int
    y: int
    result: float
