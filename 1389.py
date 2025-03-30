from collections import deque

G = [ [ 0 for j in range(101) ] for i in range(101) ]

def BFS(G, start):
    queue = deque()
    queue.append( (start, 1) )
    visited = [False] * 101
    num_length = [0] * 101
    
    while queue:
        start_node, now_length = queue.popleft()
        
        for i in range(1, 101):
            if G[start_node][i] == 1:
                if visited[i]:
                    num_length[i] = min(num_length[i], num_length[start_node] + now_length)

                else:
                    num_length[i] = now_length
                    visited[i] = True
                    queue.append( (i, now_length+1) )
            
    return sum(num_length)
            
    

n, m = map(int, input().split())
nodes = set()

for i in range(m):
    x, y = map(int, input().split())
    nodes.add(x)
    G[x][y] = 1
    G[y][x] = 1
    
kevin_bacon = []
    
for node in nodes:
    kevin_bacon.append( [node, BFS(G, node)])

kevin_bacon.sort(key=lambda kevin_bacon: kevin_bacon[0])
kevin_bacon.sort(key=lambda kevin_bacon: kevin_bacon[1])

print(kevin_bacon[0][0])
