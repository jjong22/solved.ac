from collections import deque

n, m = map(int, input().split())

adj_list = {}

def add_edge(u, v):
    if u not in adj_list:
        adj_list[u] = []
    if v not in adj_list:
        adj_list[v] = []
        
    adj_list[u].append(v)
    adj_list[v].append(u)
    
for i in range(n):
    u, v = map(int, input().split())
    add_edge(u, v)
    
for i in range(m):
    u, v = map(int, input().split())
    add_edge(u, v)
    
visited = [False] * 101

def bfs(start):
    queue = deque()
    queue.append([start, 0])
    visited[start] = True
    
    while queue:
        line = queue.popleft()
        node, cnt = line[0], line[1]
        
        for i in range(1, 6+1):
            if not visited[i+node]:
                if i+node == 100:
                    return cnt+1
                
                visited[i+node] = True
                
                if i+node in adj_list:
                    slid = adj_list[i+node]
                    visited[slid] = True
                    queue.append([slid, cnt+1])
                else: 
                    queue.append([i+node, cnt+1])
        

print(bfs(1))
    