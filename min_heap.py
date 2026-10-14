import heapq

heap = []

# Insert a element

heapq.heappush(heap, 30)
heapq.heappush(heap,10)
heapq.heappush(heap,20)
heapq.heappush(heap,5)

print(heap)

# Find peek element

print("Minimum element", heap[0])

# Delete minimum element

print("Delete minimum element", heapq.heappop(heap))
heap.remove(10)

# Final min heap tree after deletion
print("After deletion element", heap)