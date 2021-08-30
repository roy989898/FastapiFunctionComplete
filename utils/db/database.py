# DB
from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///db_test_3.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
# 仅适用于SQLite。其他数据库不需要。 链接参数：检查同一条线？ 即需要可多线程
# 通过sessionmaker得到一个类，一个能产生session的工厂。
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()  # 数据表的结构用 ORM 的语言描述出来


# DB
def get_db() -> Session:
    db: Optional[Session] = None
    try:
        db = SessionLocal()  # 这时，才真正产生一个'会话'，并且用完要关闭
        yield db  # 调用该函数将返回generator可迭代对象
    finally:
        if db:
            db.close()
        print('DB close')
