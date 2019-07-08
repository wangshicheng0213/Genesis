import matplotlib.pyplot as plt
import networkx as nx
# H = nx.path_graph(10)
# G.add_nodes_from(H)
G = nx.Graph()
G.add_cycle([0,1,2,3,4])
G.add_nodes_from([2, 3]) #同时加2和3两个节点
nx.draw(G, with_labels=True)
plt.show()

