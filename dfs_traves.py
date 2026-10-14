graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

def dfs(graph, start):

    visited = set()
    stack = [start]

    while stack:

        vertex = stack.pop()

        if vertex not in visited:

            visited.add(vertex)

            print(vertex, end=" ")

            for neighbor in reversed(graph[vertex]):

                if neighbor not in visited:
                    stack.append(neighbor)


dfs(graph, 'A')