S = input()
T = input()

diff = len(T) - len(S)

for i in range(diff):
    if T[-1] == 'A':
        T = T[:-1] # 맨 뒤에 있는 문자를 제거
    else:
        T = T[:-1] # 맨 뒤에 있는 문자를 제거
        T = T[::-1] # 문자열을 뒤집음
        
if S == T:
    print(1)
else:
    print(0)