from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return visited

def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            visited.add(vertex)
            stack.extend(reversed(graph[vertex]))


graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B", "E", "F"],
    "E": ["C", "D", "F", "G"],
    "F": ["D", "E"],
    "G": ["E"]
}

bfs_result = bfs_iterative(graph, 'A')
dfs_result = dfs_iterative(graph, 'A')


bfs_result, dfs_result

