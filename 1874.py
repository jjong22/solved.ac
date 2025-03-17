n = int(input())

num_sequencial = []
op_stack = []
num_stack = []

for i in range(n):
    num_sequencial.append(int(input()))
    
number = 0
idx = 0

while(1):
    if (num_sequencial[idx] > number):
        number += 1
        num_stack.insert(0, number)
        op_stack.append('+')
    elif (num_sequencial[idx] == num_stack[0]):
        num_stack.pop(0)
        op_stack.append('-')
        idx += 1
    else:
        print("NO")
        exit(0)
        
    if (idx == n):
        break
    
for op in op_stack: 
    print(op)