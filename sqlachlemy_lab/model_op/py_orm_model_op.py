# coding: utf-8
# @date: 2020-04-04

"""

"""

from sqlachlemy_lab.model import db_session
from sqlachlemy_lab.model import PyOrmModel


class PyOrmModelOp:
    def __init__(self):
        pass

    @staticmethod
    def save_data(data: dict):
        with db_session() as session:
            model = PyOrmModel.from_json(data)
            session.add(model)

    @staticmethod
    def query_data(pid: int):
        data_list = []
        with db_session(commit=False) as session:
            data = session.query(PyOrmModel).filter(PyOrmModel.id == pid)
            for d in data:
                data_list.append(PyOrmModel.to_json(d))

            return data_list
