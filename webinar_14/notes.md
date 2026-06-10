# Webinar 14 - Modules, Packages and Libraries

## Modules

### Import specific objects

```python
from maths import addition, PI
```

Importujeme iba konkrétne objekty z modulu.

---

### Import everything (not recommended)

```python
from maths import *
```

Použitím `*` importujeme všetko z modulu.

❌ Toto sa neodporúča používať:

* nevieme presne, čo sa importuje,
* môže dôjsť ku konfliktu názvov,
* autor modulu môže neskôr niečo zmeniť.

---

### Import with alias

Objekty z modulu si môžeme premenovať:

```python
from maths import addition as module_addition
from maths import PI as CUSTOM_PI
```

Príklad:

```python
from maths import addition as module_addition
from maths import PI as CUSTOM_PI

def addition(num1, num2):
    print("My addition")

print(module_addition(10, 20))
print(CUSTOM_PI)
```

---

### Import statements

Importy sa štandardne zapisujú na začiatok súboru.

Tým je kód prehľadnejší a všetky závislosti sú viditeľné na jednom mieste.

---

# Packages

Package (balík) je priečinok obsahujúci viac modulov, ktoré spolu logicky súvisia.

Príklad:

```python
from maths_utils.maths import addition, PI

print(addition(10, 20))
print(PI)
```

V tomto prípade:

* `maths_utils` je package,
* `maths.py` je modul,
* `addition` a `PI` sú objekty importované z modulu.

---

### Dlhé importy

Ak je import príliš dlhý, môžeme ho rozdeliť pomocou zátvoriek:

```python
from maths_utils import (
    addition,
    PI
)
```

---

### Poznámka k starším verziám Pythonu

V starších verziách Pythonu (3.7 a starších) musel package obsahovať súbor:

```text
__init__.py
```

V novších verziách to už nie je potrebné.

---

# Side Effects pri importe

Pri importe modulu sa vykoná celý kód, ktorý sa nachádza mimo funkcií.

Príklad:

### maths.py

```python
def addition(num1, num2):
    return num1 + num2

PI = 3.14

print(f"Hi from maths {__name__}")
```

### example.py

```python
from maths import addition, PI

print(addition(10, 20))
print(PI)
print(__name__)
```

Výstup:

```text
Hi from maths maths
30
3.14
__main__
```

Dôvod:

* `example.py` bol spustený priamo,
* `maths.py` bol spustený nepriamo cez import.

Preto:

```python
__name__
```

obsahuje:

```text
maths
```

a nie:

```text
__main__
```

---

## if **name** == "**main**"

Ak chceme spustiť časť kódu iba pri priamom spustení súboru, použijeme:

```python
if __name__ == "__main__":
```

Príklad:

```python
def addition(num1, num2):
    return num1 + num2

PI = 3.14

if __name__ == "__main__":
    print(f"Hi from maths {__name__}")
```

Tým zabránime neželanému vykonaniu kódu pri importe modulu.

---

# Library os

Knižnica `os` umožňuje pracovať s operačným systémom.

---

### Aktuálny adresár

```python
import os

print(os.getcwd())
```

Vráti aktuálny pracovný adresár.

---

### Výpis súborov a priečinkov

```python
import os

print(os.listdir(os.getcwd()))
```

Vypíše obsah aktuálneho adresára.

---

### Vytvorenie priečinka

```python
import os

os.makedirs(
    r"C:\Users\User\Documents\Python_academy_skillmea\NEW"
)
```

Vytvorí nový priečinok.

---

# PyPI

Oficiálny server Python balíkov:

https://pypi.org/

Odtiaľ môžeme inštalovať externé knižnice.

Príklady:

* matplotlib
* requests
* pandas
* numpy

---

# PIP

PIP = Python Install Package

Nástroj na inštaláciu externých balíkov.

---

### Verzia PIP

```bash
pip --version
```

---

### Zoznam nainštalovaných balíkov

```bash
pip list
```

---

# Príklad knižnice matplotlib

```python
import matplotlib.pyplot as plt

numbers = [
    1, 2, 3, 4, 5, 6, 7,
    0, 1, 2, 14, 55, 33,
    55, 55, 55, 67
]

plt.plot(numbers)
plt.show()
```

Knižnica matplotlib slúži na vytváranie grafov.

---

# Projekt č. 1 - Simple Notes Manager

Počas webinára sme si prešli zadanie projektu:

* Add Note
* List Notes
* Delete Note
* Exit

a rozobrali požadovanú funkcionalitu aplikácie.
# Webinar 14 - Modules, Packages and Libraries

## Modules

### Import specific objects

```python
from maths import addition, PI
```

Importujeme iba konkrétne objekty z modulu.

---

### Import everything (not recommended)

```python
from maths import *
```

Použitím `*` importujeme všetko z modulu.

❌ Toto sa neodporúča používať:

* nevieme presne, čo sa importuje,
* môže dôjsť ku konfliktu názvov,
* autor modulu môže neskôr niečo zmeniť.

---

### Import with alias

Objekty z modulu si môžeme premenovať:

```python
from maths import addition as module_addition
from maths import PI as CUSTOM_PI
```

Príklad:

```python
from maths import addition as module_addition
from maths import PI as CUSTOM_PI

def addition(num1, num2):
    print("My addition")

print(module_addition(10, 20))
print(CUSTOM_PI)
```

---

### Import statements

Importy sa štandardne zapisujú na začiatok súboru.

Tým je kód prehľadnejší a všetky závislosti sú viditeľné na jednom mieste.

---

# Packages

Package (balík) je priečinok obsahujúci viac modulov, ktoré spolu logicky súvisia.

Príklad:

```python
from maths_utils.maths import addition, PI

print(addition(10, 20))
print(PI)
```

V tomto prípade:

* `maths_utils` je package,
* `maths.py` je modul,
* `addition` a `PI` sú objekty importované z modulu.

---

### Dlhé importy

Ak je import príliš dlhý, môžeme ho rozdeliť pomocou zátvoriek:

```python
from maths_utils import (
    addition,
    PI
)
```

---

### Poznámka k starším verziám Pythonu

V starších verziách Pythonu (3.7 a starších) musel package obsahovať súbor:

```text
__init__.py
```

V novších verziách to už nie je potrebné.

---

# Side Effects pri importe

Pri importe modulu sa vykoná celý kód, ktorý sa nachádza mimo funkcií.

Príklad:

### maths.py

```python
def addition(num1, num2):
    return num1 + num2

PI = 3.14

print(f"Hi from maths {__name__}")
```

### example.py

```python
from maths import addition, PI

print(addition(10, 20))
print(PI)
print(__name__)
```

Výstup:

```text
Hi from maths maths
30
3.14
__main__
```

Dôvod:

* `example.py` bol spustený priamo,
* `maths.py` bol spustený nepriamo cez import.

Preto:

```python
__name__
```

obsahuje:

```text
maths
```

a nie:

```text
__main__
```

---

## if **name** == "**main**"

Ak chceme spustiť časť kódu iba pri priamom spustení súboru, použijeme:

```python
if __name__ == "__main__":
```

Príklad:

```python
def addition(num1, num2):
    return num1 + num2

PI = 3.14

if __name__ == "__main__":
    print(f"Hi from maths {__name__}")
```

Tým zabránime neželanému vykonaniu kódu pri importe modulu.

---

# Library os

Knižnica `os` umožňuje pracovať s operačným systémom.

---

### Aktuálny adresár

```python
import os

print(os.getcwd())
```

Vráti aktuálny pracovný adresár.

---

### Výpis súborov a priečinkov

```python
import os

print(os.listdir(os.getcwd()))
```

Vypíše obsah aktuálneho adresára.

---

### Vytvorenie priečinka

```python
import os

os.makedirs(
    r"C:\Users\User\Documents\Python_academy_skillmea\NEW"
)
```

Vytvorí nový priečinok.

---

# PyPI

Oficiálny server Python balíkov:

https://pypi.org/

Odtiaľ môžeme inštalovať externé knižnice.

Príklady:

* matplotlib
* requests
* pandas
* numpy

---

# PIP

PIP = Python Install Package

Nástroj na inštaláciu externých balíkov.

---

### Verzia PIP

```bash
pip --version
```

---

### Zoznam nainštalovaných balíkov

```bash
pip list
```

---

# Príklad knižnice matplotlib

```python
import matplotlib.pyplot as plt

numbers = [
    1, 2, 3, 4, 5, 6, 7,
    0, 1, 2, 14, 55, 33,
    55, 55, 55, 67
]

plt.plot(numbers)
plt.show()
```

Knižnica matplotlib slúži na vytváranie grafov.

---

# Projekt č. 1 - Simple Notes Manager

Počas webinára sme si prešli zadanie projektu:

* Add Note
* List Notes
* Delete Note
* Exit

a rozobrali požadovanú funkcionalitu aplikácie.
