import os

def clear_terminal():
    os.system("cls")

def menu():
    print("=== Hlavne menu ===")
    print("1 - Pozdrav")
    print("2 - Scitanie")
    print("3 - Odcitanie")
    print("4 - Nasobenie")
    print("5 - Delenie")
    print("6 - Historia vypoctov")
    print("7 - Koniec")
    print("===================\n")

def pozdrav():
    print("\nAhoj\n")

def koniec():
    print("\nKoniec\n")

def get_number(text):
    while True:
        try:
            number = float(input(text))
            return number
        except ValueError:
            print("\nToto nie je cislo! Skus to znova.\n")

def calculate(operator):
    number1 = get_number("\nZadaj prve cislo: ")
    
    if operator == "/":
        while True:
            number2 = get_number("Zadaj druhe cislo: ")

            if number2 == 0:
                print("\nNulou sa neda delit! Zadaj druhe cislo este raz\n")
            else:
                return number1 / number2
            
    else:
        number2 = get_number("Zadaj druhe cislo: ")

        if operator == "+":
            return number1 + number2
        elif operator == "-":
            return number1 - number2
        elif operator == "*":
            return number1 * number2
            
def scitanie():
    result = calculate("+")
    print(f"\nSucet oboch cisel je: {result}\n")
    history.append(f"Scitanie: {result}")

def odcitanie():
    result = calculate("-")
    print(f"\nRozdiel oboch cisel je: {result}\n")
    history.append(f"Odcitanie: {result}")

def nasobenie():
    result = calculate("*")
    print(f"\nSucin oboch cisel je: {result}\n")
    history.append(f"Nasobenie: {result}")

def delenie():
    result = calculate("/")
    print(f"\nPodiel oboch cisel je: {result}\n")
    history.append(f"Delenie: {result}")

def historia():
    for item in history:
        print(item)


options = {
    1 : pozdrav,
    2 : scitanie,
    3 : odcitanie,
    4 : nasobenie,
    5 : delenie,
    6 : historia,
    7 : koniec
}

history = []

while True:
    clear_terminal()
    menu()
    
    try:
        volba = int(input("Zadaj volbu: "))
        if volba in options:
            options[volba]()
            if volba == 6:
                break
            else:
                input("Stlac Enter pre pokracovanie ...")
        else:
            print("\nZadaj volbu 1 az 6\n")
            input("Stlac Enter pre pokracovanie ...")
    except ValueError:
        print('\nZadal si nepovoleny znak. Zadaj hodnotu "1" az "6"\n')
        input("Stlac Enter pre pokracovanie ...")
