# Príklad A – Obvod a obsah kruhu
# Do premennej r ulož polomer kruhu.
# Vypočítaj obvod: 2 * π * r.
# Vypočítaj obsah: π * r**2.
# Výsledky vypíš.
# Bonus: skús použiť math.pi (import z knižnice math).

import math

r = 2.5
v = (4/3) * math.pi * r**3
s = 4 * math.pi * r**2

print(f"Obvod kruhu je: {2 * math.pi * r:.2f}")
print(f"Obsah kruhu je: {math.pi * r**2:.2f}")
print(f"Priemer kruhu je: {2 * r:.2f}")
print(f"Objem gule je: {v:.2f}")
print(f"Obsah gule je: {s:.2f}")
print(f"{r:.2f}")