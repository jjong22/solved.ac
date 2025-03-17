n = int(input())
total = []
score = 0
count = 1

for i in range(n):
    answer = input()
    for j in range(len(answer)):
        if (answer[j] == "O"):
            score += count
            count += 1
        else:
            count = 1
    total.append(score)
    score = 0
    count = 1
    
for i in range(n):
    print(total[i])