from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app.models import VaultEntry
from app.schemas import VaultEntryCreate, VaultEntryResponse
from app.auth import get_current_user


router = APIRouter(prefix="/sync", tags=["Synchronization"])

@router.get("/status")
def sync_push(entry:list[VaultEntryResponse] , db: Session = Depends(get_db) , current_user:dict=Depends(get_current_user)):
    return(
        db.query(VaultEntryCreate).filter(
            VaultEntryCreate.user_id == current_user["user_id"]
    ).all()
    )

@router.post("/push")
def sync_push(
    entries: List[VaultEntryCreate],
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    # Delete old vault data
    db.query(VaultEntry).filter(
        VaultEntry.user_id == current_user["user_id"]
    ).delete()

    # Insert new vault data
    for entry in entries:
        db.add(
            VaultEntry(
                user_id=current_user["user_id"],
                encrypted_blob=entry.encrypted_blob,
                updated_at=datetime.utcnow()
            )
        )

    db.commit()
    return {"message": "Vault synced successfully"}
