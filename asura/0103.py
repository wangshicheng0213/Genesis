from matplotlib import use
use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
df = pd.read_csv("relation_weight_sam.csv")
# from_pandas_edgelist
# from_pandas_edgelist
G = nx.from_pandas_edgelist(df,
                              'node1',
                              'node2',
                               edge_attr='weight'
                              )
# saves the positions of the nodes on the visualization
# In detail positions is a dictionary where each node is
# a key and the value is a position on the graph
# {'Fam38a_predicted': array([ 0.52246857,  0.4412573 ], dtype=float32),...}
positions = nx.spring_layout(G)
# pass positions and set hold=True
nx.draw(G, pos=positions, hold=True, with_labels=False, node_size=30)
weights = [w[2]['weight']*5 for w in  G.edges(data=True)]
#width can be array of floats
nx.draw_networkx_edges(G, pos=positions, width=weights)
plt.savefig("net_weight.png")
# 前十行数据，weight是通过"numpy.random.rand()"模拟的。
