import sys

import graph_types
import printer
import saver
import logger
import metrics

from analyzable_graph import AnalyzableGraph

def main():
	#load file
	GRAPH_PATH = sys.argv[1]
	PROCESSES_NUMBER = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

	logger.log("Start loading graph")
	loaded_graph = graph_types.load_pajek(GRAPH_PATH)
	logger.log("Terminated graph loading")
	#printer.print_graph(g)

	logger.log("Start metrics computing")
	
	if len(loaded_graph.edges) != 0:

		loaded_analyzer = AnalyzableGraph(loaded_graph)

		#submit metrics tasks
		loaded_analyzer.add_metric("nodes_number", metrics.nodes_number, (loaded_graph, ))
		loaded_analyzer.add_metric("deg_distr_tot", metrics.degree_distribution, (loaded_graph, "tot", ))
		loaded_analyzer.add_metric("deg_distr_in", metrics.degree_distribution, (loaded_graph, "in", ))
		loaded_analyzer.add_metric("deg_distr_out", metrics.degree_distribution, (loaded_graph, "out", ))
		loaded_analyzer.add_metric("clust_coeff", metrics.clustering_coefficient, (loaded_graph, ))

		#get main component in main process, cannot submit other without result of this
		main_component = metrics.main_component(loaded_graph)

		#submit metrics based on main_component
		for node in main_component.nodes:
			loaded_analyzer.add_metric("avg_path_len", metrics.average_path_length, (main_component, node, ))

		for node in main_component.nodes:
			loaded_analyzer.add_metric("avg_wgh_path_len", metrics.average_path_length, (main_component, node, "weight", ))

		loaded_analyzer.close_pool()
		
		#get results
		results = loaded_analyzer.get_results()
		nodes_number = results["nodes_number"]
		deg_distr_tot = results["deg_distr_tot"]
		deg_distr_in = results["deg_distr_in"]
		deg_distr_out = results["deg_distr_out"]
		clust_coeff = results["clust_coeff"]
		
		avg_path_len = sum(results["avg_path_len"]) / len(results["avg_path_len"])
		avg_wgh_path_len = sum(results["avg_wgh_path_len"]) / len(results["avg_wgh_path_len"])

		logger.log( "Metrics calculated")

		logger.log("Start saving metrics")

        #save result
		results = {
			"nodes_number": nodes_number,
			"clustering_coefficient": clust_coeff,
			"average_path_length": avg_path_len,
			"average_weighted_path_length": avg_wgh_path_len,
			"degree_distribution_tot": deg_distr_tot,
			"degree_distribution_in": deg_distr_in,
			"degree_distribution_out": deg_distr_out,
		}
		saver.save_json_file(results)
		logger.log("Metrics saved")
	else:
		logger.log("Empty graph, no metrics calculated")

if __name__ == "__main__":
	main()