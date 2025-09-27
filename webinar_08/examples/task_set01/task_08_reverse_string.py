# Úloha 8 - Text naopak
# Zadaj reťazec a vypíš ho odzadu, bez použitia [::-1].
# text = "Python"
# Vystup: nohtyP

# Sem napíš svoje riešenie:

text = "Janko Hrasko"
index = -1 # v prvych troch verziach pouzivam, vo stvrtej uz netreba

# PRVA VERZIA S VNORENYM CYKLOM - ZBYTOCNE KOMPLIKOVANE
# for _ in text:
#     reverse_text = text[index]
#     for reverse in text:
#         if reverse == reverse_text:
#             print(reverse , end = "")
#     index += -1

# DRUHA VERZIA UZ IBA S JEDNYM CYKLOM:

# for _ in text:
#     reverse_text = text[index]
#     print(reverse_text, end = "")
#     index -= 1

# TRETIA VERZIA S WHILE:

# while index >= -len(text):
#     print(text[index], end = "")
#     index -= 1

# STVRTA VERZIA S FOR A range

for i in range(len(text)-1, -1, -1):
    print(text[i], end = "")