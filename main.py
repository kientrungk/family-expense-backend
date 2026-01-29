from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from datetime import date
from typing import List

from database import SessionLocal
from models import Expense
from schemas import ExpenseCreate, ExpenseOut

app = FastAPI(
    title="Family Expense App",
    version="1.0.0",
)


# ---------- DB dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- Health check ----------
@app.get("/")
def root():
    return {"status": "ok"}


# ---------- Create expense ----------
@app.post("/expense", response_model=ExpenseOut)
def add_expense(
    payload: ExpenseCreate,
    db: Session = Depends(get_db),
):
    expense = Expense(
        amount=payload.amount,
        category_id=payload.category_id,
        note=payload.note,
        spent_at=payload.spent_at,
        user_id=payload.user_id,
    )
    db.add(expense)
    db.commit()
    db.refresh(expense)
    return expense


# ---------- List expenses ----------
@app.get("/expenses", response_model=List[ExpenseOut])
def list_expenses(db: Session = Depends(get_db)):
    return (
        db.query(Expense)
        .order_by(Expense.spent_at.desc())
        .all()
    )
