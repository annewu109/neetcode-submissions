"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        def dfs(curr):
            if curr in visited:
                return visited[curr]
            visited[curr] = Node(curr.val)
            neighborsCopy = []
            for neighbor in curr.neighbors:
                neighborsCopy.append(dfs(neighbor))
            visited[curr].neighbors = neighborsCopy
            return visited[curr]

        return dfs(node) if node else None

