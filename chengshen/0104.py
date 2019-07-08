#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: 0104.py
@time: 2019/7/8 17:43
@desc:
'''

import networkx as nx
import matplotlib.pyplot as plt
# erdos renyi graph
# generate a graph which has n=20 nodes, probablity p = 0.2.
ER = nx.random_graphs.erdos_renyi_graph(20, 0.2)
# the shell layout
pos = nx.shell_layout(ER)
nx.draw(ER, pos, with_labels = False, node_size = 30)
plt.show()

