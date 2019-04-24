import networkx as nx

def load_pajek(path):
	'''
	Load pajek file with format:
	*Vertices x
	1 ...
	2 ...
	*arcs
	1 2 ...
	3 4 ...
	'''
	
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