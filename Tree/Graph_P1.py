graf = {
    'A': ['B', 'D'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['A', 'B', 'C'],
}

graf_jembatan = {
    '1': ['2', '3', '4', '5', '6'],
    '2': ['1', '3', '4', '5', '6'],
    '3': ['1', '2', '4', '5', '6', '7'],
    '4': ['1', '2', '3','7'],
    '5': ['1', '2', '3', '6', '7'],
    '6': ['1', '2', '3', '5', '7'],
    '7': ['3', '4', '5', '6'],
}

def dfs(graph, start, visited = None):
    if visited == None:
        visited = set()
    visited.add(start)
    print(start)

    if(len(visited) <  len(list(graph))):
        for next in graph[start]:
            if next not in visited:
                dfs(graph, next, visited)
    else:
        return visited

# dfs(graf, 'C')
dfs(graf_jembatan, '4')