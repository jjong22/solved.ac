# start = [a, b]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS_map(graph, start):
    queue = []
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        start = queue.pop(0)
        for i in range(4):
            x = start[0] + dx[i]
            y = start[1] + dy[i]
            if x >= 0 and x < m and y >= 0 and y < n:
                if graph[x][y] == 1 and visited[x][y] == 0:
                    queue.append([x, y])
                    visited[x][y] = 1
                    
                    
def DFS_map(graph, start):
    stack = []
    stack.append(start)
    visited[start[0]][start[1]] = 1
    while stack:
        start = stack.pop()
        for i in range(4):
            x = start[0] + dx[i]
            y = start[1] + dy[i]
            if x >= 0 and x < m and y >= 0 and y < n:
                if graph[x][y] == 1 and visited[x][y] == 0:
                    stack.append([x, y])
                    visited[x][y] = 1
        
                    
test_case = int(input())
                    
for i in range(test_case):
    m, n, num_of_cabbage = map(int, input().split())
    nodes = []
    visited = [ [0 for j in range(n)] for i in range(m)]
    
    graph = [ [0 for j in range(n)] for i in range(m)]
    
    for j in range(num_of_cabbage):
        x, y = map(int, input().split())
        nodes.append([x, y])
        graph[x][y] = 1
    
    start = [0, 0]
    num_of_worm = 0
    
    for node in nodes:
        if visited[node[0]][node[1]] == 0:
            BFS_map(graph, node)
            num_of_worm += 1
            
    print(num_of_worm)
            
            