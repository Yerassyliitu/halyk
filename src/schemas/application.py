from datetime import datetime

from pydantic import BaseModel


class ApplicationRead(BaseModel):
    id: int
    user_id: int
    insurance_sum: int
    total_insurance_premium: int
    main_coverage_premium: int
    ns_premium: int
    disability_premium: int
    tt_premium: int
    created_at: datetime
    class from_attributes:
        orm_mode = True


class ApplicationCreate(BaseModel):
    user_id: int
    insurance_sum: int
    total_insurance_premium: int
    main_coverage_premium: int
    ns_premium: int
    disability_premium: int
    tt_premium: int

    class from_attributes:
        orm_mode = True