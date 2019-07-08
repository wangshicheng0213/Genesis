import matplotlib.pyplot as plt
import networkx as nx

#顺序是不能变化的
G=nx.Graph()

H = nx.path_graph(20)      #定义了图形的点
# G.add_nodes_from(H)
# nx.draw(G, with_labels=True)

#导入所有边，每条边分别用tuple表示
G.add_edges_from([(1,2),(1,3),(2,4),(2,5),(3,6),(4,8),(5,8),(3,7),(4,8),(5,9),(6,10),(6,11),(6,12),(6,13),(6,14),(6,15),(6,16),(6,17)],)
nx.draw(G, with_labels=True, edge_color='b', node_color='g', node_size=1000)
plt.show()
#plt.savefig('./generated_image.png') 如果你想保存图片，去除这句的注释
