from fastapi import APIRouter

from src.helper_functions.parse_selenium import parse_selenium_and_bs4
from src.schemas.calculator import CalculatorPost

calculator_router = APIRouter(prefix="/v1/calculator", tags=["calculator"])


@calculator_router.post(
    "/",
    status_code=200,
)
async def get_calculator_result(
        calculator: CalculatorPost,
):
    result = parse_selenium_and_bs4(calculator.field1, calculator.field2, calculator.field3, calculator.field4,
                                    calculator.field5, calculator.field6, calculator.field7, calculator.field8)
    return result
