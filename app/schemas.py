from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    confirmer_password: str

class UserLogin(BaseModel):
    username: str
    password: str
    
