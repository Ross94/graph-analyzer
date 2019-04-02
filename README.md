# Graph Analyzer

This project compute metrics for pajek graph generated from https://github.com/Ross94/ethereum-galaxy-server. 
Metrics calculated:

* Number of Nodes
* Degree Distribution
* Clustering coefficient
* Average path length

## Getting Started

For use this project simply clone this project and install Networkx.


### Installing

Networkx installation:

```
pip install networkx==2.2
```

## Running

Get inside src folder and run the command below:

```
python main.py graphPath processNum
```

* graphPath  = path of graph reachable from src 
* processNum = number of process for better performance, default is 1 (sequential execution) recommended core number.  