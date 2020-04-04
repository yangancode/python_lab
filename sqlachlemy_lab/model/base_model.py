# coding: utf-8
# @date: 2020-04-04

"""

"""
from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, scoped_session

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/orm_test?charset=utf8mb4", echo=True)


def _get_session():
    """获取session"""
    return scoped_session(sessionmaker(bind=engine, expire_on_commit=False))()


@contextmanager
def db_session(commit=True):
    session = _get_session()
    try:
        yield session
        if commit:
            session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        if session:
            session.close()

