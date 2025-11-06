import sys

while True:    
    user_input = input("Zadaj cislo (alebo 'q' pre koniec): ").strip().lower()
    if user_input == "q":
        print('Zadal si "q" ako "quit" tak program konci, ahoj👋')
        break
    
    try:
        number = int(user_input)
    except ValueError:
        print("To nie je cislo, skus to znova")
        continue

    if number == 0:
        print("Zadal si '0', zadaj kladne cislo")
        continue
    elif number < 0:
        print("Zadal si zaporne cislo, zadaj kladne cislo")
        continue
    
    i = 1
    sucet = 0

    while i <= number:
        sucet += i
        i += 1

    print(f"Sucet cisla od 1 do {number} je {sucet}")

    while True:
        c = input("Chces pokracovat? y/n ").strip().lower()
        if c in {"y", "yes", "áno", "ano"}:
            break
        if c in {"n", "no", "nie"}:
            print("OK, končím. 👋")
            sys.exit(0)
        print("Nerozumiem. Zadaj prosím y/n.")