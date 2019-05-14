# Graph Analyzer

This project compute metrics for pajek graph generated from https://github.com/Ross94/ethereum-galaxy-server.  
Metrics calculated:

* Number of Nodes
* Number of Edges
* Tot Degree Distribution
* In Degree Distribution
* Out Degree Distribution
* Clustering coefficient
* Average path length
* Average weighted path length

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
python3 main.py graphPath resultFilename processNum
```

* graphPath  = path of graph reachable from src 
* resultFilename  = name of file with results
* processNum = (OPTIONAL) number of process for better performance, default is 1 (sequential execution) recommended core number. 

##Output

Some notes about format:
* small_world - L  => float or string "NaN"
* small_world - C  => float or string "NaN"
* All degrees are key-value structure, the number of pairs can be different.

Example:

```
{
	"loaded_graph": {
		"nodes_number": 9, 
		"edges_number": 7, 
		"clustering_coefficient": 0.007735981389354631, 
		"average_path_length": 0.25, 
		"average_weighted_path_length": 37.833333333333336, 
		"degree_distribution_tot": {
			"2": 33.33333333333333, 
			"1": 55.55555555555556, 
			"3": 11.11111111111111
			}, 
			"degree_distribution_in": {
				"1": 44.44444444444444, 
				"0": 44.44444444444444, 
				"3": 11.11111111111111
			}, 
			"degree_distribution_out": {
				"1": 77.77777777777779, 
				"0": 22.22222222222222
			}
		}, 
		"random_graph": {
			"nodes_number": 9, 
			"edges_number": 7, 
			"clustering_coefficient": 0.0,
			 "average_path_length": 1.8571428571428572, 
			 "degree_distribution_tot": {
			 	"3": 33.33333333333333, 
			 	"2": 11.11111111111111, 
			 	"0": 22.22222222222222, 
			 	"1": 33.33333333333333
			 }, 
			 "degree_distribution_in": {
			 	"2": 33.33333333333333, 
			 	"0": 55.55555555555556, 
			 	"1": 11.11111111111111
			 }, 
			 "degree_distribution_out": {
			 	"1": 44.44444444444444, 
			 	"0": 44.44444444444444, 
			 	"3": 11.11111111111111
			 }
		}, 
		"small_world": {
			"L": 0.1346153846153846, 
			"C": "NaN"
		}
	}
}
```