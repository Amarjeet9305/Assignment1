def bellman_ford(vertices, edges, source):
    distance = {v: float('inf') for v in vertices}
    distance[source] = 0

    # Relax all edges V - 1 times
    for _ in range(len(vertices) - 1):
        changed = False

        for u, v, weight in edges:
            if distance[u] != float('inf'):
                new_distance = distance[u] + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    changed = True

        # Stop early if no distance changes
        if not changed:
            break

    # Detect reachable negative-weight cycles
    for u, v, weight in edges:
        if (distance[u] != float('inf')
                and distance[u] + weight < distance[v]):
            return "Negative-weight cycle detected"

    return distance


vertices = ['A', 'B', 'C', 'D']

edges = [
    ('A', 'B', 4),
    ('A', 'C', 5),
    ('B', 'C', -2),
    ('C', 'D', 3)
]

print(bellman_ford(vertices, edges, 'A'))