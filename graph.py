import csv
from functions import graph_values
from functions import plot_graph


class Graph:
    """Class that graphs file data"""
    def __init__(self, filename):
        self.filename = filename

    def open_file(self, filename):
        """Create a graph form file data"""

        with open(filename) as f:
            reader = csv.reader(f)

            dates, highs, lows = [], [], []
            graph_values(reader, dates, highs, lows)
            plot_graph(dates, highs, lows)
