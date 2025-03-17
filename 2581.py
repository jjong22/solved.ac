m = int(input())
n = int(input())
pri = []
ispri = True
sum = 0
low_sum = 0

for i in range (m,n+1):
    for j in range (2,i):
        if (i % j == 0):
            ispri = False
            break
    if (ispri == True):
        pri.append(i)
    else:
        ispri = True
        
if (len(pri) != 0):
    if (pri[0] == 1):
        del(pri[0])
# 1이 소수로 포함되었을 경우를 제외해줌
        
for i in range (len(pri)):
    sum += pri[i]
    
if (len(pri) == 0):
    print( -1 )
else :
    print(sum)
    print(pri[0])