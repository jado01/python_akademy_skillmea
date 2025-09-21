# Webinár 5 – String metódy, f-stringy, input, listy (2025-09-15)

## Obsah
- Metódy stringov (`upper`, `lower`, `capitalize`, `title`)
- Úprava textu (`replace`, `strip`, `lstrip`, `rstrip`)
- Kontrola textu (`startswith`, `endswith`, `find`, `count`)
- f-stringy
- Funkcia `input()`
- Zoznamy (listy) – indexovanie, slicing, vnorené zoznamy

## Poznámky
- **String metódy**:
  ```python
  name = "michal hucko"
  print(name.upper())       # MICHAL HUCKO
  print(name.lower())       # michal hucko
  print(name.capitalize())  # Michal hucko
  print(name.title())       # Michal Hucko
  ```
- **replace() – nahradí text**:
    ```python
    text = "Hello world"
    print(text.replace("world", "Python"))  # Hello Python
    ```
- **strip(), lstrip(), rstrip() – odstraňujú medzery**:
    ```python
    text = "   Hello world   "
    print(text.strip())   # "Hello world"
    print(text.lstrip())  # "Hello world   "
    print(text.rstrip())  # "   Hello world"
    ```
- **startswith(), endswith() – citlivé na veľké/malé písmená**
- **find() – index výskytu textu (alebo -1 ak nenájde)**
- **count() – počet výskytov znaku alebo podreťazca**
- **f-string**:
    ```python
    name = "Michal"
    age = 29
    adress = "Bratislava"

    print(f"name: {name}\nage: {age}\nadress: {adress}")
    ```
- **input()**:
    ```python
    name = "Michal"
    age = 29
    adress = "Bratislava"

    print(f"name: {name}\nage: {age}\nadress: {adress}")
    ```
- *** Zoznamy***:
    ```python
    grade_list = [1, 1, 2, 3, "Michal", "Janko", 2.5, True]

    print(grade_list[0])      # 1
    print(grade_list[:2])     # [1, 1]
    print(grade_list[-4:])    # ['Michal', 'Janko', 2.5, True]

    nested = [1, 2, "Ferko"]
    grade_list.append(nested)
    print(grade_list[-1][-1])  # Ferko
    print(grade_list[-1][-1][-1])  # o
    ```
## Úlohy od AI
1. Použi rôzne stringové metódy na vlastný text.
2. Skús použiť replace a zmeň slovo vo vete.
3. Otestuj strip, lstrip, rstrip.
4. Skontroluj, či text začína alebo končí určitým slovom.
5. Použi f-string na formátovaný výstup s menom, vekom a mestom.
6. Využi input() a opýtaj sa používateľa na meno a vek.
7. Vytvor zoznam s rôznymi typmi hodnôt a skús indexovanie + slicing.

