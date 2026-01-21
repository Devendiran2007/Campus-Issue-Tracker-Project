from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    name: str
    email: str
    password: str = Field(min_length=8, max_length=64)
    role: str = "student"


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    role: str

    class Config:
        orm_mode = True

class LoginRequest(BaseModel):
    email: str
    password: str = Field(min_length=1, max_length=64)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

