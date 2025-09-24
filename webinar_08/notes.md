# Webinár 8 – While cykly, break, continue, komentáre (2025-09-19)

## Obsah
- Cyklus `while`
- Nekonečný cyklus
- Príkaz `break`
- Príkaz `continue`
- Komentáre v Pythone
- Úlohy

---

## While cyklus
Cyklus `while` opakuje blok kódu, kým je podmienka pravdivá.

```python
counter = 0

while counter < 5:
    print("Doors are open")
    counter += 1
print("Doors are closed")
```
## Nekonečný cyklus
Na vytvorenie nekonečného cyklu použijeme while True:.
Zastaviť sa dá ručne v termináli kombináciou CTRL+C.

```python
while True:
    print("Server is up")
```
## Príkaz break
break slúži na okamžité ukončenie cyklu zvnútra.

```python
counter = 0

while True:
    print("Server is up")
    counter += 1
    if counter > 4:
        break

print("Server is down")
```
break vieme použiť aj vo for cykle:

```python
for number in range(1, 21):
    if number == 5:
        break
    print(number)
```
## Príkaz continue
continue preskočí zvyšok cyklu a pokračuje ďalšou iteráciou.

```python
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)
```

Môžeme kombinovať continue aj break:

```python
for number in range(1, 12):
    if number % 2 == 0:
        continue
    if number > 7:
        break
    print(number)
```
## omentáre
Jednoriadkový komentár: začína znakom #
Viacriadkový komentár: môžeme použiť trojité úvodzovky """ ... """

```python
# Toto je komentár

"""
Toto je viacriadkový komentár
ktorý sa nevyhodnotí
"""
```
💡 Tipy v editore (VS Code):
- CTRL + / → zakomentuje/odkomentuje označené riadky
- CTRL + ] alebo CTRL + [ → posun odsadenia kódu doprava/doľava

## Úlohy
- Skúsiť vyriešiť zadania raz s for cyklom, raz s while cyklom.
- Zadania sú rozdelené do dvoch sád:
    - Set1: základné úlohy s cyklami, podmienkami, poľami a reťazcami
    - Set2: pokročilejšie úlohy s vnorenými cyklami a pyramídami

---
