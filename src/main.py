import sys
from multiprocessing import Pool

import graph_types
import printer
import saver
import logger
import metrics

def main():
	#load file
	GRAPH_PATH = sys.argv[1]
	PROCESSES_NUMBER = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

	logger.log("Start loading graph")

	g = graph_types.load_pajek(GRAPH_PATH)

	logger.log("Terminated graph loading")
	logger.log("Start metrics computing")
	#printer.print_graph(g)

	if len(g.edges) != 0:
		pool = Pool(processes=PROCESSES_NUMBER)

		#submit metrics tasks
		node_number = pool.apply_async(func=metrics.nodes_number, args=(g, ))
		deg_distr_tot = pool.apply_async(func=metrics.degree_distribution, args=(g, "tot", ))
		deg_distr_in = pool.apply_async(func=metrics.degree_distribution, args=(g, "in", ))
		deg_distr_out = pool.apply_async(func=metrics.degree_distribution, args=(g, "out", ))
		clust_coeff = pool.apply_async(func=metrics.clustering_coefficient, args=(g, ))

		#get main component in main process, cannot submit other without result of this
		main_component = metrics.main_component(g)

		#submit metrics based on main_component
		avg_path_len = []
		avg_wgh_path_len = []

		for node in main_component.nodes:
			avg_path_len.append(pool.apply_async(func=metrics.average_path_length, args=(main_component, node, )))

		for node in main_component.nodes:
			avg_wgh_path_len.append(pool.apply_async(func=metrics.average_path_length, args=(main_component, node, "weight", )))

		#cannot submit other tasks
		pool.close()
		#wait results
		pool.join()

		#get results
		nodes_number = node_number.get()
		deg_distr_tot = deg_distr_tot.get()
		deg_distr_in = deg_distr_in.get()
		deg_distr_out = deg_distr_out.get()
		clust_coeff = clust_coeff.get()
		
		avg_path_len = [r.get() for r in avg_path_len]
		avg_path_len = sum(avg_path_len) / len(avg_path_len)

		avg_wgh_path_len = [r.get() for r in avg_wgh_path_len]
		avg_wgh_path_len = sum(avg_wgh_path_len) / len(avg_wgh_path_len)

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