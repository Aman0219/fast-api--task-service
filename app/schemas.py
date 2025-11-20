from pydantic import BaseModel

# Shared attributes
class UserBase(BaseModel):
    name: str
    email: str

# For creating a user (request body)
class UserCreate(UserBase):
    password: str

# For returning a user (response model)
class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True
