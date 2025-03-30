n, m, b = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(n)]

# add to inventory = 2
# move block to ground = 1

times = []

for i in range(257):
    time = 0
    inventory = b
    for j in range(n):
        for k in range(m):
            if ground[j][k] > i:
                time += 2 * (ground[j][k] - i) # 파내는 경우
                inventory += ground[j][k] - i
            else:
                time += 1 * (i - ground[j][k]) # 쌓는 경우
                inventory -= i - ground[j][k]
    if inventory >= 0:
        times.append([time, i])

times.sort(key=lambda x: (x[0], -x[1]))

print(times[0][0], times[0][1])

