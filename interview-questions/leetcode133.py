"""
    Graph looks like this
    
    1 ---- 2
    |      |
    |      |
    4 ---- 3
    
    beats 95%+ sometimes cuz leetcode runtime is iffy
"""
class Node(object):
    def __init__(self, val, neighbors=[]):
        self.val = val
        self.neighbors = neighbors
class Solution:
    def dfs(self,node,visited):
        visited[node.val] = Node(node.val,[])
        for neighbor in node.neighbors:
            if neighbor.val not in visited:
                visited[node.val].neighbors.append(self.dfs(neighbor,visited))
            else:
                visited[node.val].neighbors.append(visited[neighbor.val])
        return visited[node.val]
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        return self.dfs(node,visited)

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node1.neighbors = [node2,node4]
node2.neighbors = [node1,node3]
node3.neighbors = [node2,node4]
node4.neighbors = [node1,node3]
copiedGraph = Solution().cloneGraph(node1)
print("Memory locations of originals:")
print(node1.neighbors)
print(node2.neighbors)
print(node3.neighbors)
print(node4.neighbors)
print("Memory location of copies:")
print(copiedGraph.neighbors)
print(copiedGraph.neighbors[0].neighbors)
print(copiedGraph.neighbors[0].neighbors[1].neighbors)
print(copiedGraph.neighbors[1].neighbors)
