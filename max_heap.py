import heapq

heap = []

# Insert elements
heapq.heappush(heap, -30)
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
heapq.heappush(heap, -5)

print("Max Heap:", [-x for x in heap])

# Remove maximum element
deleted = heapq.heappop(heap)

print("Deleted:", -deleted)
print("After deletion:", [-x for x in heap])