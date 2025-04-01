n, m = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[False] * m for _ in range(n)]
max_result = 0

def dfs(x, y, depth, total):
    global max_result
    
    if depth == 4:
        max_result = max(max_result, total)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + blocks[nx][ny])
            visited[nx][ny] = False

# T자 모양 예외 처리
def check_t_shape(x, y):
    global max_result
    
    for i in range(4):
        total = blocks[x][y]
        count = 0
        
        for j in range(4):
            if i == j:
                continue
            nx, ny = x + dx[j], y + dy[j]
            if 0 <= nx < n and 0 <= ny < m:
                total += blocks[nx][ny]
                count += 1
        
        if count == 3:  # 3개의 블록을 선택한 경우
            max_result = max(max_result, total)

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, blocks[i][j])  # DFS 탐색
        visited[i][j] = False
        check_t_shape(i, j)  # T자 모양 체크

print(max_result)
