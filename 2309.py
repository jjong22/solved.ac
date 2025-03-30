heights = [int(input()) for _ in range(9)]

heights.sort()
total = sum(heights)

for i in range(9):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(heights[k])
            exit()