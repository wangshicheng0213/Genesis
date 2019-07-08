#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: 0103.py
@time: 2019/7/8 17:27
@desc:
'''

import networkx as nx
import matplotlib.pyplot as plt
# regular graphy
# generate a regular graph which has 20 nodes & each node has 3 neghbour nodes.
RG = nx.random_graphs.random_regular_graph(3, 50)
# the spectral layout
pos = nx.spectral_layout(RG)
# draw the regular graphy
nx.draw(RG, pos, with_labels = False, node_size = 30)
plt.show()

