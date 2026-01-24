from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime

from app.database import get_db
from app.models import VaultEntry
from app.schemas import (
    VaultEntryCreate,
    VaultEntryUpdate,
    VaultEntryResponse
)
from app.auth import get_current_user

router = APIRouter(prefix="/vault", tags=["Vault"])


@router.post("/entries", response_model=VaultEntryResponse)
def create_entry(
    request: VaultEntryCreate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    entry = VaultEntry(
        user_id=current_user["user_id"],
        encrypted_blob=request.encrypted_blob
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


@router.get("/entries", response_model=List[VaultEntryResponse])
def get_entries(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    return (
        db.query(VaultEntry)
        .filter(
            VaultEntry.user_id == current_user["user_id"]
            )
        .all()
    )


@router.put("/entries/{entry_id}", response_model=VaultEntryResponse)
def update_entry(
    entry_id: int,
    request: VaultEntryUpdate,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    entry = (
        db.query(VaultEntry)
        .filter(
            VaultEntry.entry_id == entry_id,
            VaultEntry.user_id == current_user["user_id"]
        )
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    entry.encrypted_blob = request.encrypted_blob
    entry.updated_at = datetime.utcnow()

    db.commit()
    db.refresh(entry)
    return entry


@router.delete("/entries/{entry_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_entry(
    entry_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    entry = (
        db.query(VaultEntry)
        .filter(
            VaultEntry.entry_id == entry_id,
            VaultEntry.user_id == current_user["user_id"]
        )
        .first()
    )
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    db.delete(entry)
    db.commit()



