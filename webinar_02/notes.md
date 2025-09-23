# Webinár 2 – Premenné a dátové typy (2025-09-05)

## Obsah
- Premenné a priradenie hodnôt
- Základné dátové typy v Pythone
  - čísla (`int`, `float`)
  - reťazce (`str`)
  - logické hodnoty (`bool`)
- Operátory
  - aritmetické: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - porovnávacie: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - logické: `and`, `or`, `not`

## Poznámky
- Premenná sa vytvorí priradením:
  ```python
  x = 10
  meno = "Ján"
  ```

- Python rozlišuje typ automaticky → nemusím ho písať (`dynamické typovanie`).
- Premenné môžem pretypovať:
  ```python
  x = int("5")   # "5" -> 5
  y = str(10)    # 10 -> "10"
  ```

- Reťazce (str) sú texty v úvodzovkách:
  text = "Ahoj"
- Funkcia type() vráti dátový typ premennej:
  print(type(x))   # <class 'int'>

## Úlohy

1. Vytvoriť premennú vek a priradiť jej svoju hodnotu.
   Vypísať: „Mám X rokov“.

2. Vytvoriť dve čísla a vypočítať ich súčet, rozdiel, súčin a podiel.

3. Skúsiť pretypovať int na str a opačne.

4. Skúsiť porovnávacie operátory (napr. 5 > 3, 5 == 10).

5. Skombinovať logické operátory (and, or, not) v podmienkach.