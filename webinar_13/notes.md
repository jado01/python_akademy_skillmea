# Webinár 13 – Práca so súbormi a moduly (2025-09-24)

## Pokračovanie práce so súbormi

### Základné pojmy

* **EOF** = *End Of File* – koniec súboru.
* **IO object** = *Input/Output object* – objekt, pomocou ktorého vieme čítať alebo zapisovať dáta.
* Príkladom IO objektu je otvorený súbor.

---

## Kontextový manažér `with`

Pri práci so súbormi je vhodné používať kontextový manažér `with`.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

Výhody:

* súbor sa otvorí iba počas práce v bloku `with`,
* po skončení bloku sa automaticky zatvorí,
* nemusíme manuálne používať `file.close()`.

Všetko, čo je odsadené o 4 medzery, patrí do kontextového manažéra.

---

## Čítanie zo súboru

Na čítanie používame režim `"r"`.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    line = file.readline()
    print(line)
```

### Metódy na čítanie

* `read()` – načíta celý obsah súboru.
* `read(n)` – načíta konkrétny počet znakov.
* `readline()` – načíta jeden riadok.
* `readlines()` – načíta všetky riadky ako zoznam.

Príklad:

```python
with open("data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    print(lines)
```

---

## Cesty k súborom

### Absolútna cesta

Absolútna cesta začína od koreňa systému alebo disku.

```python
with open(r"C:\Users\User\Documents\Python_academy_skillmea\data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

### Relatívna cesta

Relatívna cesta je cesta vzhľadom na aktuálny priečinok projektu.

```python
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```

V projektoch je lepšie používať relatívne cesty, pretože projekt potom ľahšie funguje aj na inom počítači.

---

## Zápis do súboru

Na zápis používame režim `"w"`.

Režim `"w"`:

* vytvorí súbor, ak ešte neexistuje,
* prepíše celý obsah, ak súbor už existuje.

```python
with open("data.txt", "w", encoding="utf-8") as file:
    file.write("Hello, how are you?")
```

---

## Zápis viacerých riadkov

### Pomocou `writelines()`

```python
notes = [
    "Wash the dishes\n",
    "Do the homework\n",
    "Buy groceries\n"
]

with open("data.txt", "w", encoding="utf-8") as file:
    file.writelines(notes)
```

### Pomocou cyklu

```python
notes = ["Wash the dishes", "Do the homework", "Buy groceries"]

with open("data.txt", "w", encoding="utf-8") as file:
    for note in notes:
        file.write(note + "\n")
```

---

## Pridávanie na koniec súboru

Na pridanie textu na koniec súboru používame režim `"a"`.

Režim `"a"` zachová pôvodný obsah a nový text dopíše na koniec.

```python
with open("example.txt", "a", encoding="utf-8") as file:
    for number in range(10):
        file.write(str(number) + "\n")
```

---

## Vloženie textu na konkrétne miesto

Ak chceme vložiť text do stredu súboru, musíme:

1. načítať riadky zo súboru,
2. upraviť zoznam riadkov,
3. zapísať celý obsah späť do súboru.

```python
with open("data2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines.insert(5, "Janko Hrasko\n")

with open("data2.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print(lines)
```

Alternatíva pomocou skladania zoznamov:

```python
with open("data2.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

lines = lines[0:1] + ["Janko Hrasko\n"] + lines[1:]

with open("data2.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

print(lines)
```

---

## Ošetrenie neexistujúceho súboru

Ak sa pokúsime čítať súbor, ktorý neexistuje, vznikne chyba `FileNotFoundError`.

```python
try:
    with open("data3.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    print(lines)
except FileNotFoundError:
    print("Your file does not exist!")
```

---

## Vytvorenie súboru, ak neexistuje

```python
FILE_NAME = "notes3.txt"

def load_lines(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
    return lines

try:
    lines = load_lines(FILE_NAME)
except FileNotFoundError:
    print("I am creating a file")

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        file.write("")

    lines = load_lines(FILE_NAME)

print(lines)
```

Poznámka:

* Na čítanie používame `"r"`.
* Na zápis alebo vytvorenie súboru používame `"w"`.
* Pri `open()` je dobré uvádzať `encoding="utf-8"`.

---

# Moduly

## Čo je modul

Python modul je súbor s príponou `.py`, ktorý vieme použiť v inom Python súbore.

Moduly používame hlavne vtedy, keď:

* program začína byť dlhý,
* chceme oddeliť funkcie do samostatných súborov,
* chceme mať kód prehľadnejší,
* chceme opakovane používať rovnaký kód.

---

## Import celého modulu

Príklad súboru `maths.py`:

```python
PI = 3.14

def addition(a, b):
    return a + b
```

Použitie v inom súbore:

```python
import maths

print(maths.addition(10, 20))
print(maths.PI)
```

Pri tomto spôsobe používame názov modulu:

```python
maths.addition()
maths.PI
```

---

## Import konkrétnych vecí z modulu

```python
from maths import addition, PI

print(addition(10, 20))
print(PI)
```

Pri tomto spôsobe už nemusíme písať názov modulu pred funkciu alebo premennú.

---

## `__pycache__`

Pri importovaní modulov môže Python vytvoriť priečinok:

```text
__pycache__
```

Tento priečinok obsahuje súbory, ktoré Python používa na rýchlejšie spúšťanie programu.

Do GitHub repozitára sa priečinok `__pycache__` bežne nepridáva.

---

## Zhrnutie

V tomto webinári sme si precvičili:

* čítanie zo súboru,
* zápis do súboru,
* pridávanie textu na koniec súboru,
* úpravu obsahu súboru cez zoznam riadkov,
* ošetrenie chyby `FileNotFoundError`,
* vytvorenie vlastného modulu,
* import celého modulu,
* import konkrétnych funkcií alebo premenných z modulu.
