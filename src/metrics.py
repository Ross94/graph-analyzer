import networkx as nx
from collections import defaultdict
from multiprocessing import Lock, Value

import logger

__completed_unweighted = Value("i", 0)
__completed_weighted = Value("i", 0)
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

	with __progress_bar_lock:
		#need for correct log, one variable generate error with log even if improve code
		if weight != None:
			weightStr = "weighted "
			__completed_weighted.value += 1
			completed = __completed_weighted.value
		else:
			weightStr = ""	
			__completed_unweighted.value += 1
			completed = __completed_unweighted.value
		
		bar_message = "Average {0}path length".format(weightStr)
		
		logger.progress_bar(bar_message, completed, nodes_number)

		if completed == nodes_number:
			logger.log("{0} calculated".format(bar_message))

	return avg_path_len
	