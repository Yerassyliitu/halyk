from pydantic import BaseModel


class CalculatorPost(BaseModel):
    date_of_birth: str
    gender: str
    insurance_coverage_duration_years: str
    premium_payment_period_years: str
    premium_payment_frequency: str
    tt_insurance_sum: str
    total_insurance_sum: str
    insurance_premium: str

    class from_attributes:
        orm_mode = True