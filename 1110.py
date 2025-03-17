a = int(input())
save = a
count = 0

while(1):
    if(a < 10):
        a *= 11
        count += 1
    else:
        a = ((a % 10) * 10) + ((a // 10 + a % 10) %10)
        count += 1
    if (save == a):
        break
        
print(count)