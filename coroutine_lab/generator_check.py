# coding: utf-8
# @date: 2020-08-04

"""
可迭代对象、迭代器、生成器

1.凡是可作用于for循环的对象都是Iterable类型；
2.凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
3.集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
4.Python的for循环本质上就是通过不断调用next()函数实现的
"""


def check_iter():
    """判断 可迭代对象、迭代器、生成器"""
    from collections.abc import Iterable, Iterator, Generator
    l = [x for x in range(10)]
    g = (x for x in range(10))
    print(isinstance(l, Iterable))  # True
    print(isinstance(l, Iterator))  # False

    print(isinstance(g, Iterable))  # True
    print(isinstance(g, Iterator))  # True
    print(isinstance(g, Generator))  # True


def iter_element():
    """迭代元素"""
    l = [x for x in range(10)]
    g = (x for x in range(10))

    for sub_l in l:
        print(sub_l)
    # 第二次仍有元素迭代
    for sub_l in l:
        print(sub_l)

    print('--------')
    for sub_g in g:
        print(sub_g)
    # 第二次没元素迭代
    for sub_g in g:
        print(sub_g)


# 创建生成器的第二种方式
def target(N):
    count = 0
    while count < N:
        yield count
        count += 1


if __name__ == '__main__':
    t = target(3)
    print(next(t))
    print(t.send(None))
    print(next(3))
    # print(next(t))
    # print(next(t))


# 注意send发送的值
def jumping_range(N):
    index = 0
    while index < N:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


if __name__ == '__main__':
    itr = jumping_range(5)
    print(itr.send(None))  # 0
    print(itr.send(2))  # 3, 这条语句不能放到位置1, 具体可以自己尝试
    print(next(itr))  # 1
