#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: shequ.py
@time: 2019/7/9 21:18
@desc:
'''
import networkx as nx
import matplotlib.pyplot as plt
import community
import pandas as pd
import sys
# Exploratory Data Analysis
# data
df = pd.read_csv("facebook_combined.csv")
#node1 = list(df["node1"])
G = nx.from_pandas_edgelist(df,
                              'node1',
                              'node2',
                               #edge_attr='weight',
                               #create_using=nx.MultiGraph()
                              )
#Quick snapshot of the Network
print (nx.info(G))
#Create network layout for visualizations
spring_pos = nx.spring_layout(G)
plt.axis("off")
#
part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]
nx.draw_spring(G, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.savefig("FB_commu.png", dpi = 300)
#  get modularity
mod = community.modularity(part,G)
print("modularity:", mod)
