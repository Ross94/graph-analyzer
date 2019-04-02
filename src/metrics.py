import networkx as nx
from collections import defaultdict

def nodes_number(graph):
	return graph.number_of_nodes()

def degree_distribution(graph):
	degrees = defaultdict(list)

	#group nodes for degree
	for key, value in sorted(nx.degree_centrality(graph).iteritems()):
		degrees[value].append(key)

	#compute percentage for each degree
	for k, v in degrees.iteritems():
		degrees[k] = float(len(v)) / graph.number_of_nodes() * 100

	return dict(degrees) 

def clustering_coefficient(graph):
	return nx.average_clustering(graph, weight='weight')

def average_path_length(graph):
	return nx.average_shortest_path_length(graph, weight='weight')