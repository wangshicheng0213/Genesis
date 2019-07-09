#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: 0105.py
@time: 2019/7/8 17:43
@desc:
'''
"""
2.2 ER随机图
ER随机图是早期研究得比较多的一类“复杂”网络，
模型的基本思想是以概率p连接N个节点中的每一对节点。
用random_graphs.erdos_renyi_graph(n,p)方法生成一个含有n个节点、
以概率p连接的ER随机图：
"""

import networkx as nx
import matplotlib.pyplot as plt
# erdos renyi graph
# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels = False, node_size = 30)
plt.show()