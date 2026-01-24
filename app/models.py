from sqlalchemy import Column, Integer, String, DateTime, ForeignKey,LargeBinary,Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    password_verifier = Column(String, nullable=False) 
    salt = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    vault_entries = relationship(
        "VaultEntry",
        back_populates="user",
        cascade="all, delete"
    )

    devices = relationship(
        "Device",
        back_populates="user",
        cascade="all, delete"
    )


class VaultEntry(Base):
    __tablename__ = "vault_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    
    encrypted_blob = Column(Text, nullable=False) 

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="vault_entries")




class Device(Base):
    __tablename__ = "devices"

    device_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

    device_name = Column(String, nullable=False)
    last_sync_time = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="devices")
