import heapq
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
items = list(map(int, input().split()))

graph = [[] for _ in range(N+1)]
for _ in range(R):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost)) 
    graph[v].append((u, cost))

totals = [0]

for k in range(1, N+1):
    dist = [float('inf')] * (N+1)
    dist[k] = 0

    heap = [(0, k)]
    while heap:
        current_cost, u = heapq.heappop(heap)
        
        if current_cost > dist[u]:
            continue
        
        for v, w in graph[u]:
            new_cost = current_cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
    
    total_items = 0
    for i in range(1, N+1):
        if dist[i] <= M:
            total_items += items[i-1]
    
    totals.append(total_items)
    
print(max(totals))