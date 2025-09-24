# Úloha 4 - Over silu hesla
# Zisti, či zadané heslo má aspoň 8 znakov.
# Ak áno, vypíš 'Silne heslo', inak 'Slabe heslo'.
# heslo = "python123"
# Vystup: Silne heslo

# Sem napíš svoje riešenie:

#kod cez funkciu len():
# password = "python123"

# if len(password) >= 8:
#     print("Silne heslo")
# else:
#     print("Slabe heslo")

#cez for cyklus:

# password = "python123"

# counter = 0

# for word in password:
#     counter += 1
# if counter >= 8:
#     print("Strong password")
# else:
#     print("Weak password")

password = "python123"

counter = 0
i = 0

while i < len(password):
    counter += 1
    i +=1
if counter >= 8:
    print("Strong password")
else:
    print("Weak password")
    