# Graph Analyzer

This project compute metrics for pajek graph generated from https://github.com/Ross94/ethereum-galaxy-server.  
Metrics calculated:

* Number of Nodes
* Degree Distribution
* Clustering coefficient
* Average path length
* Average weighted path length

## Getting Started

For use this project simply clone this project, install python 2.7 and Networkx.


### Installing

Python installation:

Windows:

Go to https://www.python.org/ and download .exe files, then run it.  

Linux:

```
sudo apt-get install python 2.7
```

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