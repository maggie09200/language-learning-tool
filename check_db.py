# check_db.py
from sqlalchemy.orm import Session
from models import engine, QARecord

# 建立 Session
session = Session(bind=engine)

# 查詢所有資料
all_records = session.query(QARecord).all()

for record in all_records:
    print(f"ID: {record.id}, 問題: {record.question}, 答案: {record.answer}, 方向: {record.direction}")

session.close()