
# Kruskal's Algorithm to find Minimum Spanning Tree

vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Edges with their weights, based on the readable labels
edges = [
    ('B', 'E', 2),
    ('A', 'C', 3),
    ('E', 'F', 3),
    ('B', 'C', 4),
    ('E', 'G', 4),
    ('F', 'G', 4),
    ('A', 'B', 5),
    ('C', 'D', 5),
    ('C', 'F', 6),
    ('D', 'F', 6)
]

# Sort edges by increasing weight
edges.sort(key=lambda edge: edge[2])

parent = {v: v for v in vertices}
rank = {v: 0 for v in vertices}


# Find the representative of a component
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


# Merge two components
def union(u, v):
    root_u = find(u)
    root_v = find(v)

    if root_u == root_v:
        return False

    if rank[root_u] < rank[root_v]:
        parent[root_u] = root_v
    elif rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_v] = root_u
        rank[root_u] += 1

    return True


mst = []
total_weight = 0

for u, v, weight in edges:
    # Select only if the edge does not create a cycle
    if union(u, v):
        mst.append((u, v, weight))
        total_weight += weight

    # A spanning tree has V - 1 edges
    if len(mst) == len(vertices) - 1:
        break

print("Edges in Minimum Spanning Tree:")
for u, v, weight in mst:
    print(f"{u} -- {v}: {weight}")

print("Total MST Weight:", total_weight)
