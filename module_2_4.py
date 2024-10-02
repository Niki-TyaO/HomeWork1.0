members = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in range(len(members) + 1):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                not_primes.append(n)
                break
        else:
            primes.append(n)

print('Простые числа: ', primes)
print('Не простые числа: ', not_primes)