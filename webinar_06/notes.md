# Webinár 6 – Zoznamy (listy) a podmienky (if/else) (2025-09-19)

## Obsah
- Zoznamy (listy) – úpravy, mazanie, pridávanie
- Mutable vs immutable
- Operácie na listoch (`append`, `remove`, `extend`, `insert`, `count`, `index`, `reverse`, `sort`)
- Podmienky: `if`, `elif`, `else`
- Ternárny operátor (skrátený zápis)

### Poznámky
- **Listy** sú **mutable** → dajú sa meniť.  
  **Stringy** sú **immutable** → nemôžu sa meniť priamo.
- Menenie hodnoty v liste:
  ```python
  ages = [29, 33, 45, 24]
  ages[1] = 50
  ```
- **Nahradenie časti zoznamu cez slicing**:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]

    ages[1:3] = [0, 0]
    print(ages)

    >>>[29, 0, 0, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]
    ```
- **Mazanie prvkov v liste**:
    - cez slicing:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]

    ages[1:2] = []
    print(ages)

    >>>[29, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]
    ```
    - cez del:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]

    del ages[0:2]

    print(ages)

    >>>[45, 24, 29, 33, 45, 24, 29, 33, 45, 24]
    ```
- **Spočítavanie listov**:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]

    result = ages + [0, 0]

    print(result)

    >>>[29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24, 0, 0]
    ```
- **Skrátené spočítavanie listov**:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]
    ages += [0, 0]

    print(ages)

    >>>[29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24, 0, 0]
    ```
- **Pridanie prvku na koniec listu**:
    ```python
    ages = [29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24]
    ages += [0, 0]

    print(ages)

    >>>[29, 33, 45, 24, 29, 33, 45, 24, 29, 33, 45, 24, 0, 0]
    ```
- **Odstránenie prvku z listu**:
    ```python
    ages = [1, 2, 3, 4]

    ages.remove(2)  #vymaze vzdy prvy vyskyt

    print(ages)

    >>>[1, 3, 4]
    ```
- **Spočítanie výskytu prvku**:
    ```python
    ages = [1, 2, 3, 4, 2]

    result = ages.count(2)

    print(result)

    >>>2
    ```
- **Pridanie viacerých prvkov**:
    ```python
    ages = [1, 2, 3, 4, 2]

    ages.extend([1, 1])

    print(ages)

    >>>[1, 2, 3, 4, 2, 1, 1]
    ```
- **Hľadanie pozície prvku**:
    ```python
    ages = [1, 2, 3, 4, 2]

    result = ages.index(2)

    print(result)

    >>>1
    ```
- **Vkladanie prvku**:
    ```python
    ages = [1, 2, 3, 4, 2]

    ages.insert(2, "Michal")

    print(ages)

    >>>ages = [1, 2, Michal, 3, 4, 2]
    ```
- **Otočenie zoznamu**:
    ```python
    ages = [1, 2, 3, 4, 2]

    ages.reverse()    - inplace otocenie

    print(ages)

    >>>[2, 4, 3, 2, 1]
    ```
- **Otočenie zoznamu a zanechanie pôvodnej premennej ages**:
    ```python
    ages = [1, 2, 3, 4, 2]

    reversed_ages = ages[::-1]  # otocenie zoznamu a zanechanie povodnej premennej ages

    print(reversed_ages)

    >>>[2, 4, 3, 2, 1]
    ```
- **Usporiadanie hodnôt - triedenie**:
    ```python
    ages = [1, 2, 3, 4, 2]

    ages.sort()  # dokaze sortovat aj stringy podla abecedy

    print(ages)

    >>>[1, 2, 2, 3, 4]
    ```
- **PODMIENKY**:
    - **if/else**:
        ```python
        age = input("How are You old?\n")

        if int(age) >= 18:
            print("Is adult")
            print("Yes, He is")
        else:
            print("Is not adult")
            print("No, She is not")
        print("This will be printed always")
        ```
    - **if/elif/else**:
        ```python
        position = 4

        if position == 1:
            print("Competitor was first")
        elif position == 2:
            print("Competitor was second")
        elif position == 3:
            print("Competitor was third")
        else:
            print("Competitor participated")
        
        ```
    - **Ternárny operátor**:
        - jednoriadkový ternárny operátor ma 3 časti
        - da sa takto zapísať kód s vekom (zakomentovaný nižšie), nevýhoda je, že nievieme
        použiť viac riadkov ako print a pod. ...
        ```python
        age = 19
        # is_adult = -1

        # if age > 18:
        #     is_adult = True
        # else:
        #     is_adult = False

        is_adult = True if age > 18 else False

        print(is_adult)
        ```
        - dá sa použiť aj inline
        ```python
        age = 19
        adult_counter = 0

        adult_counter += 1 if age > 18 else 0

        print(adult_counter)
        ```
    - príklad s listom
    ```python
    adult_name = []
    age = 29
    name = "Michal"

    adult_name.append(name) if age > 18 else None

    print(adult_name)
    ```
    - toto je to iste ako kod vyzsie:
    ```python
    adult_name = []
    age = 29
    name = "Michal"

    if age > 18:
        adult_name.append(name)

    print(adult_name)
    ```

#### Ulohy
**Zisti, co robi kod - Cvicenia na porozumenie**
01. Priklad 1 - Jednoduchy vypocet
    a = 4
    b = 2
    vysledok = a ** b + 1
    print(vysledok)
    Otazka: Co vypise program? Co znamena **?
02. Priklad 2 - Spajanie retazcov
    meno = "Tomas"
    vek = 15
    info = f"{meno} ma {vek + 1} rokov."
    print(info)
    Otazka: Co presne vypise program? Preco sa pouzilo f""?
03. Priklad 3 - Priemer a zaokruhlovanie
    cisla = [3, 5, 7]
    priemer = sum(cisla) / len(cisla)
    print(round(priemer))
    Otazka: Ake cislo sa vypise a co spravi funkcia round()?
04. Priklad 4 - Praca so zoznamom
    ovocie = ["jablko", "banan", "hruska"]
    ovocie.append("kiwi")
    ovocie[0] = "jahoda"
    print(ovocie)
    Otazka: Ako bude vyzerat zoznam po vsetkych zmenach?
05. Priklad 5 - Kombinovane operacie
    x = 3
    y = 4
    vysledok = x * (y + 2) - (x + y)
    print(vysledok)
    Otazka: Vypocitaj vysledok rucne. Vies vysvetlit preco je taky?
06. Priklad 6 - Zaujimave indexovanie
    slovo = "elektrina"
    print(slovo[1] + slovo[-2])
    Otazka: Ktore dva znaky sa vytlacia? Co znamena zaporny index?
07. Priklad 7 - Vkladanie a mazanie zo zoznamu
    farby = ["cervena", "modra", "zelena"]
    farby.insert(1, "zlta")
    del farby[2]
    print(farby)
    Otazka: Ako sa zmeni zoznam po tychto operaciach?
08. Priklad 8 - Zlozitejsi vypocet s typmi
    a = 10
    b = "5"
    vysledok = a + int(b) * 2
    print(vysledok)
    Otazka: Preco musime prevadzat b na cislo? Aky je vysledok?
09. Priklad 9 - Hladanie znaku
    data = ["auto", "vlak", "lod"]
    slovo = data[1]
    znak = slovo[0]
    print(znak.upper())
    Otazka: Co sa vytlaci a preco?
10. Priklad 10 - Vzorec a dlzka retazca
    vzorec = "a^2 + b^2 = c^2"
    dlzka = len(vzorec)
    print(dlzka - 5)
    Otazka: Kolko znakov ma vzorec? Co sa vypise?
11. Priklad 11 - Jednoducha podmienka
    cislo = 10
    if cislo > 5:
    print("Cislo je vacsie ako 5")
    Otazka: Co vypise program? A preco?
12. Priklad 12 - Podmienka s else
    vek = 12
    if vek >= 18:
    print("Dospely")
    else:
    print("Nie je dospely")
    Otazka: Ktora cast sa vykona a co sa vytlaci?
13. Priklad 13 - Viacero podmienok
    znamka = 2
    if znamka == 1:
    print("Vyborny")
    elif znamka == 2:
    print("Chvalitebny")
    else:
    print("Ine")
    Otazka: Ktory text sa vypise? A preco?
14. Priklad 14 - Podmienka s rovnostou
    meno = "Anna"
    if meno == "Anna":
    print("Ahoj Anna!")
    Otazka: Co sa stane, ak meno bude "Jana"? A co teraz?

- **Priklady od AI**:
15. Vytvor zoznam čísel a zmeň niektorý prvok.
16. V zozname vymaž konkrétne prvky pomocou slicing aj del.
17. Použi append, remove, extend, insert.
18. Otestuj reverse a sort.
19. Načítaj vek od používateľa a skontroluj, či je dospelý.
20. Napíš program s if/elif/else, ktorý vypíše umiestnenie súťažiaceho.
21. Skús ternárny operátor a porovnaj so štandardným if/else.