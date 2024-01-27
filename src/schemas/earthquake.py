from pydantic import BaseModel


class EarthquakePost(BaseModel):
    user_latitude: float
    user_longitude: float
    class from_attributes:
        orm_mode = True