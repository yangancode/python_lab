# coding: utf-8
# @date: 2020-04-04

"""

"""

from sqlachlemy_lab import Base, engine
from sqlachlemy_lab.model_op import PyOrmModelOp


if __name__ == '__main__':
    # Base.metadata.create_all(engine)
    # PyOrmModelOp.save_data({'id': 1, 'name': 'test', 'attr': {}})

    data = PyOrmModelOp.query_data(pid=1)
    print(data)
