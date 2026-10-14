import heapq

def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []
    total_cost = 0

    while min_heap and len(visited) < len(graph):
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, weight))
            total_cost += weight

        for neighbor, edge_weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap, (edge_weight, neighbor, node)
                )

    if len(visited) != len(graph):
        return None, None

    return mst, total_cost


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5), ('E', 6)],
    'D': [('B', 4), ('C', 5), ('E', 2)],
    'E': [('C', 6), ('D', 2)]
}

mst, cost = prim(graph, 'A')

print("MST edges:", mst)
print("Minimum cost:", cost)