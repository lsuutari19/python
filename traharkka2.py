# Python code to perform Dijkstra's algorithm
# in a non-directed graph
import math
from collections import deque

INF = float("inf")

class WeightedEdgeNode:
	def __init__(self,nde,wght=0):
		self.node = nde
		self.weight = wght


class WeightedGraph:

	def __init__(self,nVerts):
		self.nVertices = nVerts
		self.adj_list = {}
		self.vertices = []

		for x in range(1,nVerts+1):
			self.adj_list[x] = []
			self.vertices.append(x)

		self.dist = {}
		for x in range(1,nVerts+1):
			self.dist[x] = INF

		self.pred = {}
		for x in range(1,nVerts+1):
			self.pred[x] = None


def add_edge(g,x,y,wght):	
	g.adj_list[x].append(WeightedEdgeNode(y,wght))
	g.adj_list[y].append(WeightedEdgeNode(x,wght))	


def dijkstra(g,s):

    for i in g.vertices:
        g.dist[i] = INF
        g.pred[i] = 0

    g.dist[s] = 0

    queue = [i for i in g.vertices]

    while len(queue) > 0:
        minval = INF
        u = 0
        for vert in queue:
            if g.dist[vert] < minval:
                minval = g.dist[vert]
                u = vert
        queue.remove(u)

        for edge in g.adj_list[u]:
            v = edge.node
            if g.dist[v] > g.dist[u] + edge.weight:  #tämä pitää muuttaa
                g.dist[v] = g.dist[u] + edge.weight
                g.pred[v] = u


def print_path(g,u):
    if g.pred[u] != 0:
        print_path(g,g.pred[u])
    print(u,":",g.dist[u])


def main():

    data = open("graph1.txt", "r")

    listData = []

    for item in data:
        line = item.split()
        listData.append(line)


    listData.pop(0)
    start, end = listData[0][0], listData[-1][-1]
    listData.pop(-1)

    end = str(end)
    end = end.strip("[]")
    end = end.strip(" ' ")

    g = WeightedGraph(int(end))


    for item in data:
        node_start, node_end, weight = item.split(' ')
        add_edge(g, int(node_start), int(node_end), int(weight))

    dijkstra(g,start)
    print("Path from {} to {}  with cumulative weights:".format(start, end))
    print_path(g,end)

main()

