class Graph(object):
	
	def __init__(self,graph_dict=None):
		if graph_dict == None:
			graph_dict = {}
		self.__graph_dict = graph_dict
		print self.__graph_dict
	def get_vertices(self):
		return list(self.__graph_dict.keys())

	def get_edges(self):
		edges = []
		for vertex in self.__graph_dict:
			for neighbour in self.__graph_dict[vertex]:
				edges.append({neighbour,vertex})
		return edges

	def add_vertex(self,vertex):
		if vertex not in self.__graph_dict:
			self.__graph_dict[vertex] = []

	def add_edge(self, edge):
		(vertex1, vertex2) = tuple(edge)
		self.__graph_dict[vertex1].append(vertex2)

	def __str__(self):
		ver = "vertices: "
		for v in self.__graph_dict:
			ver += str(v) + " "
		ver += "\nedges: "
		for e in self.get_edges():
			ver += str(e) + " "
		return ver
	def print_graph(self):
		print self.__graph_dict

if __name__ == "__main__":
	g = { 'a': ['d','a'],
		  'b': ['c']

	}

	graph = Graph(g)

	print str(graph.get_vertices())
	print graph.get_edges()
	graph.add_vertex('z')
	graph.add_edge(('a','z'))
	print str(graph.get_vertices())
	print graph.get_edges()
	graph.print_graph()
	print graph