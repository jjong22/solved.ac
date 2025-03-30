import sys
input = sys.stdin.readline

def distance(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(eucledian_points):
    if len(eucledian_points) <= 1:
        return 0
    if len(eucledian_points) == 2:
        return distance(eucledian_points[0], eucledian_points[1])
    if len(eucledian_points) == 3:
        return min(distance(eucledian_points[0], eucledian_points[1]), 
                   distance(eucledian_points[1], eucledian_points[2]), 
                   distance(eucledian_points[2], eucledian_points[0]))
    
    mid = len(eucledian_points) // 2
    vertical_line = eucledian_points[mid][0]  # x 좌표 기준 분할
    
    delta = min(closest_pair(eucledian_points[:mid]), closest_pair(eucledian_points[mid:]))
    
    p_delta = [i for i in eucledian_points if (i[0] - vertical_line) ** 2 <= delta]
    p_delta.sort(key=lambda p: p[1]) # ?
    
    for i in range(len(p_delta)):
        for j in range(i + 1, min(i + 12, len(p_delta))):
            delta = min(delta, distance(p_delta[i], p_delta[j]))
            
    return delta


n = int(input())
eucledian_points = []

for i in range(n):
    x, y = map(int, input().split())
    eucledian_points.append((x, y))

points = sorted(eucledian_points)
print(closest_pair(points))