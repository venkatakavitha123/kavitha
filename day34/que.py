import heapq
priorq = []
heapq.heappush(priorq,5)
print(priorq)
heapq.heappush(priorq,3)
print(priorq)
heapq.heappush(priorq,8)
print(priorq)
heapq.heappush(priorq,0)
print(priorq)
heapq.heappush(priorq,1)
print(priorq)
heapq.heappop(priorq)
while priorq:
    print(priorq[0])
    break