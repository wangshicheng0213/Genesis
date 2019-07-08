#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: 0101.py
@time: 2019/7/7 10:27
@desc:
'''

#有向图和无向图是可以相互转化的，分别用到Graph.to_undirected() 和 Graph.to_directed()两个方法。

import networkx as nx
import matplotlib.pyplot as plt

#建立一个空的无向图G
G=nx.DiGraph()

# #添加一个节点1
# G.add_node(1)
# G.add_node(2,3)
#
# #添加一条边2-3（隐含着添加了两个节点2、3）
# G.add_edge(2,3)
#
# #对于无向图，边3-2与边2-3被认为是一条边
# G.add_edge(3,2)
#
# #输出全部的节点： [1, 2, 3]
print (G.nodes())

#输出全部的边：[(2, 3)]
print (G.edges())


#输出边的数量：1
print (G.number_of_edges())
#输出点数
print (G.number_of_nodes())

# 添加0-1、1-2和2-3三条边，权重分别是3.0和7.5
G.add_weighted_edges_from([(0,1,3.0),(1,2,7.5),(2,3,1.0)])
# 如果想读取权重，可以使用get_edge_data方法，它接受两个参数u和v，即边的起始点。
print (G.get_edge_data(1,2))
# 选出边的权重超过一个阈值的边
estrong = [(u,v) for (u,v,d) in G.edges(data=True) if d["weight"] > 3.0]

print (estrong) # [(1, 2)]

nx.draw(G, with_labels=True)
plt.show()



