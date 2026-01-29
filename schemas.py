from pydantic import BaseModel
from datetime import date
from typing import Optional


class ExpenseCreate(BaseModel):
    amount: int
    category_id: int
    note: Optional[str] = None
    spent_at: date
    user_id: str


class ExpenseOut(ExpenseCreate):
    id: str

    class Config:
        orm_mode = True
