# 1. klasicky for cyklus
result =[]
x = 20

for num in range(1, x):
    if num % 2 == 0:
        result.append(num)

print(result)

# 2. ten isty for cyklus v list comprehension
result2 = [num2 for num2 in range(1, x) if num2 % 2 == 0]
print(result2)

# 3. pouzitie aj else - vtedy sa podmienkova cast dava pred hlavicku cyklu:
result3 =[num3 if num3 % 2 == 0 else -1*num3 for num3 in range(1, 20)]
print(result3)

# 4.
words = ["Janko", "Hrasko", "Bratislava"]
print([word.upper() for word in words])

# 5. vieme retazit for ( do jedneho for cyklu sme vnorili druhy for cyklus)
num1 = [1, 2]
num2 = [1, 2, 3]

print([(z, y) for z in num1 for y in num2])