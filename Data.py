from functions import prompt
from graph import Graph

filename = prompt()
show_graph = Graph(filename)
show_graph.open_file(filename)

