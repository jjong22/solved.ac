num = 0
hour = []

fibonachi = []
fibonachi.append(0)
fibonachi.append(1)

while (num != -1):
    num = int(input())
    if(num == -1):
        break
    hour.append(num)
    
for j in range (len(hour)):
    if (hour[j] == 1):
        print("Hour %d: %d cow(s) affected" % (hour[j],fibonachi[hour[j]]))
    else:
        for i in range (hour[j]-1):
            fibonachi.append(fibonachi[i] + fibonachi[i+1])
        print("Hour %d: %d cow(s) affected" % (hour[j],fibonachi[hour[j]]))
    fibonachi = []
    fibonachi.append(0)
    fibonachi.append(1)