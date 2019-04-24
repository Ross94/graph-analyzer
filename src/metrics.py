import networkx as nx
from collections import defaultdict
import threading

import logger

weighted_completed = 0
unweighted_completed = 0
sem = threading.Semaphore()

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

	sem.acquire()

	if weight != None:
		global weighted_completed
		weighted_completed = weighted_completed + 1
		nodes_computed = weighted_completed
		weightStr = "weighted "
	else:
		global unweighted_completed
		unweighted_completed = unweighted_completed + 1
		nodes_computed = unweighted_completed
		weightStr = ""
	
	bar_message = "Average {0}path length".format(weightStr)
	
	logger.progress_bar(bar_message, nodes_computed, nodes_number)
	if nodes_computed == nodes_number:
		logger.log("{0} calculated".format(bar_message))

	sem.release()

	return avg_path_len
	