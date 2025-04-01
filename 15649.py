n, m = map(int, input().split())

result = []
visited = [False] * (n + 1)

def dfs(depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(i)
        
        dfs(depth + 1)
        
        visited[i] = False
        result.pop()
        
dfs(0)