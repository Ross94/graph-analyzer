import networkx as nx
from collections import defaultdict

import logger

def nodes_number(graph):
	ret = graph.number_of_nodes()
	logger.log("Nodes number calculated")
	return ret

def degree_distribution(graph):
	degrees = defaultdict(list)

	#group nodes for degree
	for key, value in sorted(nx.degree_centrality(graph).iteritems()):
		degrees[value].append(key)

	#compute percentage for each degree
	for k, v in degrees.iteritems():
		degrees[k] = float(len(v)) / graph.number_of_nodes() * 100

	ret = dict(degrees)
	logger.log("Degree distribution calculated")
	return ret

def clustering_coefficient(graph):
	ret = nx.average_clustering(graph, weight='weight')
	logger.log("Clustering coefficient calculated")
	return ret

def average_path_length(graph):
	ret = nx.average_shortest_path_length(graph)
	logger.log("Average path length calculated")
	return ret

def average_weighted_path_length(graph):
	ret = nx.average_shortest_path_length(graph, weight='weight')
	logger.log("Average weighted path length calculated")
	return ret