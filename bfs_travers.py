# Import deque (double-ended queue) from the collections module.
from collections import deque


# Create the graph using an adjacency list.
# Each key is a vertex, and its value is a list of connected vertices.
graph = {
    'A': ['B', 'C'],   
    'B': ['A', 'D'],   
    'C': ['A', 'E'],   
    'D': ['B', 'E'],   
    'E': ['C', 'D']    
}

# start = the vertex from which BFS will begin
def bfs(graph, start):

    # Create an empty set to store vertices that have already
    visited = set()

    # Create an empty queue.
    # BFS follows FIFO: First In, First Out.
    queue = deque()

    # Here, start = 'A', so A becomes visited.
    visited.add(start)


    # Add the starting vertex to the queue.
    # Queue becomes: [A]
    queue.append(start)


    # Continue the loop as long as the queue is not empty.
    while queue:

        # Remove the first vertex from the queue.
        # popleft() removes from the FRONT of the queue.
        vertex = queue.popleft()


        # Print the vertex that we just removed.
        # end=" " keeps the output on the same line.
        print(vertex, end=" ")


        # Get all neighbors of the current vertex
        # and process them one by one.
        for neighbor in graph[vertex]:


            # Check whether this neighbor has already been visited.
            # If it has NOT been visited, enter the if block.
            if neighbor not in visited:


                # Mark the neighbor as visited.
                # This prevents visiting the same vertex again.
                visited.add(neighbor)


                # Add the unvisited neighbor to the queue.
                # It will be processed later.
                queue.append(neighbor)


# Call the BFS function.
# Start the traversal from vertex A.
bfs(graph, 'A')