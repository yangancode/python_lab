# coding: utf-8
# @date: 2020-07-10

"""

"""


class A:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return 'A的名字是{},体重是{}'.format(self.name, self.weight)

    def eat(self):
        print('A.吃')
        pass

    def drink(self):
        print('A.喝')


class B(A):
    # 注意点1： 新加的参数放在后面，不容易弄混
    def __init__(self, name, weight, height):
        self.height = height
        A.__init__(self, name, weight)

    def __str__(self):
        return 'B姓名是{}，体重是{}kg, 身高的{}cm'.format(self.name, self.weight, self.height)

    def sleep(self):
        print('B.睡')

    def eat(self):  # 重写父类A的eat
        print('B.吃')


class C(A):
    def __init__(self, pro):
        self.pro = pro

    # 注意点2: C继承了A，如果没有定义__init__方法，则默认继承A的__init__方法，即拥有它的name和weight属性
    # 但是这里你定义了__init__方法，相当于重写方法，所以不会拥有name和weight参数，所以只需要传入一个pro参数即可
    def __str__(self):
        return 'C的专业是{}'.format(self.pro)

    def eat(self):
        print('C.吃')

    pass


if __name__ == '__main__':
    aa = A("小A", 50)
    print(aa)

    bb = B('小B', 50, 180)
    print(bb)

    cc = C('小C的专业')
    print(cc)


# 如果是多重继承，即有多个父类，则继承是有顺序的，新式类和经典类的顺序不同！
class D(C, B):
    def __init__(self, name, weight, pro, hobby):
        # A.__init__(self, name, weight)
        # C.__init__(self, pro, weight)
        # B.__init__(self.weight, self.pro, self.weight)
        C.__init__(self, weight)
        # super().__init__(name, weight, pro)

        # super是自动找到父类进而调用方法,假设继承了多个父类,那么会按照顺序逐个去找,然后调用
        self.hobby = hobby
        self.name = name

    def __str__(self):
        return 'D的姓名是%s，爱好是%s，体重是%skg，身高:%s, pro:%s' % (self.name, self.hobby, self.weight, self.H, self.pro)


if __name__ == '__main__':
    aa = A("小A", 50)
    print(aa)

    bb = B('小B', 50, 180)
    print(bb)

    cc = C('小C的专业')
    print(cc)

    l = list()
