def print_graph(graph):
	'''Print all graph nodes and edges'''
	
	print("Nodes ({0}):".format(graph.number_of_nodes()))
	for n in graph.nodes:
		print(n)

	print("Edges ({0}):".format(graph.number_of_edges()))
	for s, t in graph.edges:
		print(s, t, graph.edges[s, t]['weight'])