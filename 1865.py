import sys
input = sys.stdin.readline
print = sys.stdout.write

tc = int(input())

def check_for_negative_cycle():
    distance = [float("inf")] * (n + 1)
    distance[0] = 0 # virtual node

    for i in range(n):  # |V|번 반복
        updated = False
        for cur_node, next_node, edge_cost in edges:
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                updated = True

        if not updated: 
            break
    
    # **n번째에도 갱신이 일어나는지 확인해야 음수 사이클 존재**
    for cur_node, next_node, edge_cost in edges:
        if distance[next_node] > distance[cur_node] + edge_cost:
            return True

    return False

for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    
    for i in range(n):
        edges.append((0, i + 1, 0))

    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((a, b, c))
        edges.append((b, a, c))
        
    for _ in range(w):
        a, b, c = map(int, input().split())
        edges.append((a, b, -c))

    has_negative_cycle = check_for_negative_cycle()

    if has_negative_cycle:
        print("YES\n")
    else:
        print("NO\n")