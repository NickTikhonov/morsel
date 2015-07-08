#Import the library
from morsel.entities import Vector
from morsel.quad_field import Field
from morsel.pathfinder import Pathfinder
import matplotlib.pyplot as plt
import networkx as nx


def print_samples(samples):
    for sample in samples:
        print sample.get_json_string()

sample_field = Field(
    Vector(1, 6),
    Vector(6, 11.1),
    Vector(11.2, 6),
    Vector(6, 1))

#---How to generate stratified random samples inside a field: ---
srs = sample_field.get_stratified_random_samples(10, 1, plt=plt)
Pathfinder.tsp_path(srs)
# G = Pathfinder.get_nn_roadmap(srs, 10)
# pos = nx.spring_layout(G)
# nx.draw_networkx_nodes(G, pos, node_size=7)
# nx.draw_networkx_edges(G, pos, width=2)
# plt.show()
