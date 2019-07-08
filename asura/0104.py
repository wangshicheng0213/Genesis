from matplotlib import use
# use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import networkx as nx
M=nx.MultiGraph()
df = pd.read_csv("relation_weight_sam.csv")
# from_pandas_edgelist



G = nx.from_pandas_edgelist(df,
                              'node1',
                              'node2',

                               edge_attr='weight'
                              )

G.add_node(1)
G.add_node('first_node')
#这里用一个对象多为key来唯一区别一个点
#我们还能够用一个列表来批量加入点
G.add_nodes_from([1,2,3])
#还可以用一个图对象作为点，嵌入到其他图中
# G.add_node(D) #这里D作为一个点的key
# #或者把一个图的所有点赋予另一个图
# G.add_nodes_from(D) #这里返回D的所有点，赋予G
#与加入相同的传递方法，我们也可以删除点
G.remove_node(1)
G.remove_nodes_from([1,2,3])

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

plt.show()

plt.savefig("net_weight3.png")

# 前十行数据，weight是通过"numpy.random.rand()"模拟的。
