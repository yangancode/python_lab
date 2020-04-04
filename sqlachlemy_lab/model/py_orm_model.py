# coding: utf-8
# @date: 2020-04-04

"""

"""
from .base_model import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, text, JSON


class PyOrmModel(Base):
    __tablename__ = 'py_orm'

    id = Column(Integer, autoincrement=True, primary_key=True, comment='唯一id')
    name = Column(String(255), nullable=False, default='', comment='名称')
    attr = Column(JSON, nullable=False, comment='属性')
    ct = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP'), comment='创建时间')
    ut = Column(TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), comment='更新时间')

    @staticmethod
    def fields():
        return ['id', 'name', 'attr']

    @staticmethod
    def to_json(model):
        fields = PyOrmModel.fields()
        json_data = {}
        for field in fields:
            json_data[field] = model.__getattribute__(field)
        return json_data

    @staticmethod
    def from_json(data: dict):
        fields = PyOrmModel.fields()

        model = PyOrmModel()
        for field in fields:
            if field in data:
                model.__setattr__(field, data[field])
        return model
