from fastapi import APIRouter, HTTPException

from src.schemas.earthquake import EarthquakePost

from src.helper_functions.earthquake import fetch_earthquakes

earthquake_router = APIRouter(prefix="/v1/earthquake", tags=["earthquake"])


@earthquake_router.post(
    "/",
    status_code=200,
)
async def get_earthquakes(
        geolocation: EarthquakePost,
):
    longitude = geolocation.user_longitude
    latitude = geolocation.user_latitude
    earthquakes = await fetch_earthquakes(latitude, longitude, 3000, 500)
    if earthquakes:
        return earthquakes
    else:
        raise HTTPException(status_code=404, detail="Землетрясений не найдено")