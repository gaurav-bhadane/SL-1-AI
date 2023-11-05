# Define an undirected graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
#-----------------------DFS---------------------------
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Initialize a set to keep track of visited nodes
visited = set()

# Call DFS starting from the 'A' node (or any other starting node)
print("DFS Traversal:")
dfs(graph, 'A', visited)
#-----------------------BFS---------------------------
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    print()

    print("BFS Traversal:")
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Call BFS starting from the 'A' node (or any other starting node)
bfs(graph, 'A')