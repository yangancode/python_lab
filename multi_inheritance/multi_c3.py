# coding: utf-8
# @date: 2020-07-10

"""
Python 多重继承
"""


# C3-深度优先
# class A:
#     var = 'A var'
#
#
# class B(A):
#     pass
#
#
# class C:
#     var = 'C var'
#
#
# class D(B, C):
#     pass
#
#
# if __name__ == '__main__':
#     print(D.mro())
#     print(D.var)


# C3-广度优先
class A:
    var = 'A var'


class B(A):
    pass


class C(A):
    var = 'C var'


class D(B, C):
    pass


if __name__ == '__main__':
    print(D.mro())
    print(D.var)
