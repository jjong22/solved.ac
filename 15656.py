n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = []

def dfs(depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(0, n):
        num = numbers[i]
        result.append(num)
        dfs(depth + 1)
        result.pop()
        
dfs(0)