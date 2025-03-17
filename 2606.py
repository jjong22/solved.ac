graph = [[0 for i in range(101)] for j in range(101)]
infected = [0 for i in range(101)]

computer_num = int(input())
edge_num = int(input())

for i in range(edge_num): # graph init
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def travel(graph, host):
    infected[host] = 1

    for i in range(1, computer_num + 1):
        if graph[host][i] == 1 and infected[i] == 0:
            travel(graph, i)

travel(graph, 1)
    
infected_num = sum(infected) - 1
        
print(infected_num)