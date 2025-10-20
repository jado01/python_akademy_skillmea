# Webinár 7 – Cykly (for a while) (2025-09-08)

## Obsah
- DRY (Don't Repeat Yourself)
- Iterácie a cykly
- `for` cyklus
- Premenná `_` ako zamlčaná premenná
- `range()` – generovanie čísel
- Vnorené cykly
- Podmienky v cykloch
- `while` cyklus

## Poznámky
- **DRY = Don't Repeat Yourself** → namiesto opakovania kódu používame cyklus.
- **For cyklus** prechádza každý prvok postupnosti:
    ```python
    for element in [1, 2, 3, 4, 5]:
         print(element)
    print("end")
    ```
    program vypise:
    1
    2
    3
    4
    5
    end
    - Iteracia po stringu:
    ```python
    name = "Michal"
    for letter in name:
        print(letter)
    ```
    program vypise:
    M
    i
    c
    h
    a
    l
    
    - ak dam do printu end="" tak vypise string do jedneho riadku, neodriadkuje po kazdej iteracii:
    ```python
    name = "Michal"
    for letter in name:
        print(letter, end="")
    ```
    program vypise:
    Michal
    
    - Podtržník "_" → zamlčaná premenná (keď ju nepotrebujem použiť).
    - range(start, stop) → generuje čísla v intervale <start, stop):
    ```python
    numbers = range(0, 11)
    for number in numbers:
        if number % 2 == 0:
            print(number)  # iba párne čísla
    ```
    - Vnorené cykly – všetky kombinácie čísel:
    ```python
    numbers = range(0, 11)
    for first in range(0, 11):
        for second in range(0, 11):
            print(f"[{first}, {second}]")
    ```
    - Príklad – nahradenie znaku v stringu:
    ```python
    name = "janko hrasko"
    for letter in name:
        if letter == "n":
            print("N", end="")
        else:
            print(letter, end="")
    ```
    - While cyklus – opakuje, kým platí podmienka:
    ```python
    counter = 0
    while counter < 5:
        print("Doors are open")
        counter += 1
    print("Doors are closed")
    ```
**Zhrnutie a porovnanie cyklov:**
    🔹 Kedy použiť for cyklus:
        - keď vieš dopredu, koľkokrát sa má cyklus zopakovať
        - alebo keď chceš prejsť cez zoznam, string alebo iný iterovateľný objekt

    🔹 Kedy použiť while
        - keď nevieš dopredu, koľkokrát sa cyklus zopakuje
        - keď závisí na nejakej podmienke, ktorá sa počas behu mení
        - používa sa často v hrách, pri práci so vstupom, kým niekto nezadá správnu hodnotu
    
    📝 Zhrnutie
        - For je kratší a ideálny, keď poznám počet opakovaní.
        - While je flexibilnejší – použijem ho, keď neviem, koľkokrát sa cyklus zopakuje (napr. „kým používateľ nezadá správne heslo“).
        
### Úlohy
**Ulohy od lektora**

**Ulohy od AI**
1. Vypíš všetky čísla od 1 po 20.
2. Vypíš iba párne čísla od 0 po 50.
3. Skús vnorený cyklus → vypíš všetky kombinácie dvojíc od 0 po 5.
4. Napíš program, ktorý vo vete nahradí malé „a“ veľkým „A“.
5. Skús program s while cyklom – nech niečo vypíše 10×.

---

## 🔹 Ukážkové súbory do `webinar_07/examples/`




