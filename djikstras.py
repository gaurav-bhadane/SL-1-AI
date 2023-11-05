import sys
def min_dist(dist, visited):  # finding minimum dist
    minimum = sys.maxsize
    ind = -1
    for k in range(6):
        if not visited[k] and dist[k] <= minimum:
            minimum = dist[k]
            ind = k
    return ind
def greedy_dijkstra(graph, src):
    dist = [sys.maxsize] * 6
    visited = [False] * 6
    dist[src] = 0  # Source vertex dist is set 0
    for _ in range(6):
        m = min_dist(dist, visited)
        visited[m] = True
        for k in range(6):
            #  updating the dist of neighbouring vertex
            if not visited[k] and graph[m][k] and dist[m] != sys.maxsize and dist[m] + graph[m][k] < dist[k]:
                dist[k] = dist[m] + graph[m][k]
    print("Vertex\t\tdist from source vertex")
    for k in range(6):
        str_val = chr(65 + k)  # Convert index to corresponding character
        print(str_val, "\t\t\t", dist[k])
# Main code
graph = [
    [0, 1, 2, 0, 0, 0],
    [1, 0, 0, 5, 1, 0],
    [2, 0, 0, 2, 3, 0],
    [0, 5, 2, 0, 2, 2],
    [0, 1, 3, 2, 0, 1],
    [0, 0, 0, 2, 1, 0]
]
greedy_dijkstra(graph, 0)