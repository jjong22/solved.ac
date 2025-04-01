n, m = map(int, input().split())

result = []

def dfs(depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(1, n + 1):
        result.append(i)
        dfs(depth + 1)
        result.pop()
        
dfs(0)