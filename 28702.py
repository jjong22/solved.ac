def get_result(i : int) -> int | str:
    if (i % 3 == 0 and i % 5 ==0):
        return "FizzBuzz"
    elif (i % 3 == 0):
        return "Fizz"
    elif (i % 5 == 0):
        return "Buzz"
    else :
        return i
    
a = input()
b = input()
c = input()
result = 0

try:
    a = int(a)
except:
    pass

try:
    b = int(b)
except:
    pass
        
try:
    c = int(c)
except:
    pass
    
if (str(type(a)) == "<class 'int'>"):
    print(get_result(a+3))  
elif (str(type(b)) == "<class 'int'>"):
    print(get_result(b+2))  
elif (str(type(c)) == "<class 'int'>"):
    print(get_result(c+1))  
