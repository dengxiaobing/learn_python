# 序列
# 在 Python 中，序列类型包括字符串、列表、元组、集合和字典，这些序列支持一些通用的操作，但比较特殊的是，集合和字典不支持索引、切片、相加和相乘操作。
"""
1. 针对序列的内置函数
"""
# `list(sub)` 把一个可迭代对象转换为列表。
""" 例子 """
print()
a = list()
print(a)  # []

b = 'I Love LsgoGroup'
b = list(b)
print(b)
# ['I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p']

c = (1, 1, 2, 3, 5, 8)
c = list(c)
print(c)  # [1, 1, 2, 3, 5, 8]

# `tuple(sub)` 把一个可迭代对象转换为元组。
""" 例子 """
print()
a = tuple()
print(a)  # ()

b = 'I Love LsgoGroup'
b = tuple(b)
print(b)
# ('I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p')

c = [1, 1, 2, 3, 5, 8]
c = tuple(c)
print(c)  # (1, 1, 2, 3, 5, 8)

# `str(obj)` 把obj对象转换为字符串
""" 例子 """
print()
a = 123
a = str(a)
print(a)  # 123

# - `len(s)` 返回对象（字符、列表、元组等）长度或元素个数。
#     - `s` -- 对象。
""" 例子 """
print()
a = list()
print(len(a))  # 0

b = ('I', ' ', 'L', 'o', 'v', 'e', ' ', 'L', 's', 'g', 'o', 'G', 'r', 'o', 'u', 'p')
print(len(b))  # 16

c = 'I Love LsgoGroup'
print(len(c))  # 16

# - `max(sub)`返回序列或者参数集合中的最大值
""" 例子 """
print()
print(max(1, 2, 3, 4, 5))  # 5
print(max([-8, 99, 3, 7, 83]))  # 99
print(max('IloveLsgoGroup'))  # v

# - `min(sub)`返回序列或参数集合中的最小值
""" 例子 """
print()
print(min(1, 2, 3, 4, 5))  # 1
print(min([-8, 99, 3, 7, 83]))  # -8
print(min('IloveLsgoGroup'))  # G

# - `sum(iterable[, start=0])` 返回序列`iterable`与可选参数`start`的总和。
""" 例子 """
print()
print(sum([1, 3, 5, 7, 9]))  # 25
print(sum([1, 3, 5, 7, 9], 10))  # 35
print(sum((1, 3, 5, 7, 9)))  # 25
print(sum((1, 3, 5, 7, 9), 20))  # 45

# - `sorted(iterable, key=None, reverse=False) ` 对所有可迭代的对象进行排序操作。
#     - `iterable` -- 可迭代对象。
#     - `key` -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
#     - `reverse` -- 排序规则，`reverse = True` 降序 ， `reverse = False` 升序（默认）。
#     - 返回重新排序的列表。
""" 例子 """
print()
x = [-8, 99, 3, 7, 83]
print(sorted(x))  # [-8, 3, 7, 83, 99]
print(sorted(x, reverse=True))  # [99, 83, 7, 3, -8]

t = ({"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"})
x = sorted(t, key=lambda a: a["age"])
print(x)
# [{'age': 10, 'name': 'c'}, {'age': 20, 'name': 'a'}, {'age': 25, 'name': 'b'}]


# - `reversed(seq)` 函数返回一个反转的迭代器。
#     - `seq` -- 要转换的序列，可以是 tuple, string, list 或 range。
""" 例子 """
print()
s = 'lsgogroup'
x = reversed(s)
print(type(x))  # <class 'reversed'>
print(x)  # <reversed object at 0x000002507E8EC2C8>
print(list(x))
# ['p', 'u', 'o', 'r', 'g', 'o', 'g', 's', 'l']

t = ('l', 's', 'g', 'o', 'g', 'r', 'o', 'u', 'p')
print(list(reversed(t)))
# ['p', 'u', 'o', 'r', 'g', 'o', 'g', 's', 'l']

r = range(5, 9)
print(list(reversed(r)))
# [8, 7, 6, 5]

x = [-8, 99, 3, 7, 83]
print(list(reversed(x)))
# [83, 7, 3, 99, -8]

# - `enumerate(sequence, [start=0])`
""" [例子]用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。"""
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
a = list(enumerate(seasons))
print(a)
# [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

b = list(enumerate(seasons, 1))
print(b)
# [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

for i, element in a:
    print('{0},{1}'.format(i, element))
# 0,Spring
# 1,Summer
# 2,Fall
# 3,Winter

# - `zip(iter1 [,iter2 [...]])`
#     - 用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。
#     - 我们可以使用 `list()` 转换来输出列表。
#     - 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 `*` 号操作符，可以将元组解压为列表。
""" 例子 """
print()
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]

zipped = zip(a, b)
print(zipped)  # <zip object at 0x000000C5D89EDD88>
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]
zipped = zip(a, c)
print(list(zipped))  # [(1, 4), (2, 5), (3, 6)]

a1, a2 = zip(*zip(a, b))
print(list(a1))  # [1, 2, 3]
print(list(a2))  # [4, 5, 6]