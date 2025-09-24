# Najdi vsetky prvocisla od 0 po 100

# numbers = range(2, 101)

# for prime in numbers:
#     is_prime = True
#     for divide in range(2, prime-1):
#         if == 0:
#             is_prime = False
#         else:
#             is_prime = True
#             print(prime)
for n in range(2, 101):
    is_prime = True
    for d in range(2, n):
        if n % d == 0:
            is_prime = False
            break
    if is_prime:
        print(n)
