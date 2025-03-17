is_make = []
n_sum = 0

def solution(n):
    answer=0
    while n>0 :
        answer+=n%10
        n//=10
    return answer

for i in range (10000):
    n_sum = solution(i+1) # 자릿수를 모두 더해줌.
    is_make.append(i+1 + n_sum)
    
for i in range (10000):
    if (is_make.count(i+1) == 0):
        print(i+1)