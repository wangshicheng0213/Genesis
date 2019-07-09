#!F:PythonWorkSpace
# encoding: utf-8
'''
@author: wangshicheng
@license: Copyright 2018-2010, Facebook.
@contact: icandicefly@163.com
@software: never ,never,never.... give up
@file: shequ2.py
@time: 2019/7/9 21:20
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
def most_important(G):
    """
    returns a copy of G with
    the most important nodes
    according to the pagerank
    """
    ranking = nx.betweenness_centrality(G).items()
    #print ranking
    r = [x[1] for x in ranking]
    m = sum(r)/len(r) # mean centrality
    t = m*10 # threshold, we keep only the nodes with 10 times the mean
    Gt = G.copy()
    for k, v in ranking:
        if v < t:
            Gt.remove_node(k)
    return Gt
Gt = most_important(G) # trimming
# draw the nodes and the edges (all)
nx.draw_networkx_nodes(G,spring_pos,node_color='b',alpha=0.2,node_size=8)
nx.draw_networkx_edges(G,spring_pos,alpha=0.1)
# draw the most important nodes with a different style
nx.draw_networkx_nodes(Gt,spring_pos,node_color='r',alpha=0.4,node_size=254)
# also the labels this time
nx.draw_networkx_labels(Gt,spring_pos,font_size=6,font_color='b')
#
part = community.best_partition(G)
values = [part.get(node) for node in G.nodes()]
nx.draw_networkx(G, pos = spring_pos, cmap = plt.get_cmap('jet'), node_color = values, node_size=30, with_labels=False)
plt.savefig("../output/FB_BC_commu.png", dpi = 300)
#  get modularity
mod = community.modularity(part,G)
print("modularity:", mod)
