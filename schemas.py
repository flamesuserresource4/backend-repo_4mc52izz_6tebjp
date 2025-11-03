"""
Database Schemas for Cashflow App

Each Pydantic model represents a collection in MongoDB.
The collection name is the lowercase of the class name.

Examples:
- User -> "user"
- Cashflow -> "cashflow"
"""

from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    email: EmailStr = Field(..., description="Email address (unique)")
    password_hash: str = Field(..., description="BCrypt hashed password")
    name: Optional[str] = Field(None, description="Full name")
    is_active: bool = Field(True, description="Whether user is active")


class Cashflow(BaseModel):
    """
    Cashflow entries schema
    Collection name: "cashflow"
    """
    user_id: str = Field(..., description="ID of the user who created the entry")
    amount: float = Field(..., description="Transaction amount (positive for income, negative for expense)")
    reason: str = Field(..., description="Spending reason / description")
