# coding: utf-8
# @date: 2020-07-10

"""
Python 多重继承
"""


# 菱形多重继承
# class A:
#     def say(self):
#         print("A say")
#
#
# class B(A):
#     def say(self):
#         print("B say")
#         A.say(self)
#
#
# class C(A):
#     def say(self):
#         print("C say")
#         A.say(self)
#
#
# class D(B, C):
#     def say(self):
#         print("D say")
#         B.say(self)
#         C.say(self)
#
#
# if __name__ == '__main__':
#     print(D.mro())
#     dd = D()
#     dd.say()


# 解决菱形继承，可使用super方法
class A:
    def say(self):
        print("A say")


class B(A):
    def say(self):
        print("B say")
        super().say()


class C(A):
    def say(self):
        print("C say")
        super().say()


class D(B, C):
    def say(self):
        print("D say")
        super().say()


if __name__ == '__main__':
    print(D.mro())
    dd = D()
    dd.say()
