n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
visited = {}

result = []
for num in numbers:
    visited[num] = False

def dfs(depth):
    if depth == m:
        print(*result)
        return
    
    for num in numbers:
        if visited[num]:
            continue
        
        visited[num] = True
        result.append(num)
        
        dfs(depth + 1)
        
        visited[num] = False
        result.pop()
        
dfs(0)