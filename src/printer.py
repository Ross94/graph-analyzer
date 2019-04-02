def print_graph(graph):
	print "Nodes (%d):" % graph.number_of_nodes()
	for n in graph.nodes:
		print n

	print "Edges (%d):" % graph.number_of_edges()
	for s, t in graph.edges:
		print s, t, graph.edges[s, t]['weight']