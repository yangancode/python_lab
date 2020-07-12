# coding: utf-8
# @date: 2020-07-11

"""
普通继承
"""


# class A:
#     def __init__(self, a1, a2):
#         self.a1 = a1
#         self.a2 = a2
#
#     def say(self):
#         print("A say, a1: %s, a2: %s" % (self.a1, self.a2))
#
#
# class B(A):
#     def say(self):
#         print("B say, a1: %s, a2: %s" % (self.a1, self.a2))
#
#
# if __name__ == '__main__':
#     # 因为B继承了A的init方法，所以也要传入 a1，a2参数
#     bb = B("10", "100")
#     bb.say()


# class A:
#     def __init__(self, a1, a2):
#         self.a1 = a1
#         self.a2 = a2
#
#     def say(self):
#         print("A say, a1: %s, a2: %s" % (self.a1, self.a2))
#
#
# class B(A):
#     def __init__(self, b1):
#         self.b1 = b1
#
#     def say(self):
#         print("B say, b1: %s" % self.b1)
#
#
# if __name__ == '__main__':
#     # 此处B重写了A的init方法，所以只需要传入b1参数，也没有拥有a1，a2属性
#     bb = B("10")
#     bb.say()


class A:
    def __init__(self, a1, a2):
        self.a1 = a1
        self.a2 = a2

    def say(self):
        print("A say, a1: %s, a2: %s" % (self.a1, self.a2))


class B(A):
    def __init__(self, b1, a1, a2):
        # 第一种写法: Python2的写法
        # super(B, self).__init__(a1, a2)
        # 第二种写法（推荐）：Python3的写法，与第一种等价
        super().__init__(a1, a2)
        # 第三种写法：与前两种等价，不过这种需要显示调用基类，而第二种不用
        # A.__init__(self, a1, a2)
        self.b1 = b1

    def say(self):
        print("B say, a1: %s, a2: %s, b1: %s" % (self.a1, self.a2, self.b1))


if __name__ == '__main__':
    # 此处B重写了A的init方法，所以只需要传入b1参数，也没有拥有a1，a2属性
    bb = B("10", "100", "1000")
    bb.say()
