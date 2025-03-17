n, k = map(int, input().split())
pri = []
save_pri = []
deleted_num = 0
memory = 0
roop = 0

for i in range(2, n + 1):
    pri.append(i)
    
while (k != deleted_num):
    memory = pri[0] + roop
    if (save_pri.count(memory) == 0):
        deleted_num += 1
        save_pri.append(pri[0])
        del(pri[0])
        
    if (deleted_num == k):
                break
    
    for i in range (len(pri)):
        if (pri[i] % memory == 0):
            save_pri.append(pri[i])
            pri[i] = 1
            deleted_num += 1
            
            if (deleted_num == k):
                break
          
    while (save_pri.count(pri[0] + roop) != 0):
        roop += 1      
    
    while (pri.count(1) != 0):
        pri.remove(1)
          
print(save_pri[k-1])