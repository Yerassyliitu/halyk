from pydantic import BaseModel


class EarthquakePost(BaseModel):
    user_latitude: float
    user_longitude: float
    class Config:
        orm_mode = True