# coding=utf-8
import random
import sys
import os
c = random.choice(["a", "b", "c"])
print(c)
current_path = os.getcwd()
print(current_path)
current_file = os.path.split(current_path)
print(current_file)
file = os.path.isfile(current_file[1])
file_sys = sys.path
print(file_sys, '-----------------')
print(file)
if not os.path.exists("test"):
    os.mkdir("test")

file = os.path.join(current_path, "test2", "abc.py")
print(file)
print(sys.getdefaultencoding())

def func(a):
    return a % 2 == 0

l = [i for i in range(10)]
f = list(filter(func, l))
print(f)