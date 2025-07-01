graf = {
    'A': {'B':4, 'D':9},
    'B': {'A':4, 'C':4, 'D':7},
    'C': {'B':4, 'D':9},
    'D': {'A':9, 'B':7, 'C':9},
}


def dijkstra(graf, start):
    distances = {vertex: float('inf') for vertex in graf}
    points = {vertex: [start] for vertex in graf}
    distances[start] = 0

    visited = set()
    current_vertex = start

    while len(visited) < len(graf):
        shortest_edge = float('inf')
        visited.add(current_vertex)

        for neighbor, weight in graf[current_vertex].items():
            # Mencari Jarak terpendek
            if weight + distances[current_vertex] < distances[neighbor]:
                distances[neighbor] = weight + distances[current_vertex]
                # Mencari Titik yang dilewati dengan append
                points[neighbor] = points[current_vertex] + [neighbor]
            # Mencari Tetangga Terdekat sebagai current_vertex baru
            if neighbor not in visited and weight < shortest_edge:
                shortest_edge = weight
                next = neighbor
        current_vertex = next
    print(visited,'\n', distances,'\n', points)

dijkstra(graf, "A")
