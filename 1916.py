import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost)) 

start, end = map(int, input().split())

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

print(dist[end])
