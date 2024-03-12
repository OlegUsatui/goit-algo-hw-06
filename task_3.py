def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances

edges = [
    ("A", "B", 1), ("A", "C", 2), ("B", "C", 3), ("B", "D", 4),
    ("C", "E", 5), ("D", "E", 6), ("D", "F", 7), ("E", "F", 8), ("E", "G", 9)
]

# Трансформація у словник словників
graph = {}
for edge in edges:
    a, b, weight = edge
    if a not in graph:
        graph[a] = {}
    if b not in graph:
        graph[b] = {}
    graph[a][b] = weight
    graph[b][a] = weight

# Виконання алгоритму для визначення найкоротших шляхів від вершини 'E'
start_vertex = 'E'
distances = dijkstra(graph, start_vertex)
print(f"Найкоротші шляхи від вершини {start_vertex}: {distances}")