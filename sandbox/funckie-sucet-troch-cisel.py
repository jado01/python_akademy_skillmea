def nacitaj_cislo(prompt):
    while True:
        try:
            cislo = int(input(prompt))
            return cislo
        except ValueError:
            print("Zadaj prosim cislo")

def sucet_troch():
    a = nacitaj_cislo("Zadaj prvé číslo: ")
    b = nacitaj_cislo("Zadaj druhé číslo: ")
    c = nacitaj_cislo("Zadaj tretie číslo: ")
    return a + b + c

vysledok = sucet_troch()
print(vysledok)