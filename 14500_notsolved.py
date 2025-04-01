global n, m
n, m = map(int, input().split())

blocks = [ [ 0 for i in range(m)] for j in range(n)]


for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        blocks[i][j] = line[j]
        
        
def find_next_max_num(G, i, j, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    next_num = []
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
    
        if x >= 0 and x < n and y >= 0 and y < m:
            if not visited[x][y]:
                next_num.append([G[x][y], x, y])
                visited[x][y] = True
    
    if next_num:
        return max(next_num)
    else: 
        return [0, i, j]
    
def tetoris(G, i, j):
    result_num = G[i][j]
    x_next, y_next = i, j
    visited = [ [False for __ in range(m)] for _ in range(n)]
    
    for k in range(3):
        line = find_next_max_num(G, x_next, y_next, visited)
        max_num, x_next, y_next = line[0], line[1], line[2]
        result_num += max_num
        
    return result_num

max_result = 0

for i in range(n):
    for j in range(m):
        max_result = max(max_result, tetoris(blocks, i, j))
        
print(max_result)