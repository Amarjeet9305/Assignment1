import heapq  # Import heapq to use a min-heap priority queue

# Represent the graph using an adjacency list
# Each neighbour is stored as (vertex, weight)
graph = {
    'A': [('B', 4), ('C', 3)],      
    'B': [('D', 2), ('E', 5)],       
    'C': [('E', 6), ('F', 4)],       
    'D': [('E', 2)],                
    'E': [('F', 1), ('G', 3)],       
    'F': [('G', 2), ('H', 6)],       
    'G': [('H', 2)],                
    'H': []                  
}

def dijkstra(graph, start):
    # Initialize all vertex distances to infinity
    distances = {v: float('inf') for v in graph}

    # Store the previous vertex for path reconstruction
    parent = {v: None for v in graph}
# Distance from start to itself is 0
    distances[start] = 0  
# Insert start vertex with distance 0           
    pq = [(0, start)]                
# Continue while the queue is not empty
    while pq:
        # Get the smallest distance                        
        current_distance, u = heapq.heappop(pq)  

        # Skip this entry if a shorter distance was already found
        if current_distance > distances[u]:
            continue

        # Explore all neighbours of the current vertex
        for v, weight in graph[u]:
            # Calculate the distance through the current vertex
            new_distance = current_distance + weight

            # Relax the edge if a shorter path is found
            if new_distance < distances[v]:
                # Update the shortest distance
                distances[v] = new_distance  
                # Store the previous vertex
                parent[v] = u      
                 # Add updated distance          
                heapq.heappush(pq, (new_distance, v)) 

    return distances, parent     
# Return distances and parent information
def get_path(parent, destination):
    # Create an empty list for the path
    path = []   
     # Start from the destination vertex                   
    current = destination         

    # Trace the path backwards using parent information
    while current is not None:
         # Add the current vertex to the path
        path.append(current)    
        # Move to its previous vertex  
        current = parent[current]  
# Reverse to get start-to-destination order
    return path[::-1]              

# Run Dijkstra's algorithm starting from vertex A
distances, parent = dijkstra(graph, 'A')

# Display the shortest distance and path for every vertex
for vertex in graph:
    path = get_path(parent, vertex)  # Reconstruct the shortest path
    print(
        f"{vertex}: Distance = {distances[vertex]}, "
        f"Path = {' -> '.join(path)}"  # Print the path as a string
    )