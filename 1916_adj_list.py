import heapq

def dijkstra(G, start, dest):
    dist = {node: float("Inf") for node in G} 
    dist[start] = 0 
    heap = []
    heapq.heappush(heap, [dist[start], start]) # 거리 기준으로 정렬
        
    while heap:
        current_dist, u = heapq.heappop(heap)
        
        if dist[u] < current_dist:
            continue
        
        for v, new_dist in G[u].items(): # from G
            distance = current_dist + new_dist
            if distance < dist[v]:
                dist[v] = distance
                heapq.heappush(heap, [distance, v])
                
    return dist[dest]

n = int(input())
m = int(input())

G = {}

for i in range(n+1):
    G[i] = {}

for i in range(m):
    u, v, cost = map(int, input().split())
    G[u][v] = cost # from u to v


start, dest = map(int, input().split())

print(dijkstra(G, start, dest))
