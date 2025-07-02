from pydantic import BaseModel
from typing import Optional

class UserModel(BaseModel):
    id: int
    email: str

class AnalyzeRequest(BaseModel):
    code: Optional[str] = None
    file_path: Optional[str] = None
    user: UserModel
