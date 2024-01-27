from pydantic import BaseModel


class CalculatorPost(BaseModel):
    field1: str
    field2: str
    field3: str
    field4: str
    field5: str
    field6: str
    field7: str
    field8: str
    class Config:
        orm_mode = True