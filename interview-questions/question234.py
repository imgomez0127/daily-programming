from functools import reduce
def find_lowest_node(traversed):
    for i in range(len(traversed)):
        if not traversed[i]:
            return i
def shares_adjacency(node_set):
     
def reverse_prims(graph):
    traversed = [False for _ in len(graph)]
    node_set = [[0 for _ in range(len(graph))] for _ in len(graph)]
    while(not reduce(lambda x,y: x and y, traversed)):
        cur_node = find_lowest_node(traversed)
        for i,weight in enumerate(graph[cur_node]):
             
