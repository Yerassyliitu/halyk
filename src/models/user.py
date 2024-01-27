from sqlalchemy import Column, String, BigInteger

from src.schemas.user import UserRead
from settings.database.database_connection import Base


class User(Base):
    __tablename__ = "User"
    id = Column(BigInteger, primary_key=True)
    email = Column(String, nullable=False, unique=True)

    hashed_password: str = Column(String(length=1024), nullable=False)

    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)

    def to_read_model(self) -> UserRead:
        return UserRead(
            id=self.id,
            email=self.email,
            firstname=self.firstname,
            lastname=self.lastname,
        )



