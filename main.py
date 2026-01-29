from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Expense
from datetime import date

app = FastAPI(title="Family Expense App")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/expense")
def add_expense(
    amount: int,
    category_id: int,
    note: str,
    spent_at: date,
    user_id: str,
    db: Session = Depends(get_db)
):
    e = Expense(
        amount=amount,
        category_id=category_id,
        note=note,
        spent_at=spent_at,
        user_id=user_id
    )
    db.add(e)
    db.commit()
    return {"status": "ok"}

@app.get("/expenses")
def list_expenses(db: Session = Depends(get_db)):
    return db.query(Expense).order_by(Expense.spent_at.desc()).all()
