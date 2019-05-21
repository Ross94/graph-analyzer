# Graph Analyzer

This project compute metrics for pajek graph generated from https://github.com/Ross94/ethereum-galaxy-server.  
Metrics calculated:

* Number of Nodes
* Number of Edges
* Tot Degree Distribution
* In Degree Distribution
* Out Degree Distribution
* Clustering coefficient
* Average path length (only main component)
* Average weighted path length (only main component of loaded graph)

Comapare data with random graph for small world property.  

## Getting Started

For use this project simply clone this project, install python 3 and Networkx.


### Installing

Python installation:

Windows:

Go to https://www.python.org/ and download .exe files, then run it.  

Linux:

```
sudo apt-get install python3.7.3
```

Networkx installation:

```
pip3 install networkx==2.3
```

In Windows add --user after networkx version.  

## Running

Get inside src folder and run the command below:

Windows:  

```
py -3 .\main.py graphPath processNum
```

Linux:  

```
python3 main.py -graph=string -result=string -process=int -weight=bool
```

* -graph = path of graph reachable from src. 
* -result = name of file with results.
* -processNum = (OPTIONAL) number of process for better performance, default is 1 (sequential execution) recommended core number. 
* -weight = (OPTIONAL) also compute average path length weighted, default is False, high cost.

## Output

Some notes about format:
* All degrees are key-value structure, the number of pairs can be different.

Example:

```
{
	"loaded_graph": {
		"global": {
			"nodes_number": int, 
			"edges_number": int, 
			"clustering_coefficient": float, 
			"degree_distribution_tot": {
				"degree1": float
			}, 
			"degree_distribution_in": {
				"degree1": float, 
				"degree2": float
			}, 
			"degree_distribution_out": {
				"degree1": float
			}
		}, 
		"main_component": {
			"nodes_number": int, 
			"edges_number": int, 
			"clustering_coefficient": float, 
			"average_path_length": float, 
			"average_weighted_path_length": float, 
			"degree_distribution_tot": {
				"degree1": float,
				"degree2": float
			}, 
			"degree_distribution_in": {
				"degree1": float, 
				"degree2": float
			}, 
			"degree_distribution_out": {
				"degree1": float
			}
		}
	}, 
	"random_graph": {
		"global": {
			"nodes_number": int, 
			"edges_number": int, 
			"clustering_coefficient": float, 
			"degree_distribution_tot": {
				"degree1": float,
				"degree2": float
			}, 
			"degree_distribution_in": {
				"degree1": float, 
				"degree2": float
			}, 
			"degree_distribution_out": {
				"degree1": float,
				"degree2": float,
				"degree3": float
			}
		}, 
		"main_component": {
			"nodes_number": int, 
			"edges_number": int, 
			"clustering_coefficient": float, 
			"average_path_length": float, 
			"degree_distribution_tot": {
				"degree1": float
			}, 
			"degree_distribution_in": {
				"degree1": float, 
				"degree2": float,
				"degree3": float, 
				"degree4": float
			}, 
			"degree_distribution_out": {
				"degree1": float,
				"degree2": float,
				"degree3": float
			}
		}
	}, 
	"small_world": {
		"L": "NaN"/float, 
		"C": "NaN"/float
	}
}
```