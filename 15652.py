n, m = map(int, input().split())

result = []

def dfs(start, depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(start, n + 1):
        result.append(i)
        dfs(i, depth + 1)
        result.pop()
        
dfs(1, 0)