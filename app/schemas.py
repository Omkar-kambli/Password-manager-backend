from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# -------- Register --------
class RegisterRequest(BaseModel):
    email: EmailStr
    password: str


class RegisterResponse(BaseModel):
    message: str


# -------- Login --------
class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


# -------- For the vault --------

class VaultEntryCreate(BaseModel):
    encrypted_blob: str  

class VaultEntryUpdate(BaseModel):
    encrypted_blob: Optional[str] = None

class VaultEntryResponse(BaseModel):
    entry_id: int
    user_id: int
    encrypted_blob: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class justresponse(BaseModel):
    message:str        