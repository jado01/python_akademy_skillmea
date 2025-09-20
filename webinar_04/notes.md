# Webinár 4 – Logické spojky a Rubber Duck Debugging (2025-09-12)

## Obsah
- Rubber Duck Debugging
- Logické spojky: `and`, `or`, `xor`, `not`
- Komutatívny zákon
- Stringy (reťazce) a základné operácie
- Castovanie typov (`str()`, `int()`, `float()`)
- Operátory na stringoch (`*`)
- Funkcia `len()`
- Indexovanie a slicing reťazcov
- Logické tabuľky (pravdivostné tabuľky)
- Operátor `xor` (exkluzívne alebo)

## Poznámky
- **Rubber Duck Debugging**:
  - technika hľadania chýb → vysvetľuj svoj kód nahlas (ako keby si to vysvetľoval kačičke)
  - pomáha, lebo sa donútiš myslieť krok za krokom
  - pomáha nájsť chyby
- **Logické spojky**:
  - `and` – výsledok je True, iba ak sú obidve podmienky True
  - `or` – výsledok je True, ak je aspoň jedna podmienka True
  - `xor` – výsledok je True, ak je presne jedna podmienka True (v Pythone: `!=` alebo `bool(a) ^ bool(b)`)
- **Pravdivostné tabuľky**:

### `and`
| A     | B     | A and B |
|-------|-------|----------|
| True  | True  | True     |
| True  | False | False    |
| False | True  | False    |
| False | False | False    |

### `or`
| A     | B     | A or B  |
|-------|-------|---------|
| True  | True  | True    |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### `xor`
| A     | B     | A xor B |
|-------|-------|---------|
| True  | True  | False   |
| True  | False | True    |
| False | True  | True    |
| False | False | False   |

### `not`
|A  |B  |
|---|---|
| 0 | 1 |
| 1 | 0 |
- **Komutatívny zákon** – pri `and` a `or` nezáleží na poradí:
  - `A and B == B and A`
  - `A or B == B or A`
- **String** – postupnosť znakov:
  - zapisujeme do `"dvojitých"` alebo `'jednoduchých'` úvodzoviek
- **Castovanie** (pretypovanie):
  ```python
  cislo = 3
  text = str(cislo)  # "3"
  ```
- **Operátor "*" na stringoch**:
  ```python
  meno = "Ján"
  print(meno * 3)   # JánJánJán
  ```
  - funguje iba string * integer, nie string * float
- **Funkcia len() - vvráti počet prvkov**:
  ```python
  meno = "miso"
  print(len(meno))  # 4
  ```
- **Indexovanie**:
  ```python
  meno = "miso"
  print(meno[1])   # i
  ```
- **Slicing**:
  ```python
  meno = "miso"
  print(meno[0:2])   # mi
  print(meno[:2])    # mi
  print(meno[-3:-1]) # is
  print(meno[-2:])   # so
  ```
  - horná hranica je otvorený interval (nezahrnie ju)
  - ak horná hranica presahuje dĺžku stringu, Python to zvládne bez chyby


## Úlohy
- **Ulohy webinar č.4**:
1. Z retazcov do viet
Vytvor tri premenne:
meno = "Jakub"
vek = 13
mesto = "Nitra"
Pouzi ich na vytvorenie a vypisanie tejto vety:
Jakub ma 13 rokov a byva v meste Nitra.
(Pouzi bud spajanie retazcov alebo f-string.)
2. Jednoduchy kalkulator
Uloz dve cisla do premennych:
a = 10
b = 4
Spocitaj a vypis:
- Sucet
- Rozdiel
- Sucin
- Podiel
Bonus: Zaobli podiel na 2 desatinne miesta pomocou round().
3. Prva a posledna hlaska
Uloz do premennej meno:
meno = "Veronika"
Vypis:
- Prvy znak mena
- Posledny znak mena
(Pouzi indexovanie: meno[0], meno[-1])
4. Priemer znamok
Zadaj 3 znamky do premennych a vypocitaj priemer:
znamka1 = 2
znamka2 = 1
znamka3 = 2
Vystup:
Priemer znamok je: 1.67
(Zaobli vystup na 2 desatinne miesta.)
5. Veta s opakovanim
Vytvor premennu:
slovo = "hej "
Opakuj ju 5-krat a vypis vysledok:
hej hej hej hej hej
6. Jednoduchy preklad do velkych pismen
Do premennej `slovo` vloz lubovolne slovo a vypis ho velkymi pismenami:
slovo = "programovanie"
Pouzi:
print(slovo.upper())

- **Dodatočné úlohy od AI**:
7. Vyskúšať logické operátory `and`, `or`, `not` na rôznych hodnotách.
8. Vytvor malú funkciu, ktorá implementuje `xor` (vracia True, ak je práve jedna podmienka True).
9. Pretypuj číslo na string a vypíš ho spolu s textom.
10. Použi `*` na opakovanie stringu 3×.
11. Použi `len()` na zistenie dĺžky textu.
12. Skús indexovanie a slicing na rôznych reťazcoch.
13. Skús vysvetliť svoj kód „gumenej kačičke“ – či už reálne alebo len nahlas.
