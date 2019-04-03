import sys
from multiprocessing.pool import ThreadPool

import graph_types
import printer 
import metrics 
import saver
import logger

def main():
    #load file
    GRAPH_PATH = sys.argv[1]
    PROCESSES_NUMBER = int(sys.argv[2]) if len(sys.argv) >= 3 else 1

    pool = ThreadPool(processes=PROCESSES_NUMBER)

    logger.log("Start loading graph")

    g = graph_types.load_pajek(GRAPH_PATH)

    logger.log("Terminated graph loading")
    logger.log("Start metrics computing")
    #printer.print_graph(g)

	#submit metrics tasks
    node_number_task = pool.apply_async(metrics.nodes_number, (g,))
    deg_distr_task = pool.apply_async(metrics.degree_distribution, (g,))
    clust_coeff_task = pool.apply_async(metrics.clustering_coefficient, (g,))
    avg_path_len_task = pool.apply_async(metrics.average_path_length, (g,))

    #cannot submit other tasks
    pool.close()
    #wait results
    pool.join()

    logger.log( "Metrics calculated")

    #get results
    nodes_num = node_number_task.get()
    deg_distr = deg_distr_task.get()
    clust_coeff = clust_coeff_task.get()
    avg_path_len = avg_path_len_task.get()

    logger.log("Start saving graph")

    #save result
    results = {
        "nodes_number": nodes_num,
        "clustering_coefficient": clust_coeff,
        "average_path_length": avg_path_len,
        "degree_distribution": deg_distr,
    }
    saver.save_json_file(results)
    logger.log("Data saved")

if __name__ == "__main__":
	main()