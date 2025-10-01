# Webinár 12 – Exceptions a práca so súbormi (2025-09-26)

## Exceptions – výnimky
- Výnimka = chyba počas behu programu.
- Pomocou `try/except` vieme zabrániť pádu programu a ošetriť chybu.
- Ak nastane chyba vo vnútri `try`, kód preskočí do `except`.

### Príklad:
```python
num1 = 10
num2 = 1

try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print("You are trying to divide by 0")
```
- as e → uloží detail chyby do premennej e.
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
```
- Chybu vieme aj vyvolať manuálne pomocou raise.
```python
def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return num1 / num2
```
**File handling – práca so súbormi**

1. Otváranie súboru
    - open("data.txt", "r") – otvorí súbor na čítanie
    - file.close() – treba zatvoriť súbor
2. Čítanie obsahu
    - file.read() – prečíta celý obsah
    - file.read(n) – prečíta n znakov
    - file.readline() – načíta 1 riadok
    - file.readlines() – načíta všetky riadky ako zoznam
```python
file = open("data.txt", "r")
text = file.read()
print(text)
file.close()
```
**Súvislosť s projektom**

Poznámky budú uložené v súbore notes.txt.
Každá poznámka môže byť reprezentovaná ako dictionary (date, note, important).
Serializácia = uloženie dát na disk, tu zatiaľ formou textu.
