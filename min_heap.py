import heapq

heap = []

# Insert elements
heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)
heapq.heappush(heap, 5)

print("Min Heap:", heap)

# Remove minimum element
print("Deleted:", heapq.heappop(heap))

print("After deletion:", heap)