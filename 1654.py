n, total = map(int, input().split())
line_list = []

for num in range(n):
    line_list.append(int(input()))
    
line_list.sort()

low = 1
high = line_list[-1]
result = 0

while(low <= high):
    mid = (low + high) // 2
    summation = 0
    for i in range(n):
        summation += (line_list[i] // mid)
        
    if summation >= total:
        result = mid
        low = mid + 1
        
    else:
        high = mid - 1
         
print(result)