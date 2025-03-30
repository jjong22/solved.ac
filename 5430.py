t = int(input())

for i in range(t):
    operation = input()
    _ = input()
    arr = eval(input())
    is_error = False
    is_reverse = False
    
    for char in operation:
        if char == 'R':
            is_reverse = not is_reverse
        else:
            if len(arr) == 0:
                print('error')
                is_error = True
                break
            if is_reverse:
                arr.pop()
            else:
                arr.pop(0)
        
    if not is_error:
        if is_reverse:
            arr.reverse()
        print(str(arr).replace(' ', ''))