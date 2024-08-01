import math

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ]
primes = []
not_primes = []

for i in range(len(numbers)):
    n = numbers[i]
    is_prime = True
    if n < 2:
        continue
    else:
        f = math.sqrt(n) + 1
        for a in range(2, int(f)):
            if n % a == 0:
                is_prime = False
    if not is_prime:
        not_primes.append(n)
    else:
        primes.append(n)
print(f'Primes: {primes}')
print(f'Not primes: {not_primes}')
