from collections import deque

n, k = map(int, input().split())
time = 0
linear_graph = set([n])
queue = deque([n])

while queue:
    for _ in range(len(queue)):
        x = queue.popleft()
        if x == k:
            print(time)
            exit()
       
        for next_num in (x-1, x+1, x*2):
            if 0 <= next_num <= 100000 and next_num not in linear_graph:
                linear_graph.add(next_num)
                queue.append(next_num)
                
    time += 1