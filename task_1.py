import networkx as nx
import matplotlib.pyplot as plt

# Створення графу
G = nx.Graph()

# Додавання вершин і ребер. Кожна вершина - це транспортний вузол, ребро - дорога між вузлами.
edges = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E"), ("D", "F"), ("E", "F"), ("E", "G")]
G.add_edges_from(edges)

# Візуалізація графу
plt.figure(figsize=(10, 7))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='k', linewidths=1, font_size=15, )
plt.title("Модель транспортної мережі маленького міста")
plt.show()

# Аналіз основних характеристик графу
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
average_degree = sum(dict(G.degree()).values()) / num_nodes

num_nodes, num_edges, average_degree

