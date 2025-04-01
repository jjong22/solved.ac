n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = []

def dfs(idx, depth):
    if depth == m:
        print(*result)
        return
    
    for i in range(idx, n):
        num = numbers[i]
        result.append(num)
        dfs(i+1,depth + 1)
        result.pop()
        
dfs(0, 0)