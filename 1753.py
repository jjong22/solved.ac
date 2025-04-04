import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost)) 

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

for i in range(1, n+1):
    if i == start:
        print(0)
    elif dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])