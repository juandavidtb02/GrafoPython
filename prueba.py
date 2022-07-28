import networkx as nx
import matplotlib.pyplot as plt

d = nx.DiGraph()

d.add_node('A')
d.add_node('B')
d.add_node('C')


d.add_edge('A','B',weight=3)
d.add_edge('B','C',weight=3)
d.add_edge('C','A',weight=3)
d.add_edge('C','C',weight=3)


options = {
    'node_color': 'blue',
    'node_size': 600,
    'width': 2,
    'arrowstyle': '->',
    'arrowsize': 10,
}

pos = nx.circular_layout(d)
nx.draw_networkx(d, pos, with_labels=True, font_weight='bold', font_color='white')
labels = nx.get_edge_attributes(d, 'weight')

nx.draw_networkx_edges(d, pos, arrowsize=10, arrowstyle='->', width=1 )
nx.draw_networkx_nodes(d, pos, node_size=300, node_color='black')
nx.draw_networkx_edge_labels(d, pos, edge_labels=labels)

ax = plt.gca()
plt.axis('off')
ax.margins(0.6)

plt.savefig('grafo.png', transparent=True, bbox_inches='tight', pad_inches=1)