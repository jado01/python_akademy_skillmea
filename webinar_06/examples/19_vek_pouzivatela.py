# Načítaj vek od používateľa a skontroluj, či je dospelý.

vek = input("Zadaj svoj vek:\n")
vek = int(vek)

if vek >= 18:
    print("Si dospely")
else:
    print("Nie si dospely")