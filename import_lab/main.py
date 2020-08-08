# coding: utf-8
# @date: 2020-04-04

"""

"""
# 1.测试是否需要__init__.py
import module1.test
import sys

if __name__ == '__main__':
    module1.test.hello()
    print(sys.path)


# 2.测试__all__
# from module2 import *
#
# if __name__ == '__main__':
#     test1()
#     test2()


# 3.测试导入路径的缩短
# from module3 import test
# if __name__ == '__main__':
#     test.hello()

# from ma.mb.test import hello
#
# if __name__ == '__main__':
#     hello()


# import ma.mb.sub_ma1
# import module_c
#
# # from module_c.hello3 import hello3_func
#
# print(__name__)
#
# module_c.hello3.hello3_func()
#
# if __name__ == '__main__':
#     pass
