#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: test1.py
@time: 2019/7/4 15:22
@desc:
'''


import networkx as nx                   #导入networkx包
import matplotlib.pyplot as plt     #导入绘图包matplotlib（需要安装，方法见第一篇笔记）
G =nx.random_graphs.barabasi_albert_graph(100,1)   #生成一个BA无标度网络G
nx.draw(G)                          #绘制网络G
plt.savefig("ba.png")           #输出方式1: 将图像存为一个png格式的图片文件
plt.show()                            #输出方式2: 在窗口中显示这幅图像

