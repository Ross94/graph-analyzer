import networkx as nx
from collections import defaultdict
from multiprocessing import Lock

import logger

__weighted_completed = 0
__unweighted_completed = 0
__progress_bar_lock = Lock()

def nodes_number(graph):
	'''Compute the number of nodes in graph'''

	nodes_num = graph.number_of_nodes()
	logger.log("Nodes number calculated")
	return nodes_num

def degree_distribution(graph):
	'''
	Compute degree for each node. Group nodes for degree.
	For each degree count number of nodes then calculate percentage of degree. 
	'''

	degrees = defaultdict(list)

	#group nodes for degree
	for key, value in sorted(graph.degree):
		degrees[value].append(key)

	#compute percentage for each degree
	for k, v in degrees.items():
		degrees[k] = len(v) / graph.number_of_nodes() * 100

	deg_distr = dict(degrees)
	logger.log("Degree distribution calculated")
	return deg_distr

def clustering_coefficient(graph):
	'''Compute graph clustering coefficient'''

	clust_coeff = nx.average_clustering(graph, weight='weight')
	logger.log("Clustering coefficient calculated")
	return clust_coeff

def average_path_length(graph, source, weight=None):
	'''Compute average shortest paths form one node to others'''

	total_weight = 0.0
	nodes_number = graph.number_of_nodes()

	for target in graph.nodes:
		if nx.has_path(graph, source, target) and source != target:
			total_weight = total_weight + nx.shortest_path_length(graph, source, target, weight=weight)

	avg_path_len = total_weight /  (nodes_number - 1)

	__progress_bar_lock.acquire()

	if weight != None:
		global __weighted_completed
		__weighted_completed = __weighted_completed + 1
		nodes_computed = __weighted_completed
		weightStr = "weighted "
	else:
		global __unweighted_completed
		__unweighted_completed = __unweighted_completed + 1
		nodes_computed = __unweighted_completed
		weightStr = ""
	
	bar_message = "Average {0}path length".format(weightStr)
	
	logger.progress_bar(bar_message, nodes_computed, nodes_number)
	if nodes_computed == nodes_number:
		logger.log("{0} calculated".format(bar_message))

	__progress_bar_lock.release()

	return avg_path_len
	