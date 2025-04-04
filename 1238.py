import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost)) 

end = x
min_cost = [ 0 ] * (n+1)

for i in range(1, n+1):
    start = i
    if start == end:
        min_cost[start] = 0
        continue
    
    dist = [float('inf')] * (n+1)
    dist[start] = 0

    heap = [(0, start)]
    while heap:
        current_cost, u = heapq.heappop(heap)
        
        if current_cost > dist[u]:
            continue
        
        for v, w in graph[u]:
            new_cost = current_cost + w
            if new_cost < dist[v]:
                dist[v] = new_cost
                heapq.heappush(heap, (new_cost, v))
                
    
    min_cost[start] = dist[end]

start = x

x_to_home = [float('inf')] * (n+1)

heap = [(0, start)]
while heap:
    current_cost, u = heapq.heappop(heap)
    
    if current_cost > x_to_home[u]:
        continue
    
    for v, w in graph[u]:
        new_cost = current_cost + w
        if new_cost < x_to_home[v]:
            x_to_home[v] = new_cost
            heapq.heappush(heap, (new_cost, v))
    
for i in range(1, n+1):
    min_cost[i] += x_to_home[i]
    
print(max(min_cost[1:]))