from src.models.application import Application
from src.models.user import User
from src.repositories.repository import SQLAlchemyRepository


class UserRepository(SQLAlchemyRepository):
    model = User


class ApplicationRepository(SQLAlchemyRepository):
    model = Application