# coding=utf-8
from datetime import datetime
from datetime import timedelta

now = datetime.now()
three_day = timedelta(days=3)
beform_three_day = now - three_day
beform = beform_three_day.strftime("%Y-%m-%d %H:%M:%S")
print(beform)
beform_three_day = datetime.strftime(beform_three_day, "%Y-%m-%d %H:%M:%S")
DATA = datetime.strptime(beform_three_day, "%Y-%m-%d %H:%M:%S")
print(DATA, type(DATA))
print(beform_three_day)
now_time = datetime.strftime(now, "%Y-%d-%m %H:%M:%S")
print(now_time)
info = []


def user(*arg, **kwargs):
    print(arg, kwargs)
    info.append(arg)


tuple1 = ('赵云', '张飞', '关羽')
kwargs = {'name': '项羽', 'skill': '推进', 'hurt': 300}
user(*tuple1, **kwargs)
print(info)

a = 10
b = 2
a, b = b, a
print(a)
print(b)
kwargs = {'name': '项羽', 'skill': '推进', 'hurt': 300}
kwargs['name'] = '关羽'
print(kwargs)

a = 10
b = 100


print(id(a))
print(id(b))
a = b
print(id(a))
print(id(b))

def func(name):
    print(name)


list1 = ['赵云', '张飞', '关羽']
func(list1)


def recusive(n):
    if n == 10:
        return recusive(n) + 1


def f(n):
    if n == 10:
        return 1
    return (f(n+1) +1)*2


print(f(1))
print('-----------------------------------------------------')
# f = lambda i, *args: args
# print(f(1, 2, 3))


def f(*args):
    pass


kwargs = {'i': 22,'n': 'll'}

args = [1, 2, 3, 4, 5]
# f(**kwargs)
f(*args)
# f(args) = f((1,2,3,4,5))
# f(args)
adds = lambda x, y: x+y
print(adds(3, 4))

def func(n):
    return n**2
list1 = [1, 2, 3]
list2 = list(map(func, list1))
print(list2)