def fibonacci(n):
    f_data = [1 if i <= 1 else 0 for i in range(n + 1)]

    last_pos = 1
    if(f_data[n-1] == 0):
        for i in range(last_pos + 1, n + 1):
            f_data[i] = (f_data[i - 1] + f_data[i - 2])
        last_pos = n - 1
    return f_data[n-1]

n = int(input())
print(fibonacci(n))