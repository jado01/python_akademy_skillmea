numbers = range(2, 101)

for prime_number in numbers:
    is_prime = True
    for divider in range(2, prime_number):
        if prime_number % divider == 0:
            is_prime = False
            break
    if is_prime == True:
        print(prime_number)
