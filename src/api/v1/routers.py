from src.api.v1.auth import auth_router
from src.api.v1.earthquake import earthquake_router

all_routers = [
    auth_router,
    earthquake_router,
]