from fastapi import APIRouter

from src.helper_functions.all_calculators.calc_1 import calc_1
from src.schemas.calculator import CalculatorPost

calculator_router = APIRouter(prefix="/v1/calculator", tags=["calculator"])


@calculator_router.post(
    "/",
    status_code=200,
)
async def get_calculator_result(calculator: CalculatorPost):
    result = calc_1(**calculator.dict())
    return result