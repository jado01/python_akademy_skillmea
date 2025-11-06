def opakuj_slovo(slovo, pocet=3):
    slovo += " "
    return slovo * pocet

def spocitaj_samohlasky(text):
    text = text.lower()
    samohlasky = {"a", "e", "i", "o", "u", "á", "é", "í", "ó", "ú", "y", "ý"}
    counter = 0
    for pismeno in text:
        if pismeno in samohlasky:
            counter += 1
    return counter

def sucet_cisel(text):
    slova = text.split()
    sucet = 0
    for slovo in slova:
        try:
            slovo = int(slovo)
            sucet += slovo
        except ValueError:
            continue
    return sucet


print(opakuj_slovo("Python", 6))
print(spocitaj_samohlasky("Programovanie je zábava"))
print(sucet_cisel("12 jablk a 8 hrušiek a 3 melóny"))