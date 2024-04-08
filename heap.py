import heapq

heap = [5,1,23,54]

heapq.heapify(heap)
heapq.heappush(heap,60)
heapq.heappush(heap,30)
print(heap)
heapq.heapify(heap)
heapq.heappop(heap)
print(heap)


 
