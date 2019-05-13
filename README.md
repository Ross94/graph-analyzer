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
python3 main.py graphPath processNum
```

* graphPath  = path of graph reachable from src 
* processNum = number of process for better performance, default is 1 (sequential execution) recommended core number. 