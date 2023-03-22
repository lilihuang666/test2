# coding=utf-8
import os

# f = open("11.txt", encoding="utf-8")  # 不写默认为r 只读模式
# r = f.read()
# f.close()  # 使用完文件需要关闭文件
# print(r)

# with open("11.txt", 'r+', encoding="utf-8") as f:  # r+ 可读可写，使用with as 可以不用close文件
#     r = f.read()
#     f.write("\n学习python的第一天")
#     print(r)
abs_path = os.path.abspath("demo1.py")
dir_path = os.path.dirname(abs_path)
print(abs_path)
print(dir_path)
