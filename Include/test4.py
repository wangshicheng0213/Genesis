#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: test4.py
@time: 2019/7/4 20:04
@desc:
'''
#输出文件的全部内容
# import csv
#
# with open('0101.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     rows= [row for row in reader]
#
#     print(rows)


#问题分析：因为此csv文件是一个文本文件，并非二进制文件。
#有趣的代码实验
import csv
with open('0101.csv','rt') as csvfile:
    reader = csv.reader(csvfile)
    # next(reader, None)
    column = [row[2] for row in reader]
print(column)