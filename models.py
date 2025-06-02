from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class QARecord(Base):
    __tablename__ = 'qa_records'
    id = Column(Integer, primary_key=True)
    question = Column(String, unique=True, nullable=False)
    answer = Column(String, nullable=False)
    direction = Column(String, nullable=False)  # "zh2Jp" 或 "Jp2zh"

# 建立資料庫連線（SQLite）
engine = create_engine('sqlite:///qa_records.db')
Base.metadata.create_all(engine)

# 建立 Session
SessionLocal = sessionmaker(bind=engine)

#查詢
def get_answer_from_db(question,direction):
    session = SessionLocal()
    record = session.query(QARecord).filter_by(question=question, direction=direction).first()
    session.close()
    if record:
        return record.answer
    return None

#修改
def save_answer_to_db(question, answer, direction):
    session = SessionLocal()
    # 確認是否已存在
    record = session.query(QARecord).filter(QARecord.question == question).first()
    if not record:
        new_record = QARecord(question=question, answer=answer, direction=direction)
        session.add(new_record)
        session.commit()
    session.close()