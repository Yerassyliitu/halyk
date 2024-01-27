from pydantic import EmailStr, BaseModel


class UserRead(BaseModel):
    id: int
    email: EmailStr
    firstname: str
    lastname: str


class UserCreate(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr
    password: str


class LoginInput(BaseModel):
    email: EmailStr
    password: str


class LoginOutput(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


