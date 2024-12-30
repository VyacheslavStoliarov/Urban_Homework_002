numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# numbers = [9, 11, 12, 13, 14, 15, 1, 2, 3, 4, 5, 6, 7, 8]
print('Без флага')
primes = []
not_primes = []
for i in numbers:
    if i != 1:
        for j in range(sorted(numbers)[0], i + 1):
            if j != 1 and i % j == 0:
                if i != j:
                    not_primes.append(i)
                    break
                primes.append(i)
print('Primes: ', primes)
print('Not Primes: ', not_primes)

# *****************
print('С флагом')
primes = []
not_primes = []
for i in numbers:
    is_prime = True
    if i != 1:
        for j in range(sorted(numbers)[0], i + 1):
            if j != 1 and i % j == 0:
                if i != j:
                    is_prime = False
                    break
        if is_prime:
            primes.append(i)
        else:
            not_primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_primes)