from fastapi import FastAPI
from sqladmin import Admin
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from settings.database.database_connection import engine
from src.api.v1.routers import all_routers
from src.models.admin import UserAdmin, ApplicationAdmin

app = FastAPI()
admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(ApplicationAdmin)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def hello():
    return {'Details': 'Add /docs'}


@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})


for router in all_routers:
    app.include_router(router, prefix='/api')



