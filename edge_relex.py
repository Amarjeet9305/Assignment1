distance = {
    'A': 0,
    'B': 4,
    'C': 10
}

# Relax edge B -> C with weight 2
u = 'B'
v = 'C'
weight = 2

if distance[u] + weight < distance[v]:
    distance[v] = distance[u] + weight

print(distance)