r = 31
M = 1234567891

def get_num(c : chr) -> int: 
    return ord(c) - 96

n = int(input())
str_input = input()
i = 0
result = 0

for c in str_input:
    result += get_num(c) * pow(r, i, M) 
    result %= M
    i += 1

print(result)