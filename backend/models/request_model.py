from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    id: int
    email: str

class AnalyzeRequest(BaseModel):
    language: Optional[str] = None
    code: Optional[str] = None
    user: UserModel 
