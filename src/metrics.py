import networkx as nx
from collections import defaultdict

import logger

def nodes_number(graph):
	nodes_num = graph.number_of_nodes()
	logger.log("Nodes number calculated")
	return nodes_num

def degree_distribution(graph):
	degrees = defaultdict(list)

	#group nodes for degree
	for key, value in sorted(nx.degree_centrality(graph).iteritems()):
		degrees[value].append(key)

	#compute percentage for each degree
	for k, v in degrees.iteritems():
		degrees[k] = float(len(v)) / graph.number_of_nodes() * 100

	deg_distr = dict(degrees)
	logger.log("Degree distribution calculated")
	return deg_distr

def clustering_coefficient(graph):
	clust_coeff = nx.average_clustering(graph, weight='weight')
	logger.log("Clustering coefficient calculated")
	return clust_coeff

def average_path_length(graph, weight=None):
	weightStr = "weighted " if weight != None else ""
	total_weight = 0.0
	bar_message = "Average path length " + weightStr

	logger.progress_bar(0, graph.number_of_nodes(), bar_message)
	for s in graph.nodes:
		logger.progress_bar(s, graph.number_of_nodes(), bar_message)

		for t in graph.nodes:
			if nx.has_path(graph, s, t):
				total_weight = total_weight + nx.shortest_path_length(graph, s, t, weight=weight)

	avg_path_len = total_weight / (graph.number_of_nodes() * (graph.number_of_nodes() - 1))

	logger.log("Average " + weightStr + "path length calculated")

	return avg_path_len
	