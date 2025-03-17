# 문자열로 된 number
# 진법을 나타내는 digit

## ord("A") = 65. 즉 55를 빼야함.
## ord("0") = 48. 즉 48을 빼야함.

number, digit = input().split()

number = number[::-1]
digit = int(digit)

result = 0

deci_list = ["0", "1", '2', '3' ,'4' ,'5' ,'6','7', '8', '9']

cnt = 0

for char in number:
    if char in deci_list:
        result += (ord(char) - 48) * pow(digit, cnt) 
    else : 
        result += (ord(char) - 55) * pow(digit, cnt)
    
    cnt += 1

print(result)