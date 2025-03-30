prime_dict = {}

def fatorization(n):
    prime_dict[1] = 1
    
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_dict[i] = prime_dict.get(i, 0) + 1
            n //= i
            
n = int(input())
fatorization(n)
print(prime_dict)