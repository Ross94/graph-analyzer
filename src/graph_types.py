import networkx as nx

def load_pajek(path):
	g = nx.DiGraph()
	with open(path, "r") as f:
		for line in f:
			parts = line.split(" ")
			#add node
			if "*" not in line and len(parts) == 2:
				g.add_node(int(parts[0]))
			#add edge
			elif "*" not in line and len(parts) == 3:
				source = int(parts[0])
				target = int(parts[1])
				weight = float(parts[2])
				#update weight of existent edge
				if g.has_edge(source, target): 
					g[source][target]['weight'] += weight
				#new edge
				else:
					g.add_edge(source, target, weight=weight)
	return g


def acessoValori():
	g = nx.MultiDiGraph()
	g.add_node(0)
	g.add_node(1)
	g.add_node(2)
	g.add_edge(0, 1, weight=20.0)
	g.add_edge(0, 1, weight=20.0)
	g.add_edge(0, 1, weight=30.0)
	g.add_edge(0, 2, weight=420.0)
	g.add_edge(1, 2, weight=1000.0)
	print_graph(g)
	elems = g.adj[0].items()
	print elems #all edges with source 0
	#[(1, AtlasView({0: {'weight': 20.0}, 1: {'weight': 20.0}, 2: {'weight': 30.0}})), (2, AtlasView({0: {'weight': 420.0}}))]
	print elems[0] #all edges with source 0 and first target
	#(1, AtlasView({0: {'weight': 20.0}, 1: {'weight': 20.0}, 2: {'weight': 30.0}}))
	print elems[0][0] #first target from source 0 
	#1
	print elems[0][1] #data of edges with target first target
	#{0: {'weight': 20.0}, 1: {'weight': 20.0}, 2: {'weight': 30.0}}
	print elems[0][1][1] #dictionary with data of second edge from source 0 to first target
	#{'weight': 20.0}
	print elems[0][1][1]['weight'] #weight of second edge from source 0 to first target
	#20.0