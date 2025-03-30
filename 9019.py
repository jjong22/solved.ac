from collections import deque

def D(a):
    return (a * 2) % 10000

def S(a):
    return (a - 1) % 10000

def L(a):
    return (a % 1000) * 10 + (a // 1000)

def R(a):
    return (a // 10) + (a % 10) * 1000

# use queue for BFS
# use stack for DFS

def DSLR(a, b):
    queue = deque()
    queue.append((a, ""))
    visited = [False] * 10000 
    visited[a] = True
            
    while queue:
        current, oper = queue.popleft()
        if current == b:
            return oper
        
        for next_num, operation in [(D(current), "D"), (S(current), "S"), (L(current), "L"), (R(current), "R")]:
            if not visited[next_num]:
                visited[next_num] = True
                queue.append((next_num, oper + operation))
    
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    result = DSLR(a, b)
    print(result)
    