import sys
import os

import networkx as nx

import graph_types
import saver
import logger
import metrics
from analyzable_graph import AnalyzableGraph

def analyze_loaded(graph):
	logger.log("Start metrics computing for loaded graph")

	analyzer = AnalyzableGraph(graph)

	#submit metrics tasks
	analyzer.add_metric("nodes_number", metric= metrics.nodes_number, 
		args=(graph, ))
	analyzer.add_metric("edges_number", metric= metrics.edges_number, 
		args=(graph, ))
	analyzer.add_metric("deg_distr_tot", metric=metrics.degree_distribution, 
		args=(graph, "tot", ))
	analyzer.add_metric("deg_distr_in", metric=metrics.degree_distribution, 
		args=(graph, "in", ))
	analyzer.add_metric("deg_distr_out", metric=metrics.degree_distribution, 
		args=(graph, "out", ))
	analyzer.add_metric("clust_coeff", metric=metrics.clustering_coefficient, 
		args=(graph, ))

	#get main component in main process, cannot submit other without result of this
	main_component = metrics.main_component(graph)

	#submit metrics based on main_component
	for node in main_component.nodes:
		analyzer.add_metric("avg_path_len", metric=metrics.average_path_length, 
		args=(main_component, node, ))

	for node in main_component.nodes:
		analyzer.add_metric("avg_wgh_path_len", metric=metrics.average_path_length, 
		args=(main_component, node, "weight", ))

	analyzer.close_pool()

	#get results
	results = analyzer.get_results()
	nodes_number = results["nodes_number"]
	edges_number = results["edges_number"]
	deg_distr_tot = results["deg_distr_tot"]
	deg_distr_in = results["deg_distr_in"]
	deg_distr_out = results["deg_distr_out"]
	clust_coeff = results["clust_coeff"]
		
	avg_path_len = sum(results["avg_path_len"]) / len(results["avg_path_len"])
	avg_wgh_path_len = sum(results["avg_wgh_path_len"]) / len(results["avg_wgh_path_len"])

	logger.log( "Metrics computed for loaded graph")

	return {
		"nodes_number": nodes_number,
		"edges_number": edges_number,
		"clustering_coefficient": clust_coeff,
		"average_path_length": avg_path_len,
		"average_weighted_path_length": avg_wgh_path_len,
		"degree_distribution_tot": deg_distr_tot,
		"degree_distribution_in": deg_distr_in,
		"degree_distribution_out": deg_distr_out,
	}

def analyze_random(nodes_number, edges_number):
	logger.log("Start metrics computing for random graph")

	graph = nx.gnm_random_graph(nodes_number, edges_number, directed=True)
	analyzer = AnalyzableGraph(graph)

	#submit tasks
	analyzer.add_metric("nodes_number", metric= metrics.nodes_number, 
		args=(graph, ))
	analyzer.add_metric("edges_number", metric= metrics.edges_number, 
		args=(graph, ))
	analyzer.add_metric("deg_distr_tot", metric=metrics.degree_distribution, 
		args=(graph, "tot", ))
	analyzer.add_metric("deg_distr_in", metric=metrics.degree_distribution, 
		args=(graph, "in", ))
	analyzer.add_metric("deg_distr_out", metric=metrics.degree_distribution, 
		args=(graph, "out", ))
	analyzer.add_metric("clust_coeff", metric=metrics.clustering_coefficient, 
		args=(graph, ))

	main_component = metrics.main_component(graph)

	#submit metrics based on main_component
	for node in main_component.nodes:
		analyzer.add_metric("avg_path_len", metric=metrics.average_path_length, 
		args=(main_component, node, ))

	analyzer.close_pool()

	#get results
	results = analyzer.get_results()
	nodes_number = results["nodes_number"]
	edges_number = results["edges_number"]
	deg_distr_tot = results["deg_distr_tot"]
	deg_distr_in = results["deg_distr_in"]
	deg_distr_out = results["deg_distr_out"]
	clust_coeff = results["clust_coeff"]
	avg_path_len = sum(results["avg_path_len"]) / len(results["avg_path_len"])

	logger.log( "Metrics computed for random graph")

	return {
		"nodes_number": nodes_number,
		"edges_number": edges_number,
		"clustering_coefficient": clust_coeff,
		"average_path_length": avg_path_len,
		"degree_distribution_tot": deg_distr_tot,
		"degree_distribution_in": deg_distr_in,
		"degree_distribution_out": deg_distr_out,
	}

def main():

	#parse params
	if len(sys.argv) < 3:
		print("Missing params specify arguments in this order:\n"
		"graphPath resultFilename processNumber\n"
		"graphPath => path of graph from src folder\n"
		"resultFilename => name of file with results\n"
		"processNumber => optional, improve performance best value is number of core")
	else:
		GRAPH_PATH = sys.argv[1]
		OUTPUT_NAME = sys.argv[2]
		PROCESSES_NUMBER = int(sys.argv[3]) if len(sys.argv) >= 4 else 1

		if not os.path.exists(GRAPH_PATH):
			print("File {0} does not exist, please check your path".format(GRAPH_PATH))
			sys.exit(1)

		logger.config_logger(OUTPUT_NAME)
		
		#load file
		logger.log("Start loading graph")
		loaded_graph = graph_types.load_pajek(GRAPH_PATH)
		logger.log("Terminated graph loading")
		
		if len(loaded_graph.edges) != 0:

			loaded_metrics = analyze_loaded(loaded_graph)
			random_metrics = analyze_random(nodes_number=loaded_graph.number_of_nodes(), 
				edges_number=loaded_graph.number_of_edges())

			small_world = {}
			small_world["L"] = ("NaN" if random_metrics["average_path_length"] == 0 
				else loaded_metrics["average_path_length"] / random_metrics["average_path_length"])
			small_world["C"] = ("NaN" if random_metrics["clustering_coefficient"] == 0 
				else loaded_metrics["clustering_coefficient"] / random_metrics["clustering_coefficient"])

			results = {}
			results["loaded_graph"] = loaded_metrics
			results["random_graph"] = random_metrics
			results["small_world"] = small_world

			logger.log("Start saving metrics")
			saver.save_json_file(results, OUTPUT_NAME)
			logger.log("Metrics saved")
		else:
			logger.log("Empty graph, no metrics calculated")

if __name__ == "__main__":
	main()