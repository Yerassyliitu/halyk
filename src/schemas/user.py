from pydantic import EmailStr, BaseModel


class UserRead(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str

    class from_attributes:
        orm_mode = True


class UserRegistration(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    phone_number: str
    password: str
    confirm_password: str

    class from_attributes:
        orm_mode = True


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    phone_number: str
    email: EmailStr
    password: str

    class from_attributes:
        orm_mode = True


class LoginInput(BaseModel):
    email: EmailStr
    password: str

    class from_attributes:
        orm_mode = True


class LoginOutput(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

    class from_attributes:
        orm_mode = True
