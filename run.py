from code.data_prep import GraphModel
import networkx as nx
from networkx.algorithms import approximation as apxa

graphObject = GraphModel("data")
G = graphObject.finalGraphModel()

print(nx.average_neighbor_degree(G))