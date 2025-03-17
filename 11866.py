num, t = map(int, input().split())

sque = [i + 1 for i in range(num)]
jo_sque = []

iter = 0
heap = 0
cnt = num

while(1):
    heap += 1
    
    if (heap == t):
        
        jo_sque.append(sque[iter])
        del sque[iter]
        
        heap = 0
        iter -= 1
        cnt -= 1
        
    iter += 1
        
    if (iter >= cnt):
        iter -= cnt
        
    if (cnt == 0):
        break

print("<", end="")
for num in jo_sque:
    if (num != jo_sque[-1]):
        print("%d," %num, end=" ")
    else :
        print(num, end="")
print(">")
    
