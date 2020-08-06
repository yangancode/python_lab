# coding: utf-8
# @date: 2020-07-14

"""
Mixin 尝试

https://blog.csdn.net/u012814856/article/details/81355935
"""


class Displayer():
    def display(self, message):
        print(message)


class LoggerMixin():
    def log(self, message, filename='logfile.txt'):
        with open(filename, 'a') as fh:
            fh.write(message)

    def display(self, message):
        super().display(message)
        self.log(message)


class MySubClass(LoggerMixin, Displayer):
    def log(self, message):
        super().log(message, filename='subclassing.txt')


subclass = MySubClass()
subclass.display("This string will be shown and logged in subclasslog.txt")
