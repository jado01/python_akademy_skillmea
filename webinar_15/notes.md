# Webinar 15 - Project Review and Best Practices

## Match Case

Alternatíva k dlhým `if/elif/else` blokom.

Príklad:

```python
choice = 2

match choice:
    case 1:
        print("Add note")
    case 2:
        print("List notes")
    case 3:
        print("Delete note")
    case _:
        print("Invalid choice")
```

### Poznámka

`match/case` funguje až od Pythonu 3.10.

Pri starších verziách Pythonu je potrebné použiť `if/elif/else`.

---

## Funkcie by mali vykonávať logiku

Nevytvárať funkcie, ktoré iba vypisujú text pomocou `print()`.

Lepšie je:

* spracovať údaje vo funkcii,
* vrátiť výsledok pomocou `return`,
* výpis riešiť v hlavnom programe.

---

## Side Effects

`print()` je vedľajší efekt (side effect).

Pri návrhu funkcií je často vhodnejšie použiť:

```python
return value
```

namiesto:

```python
print(value)
```

Výstup programu by mal byť ideálne oddelený od logiky programu.

---

## Validácia vstupu

Používateľský vstup by mal byť kontrolovaný.

Príklady:

* prázdny vstup,
* nesprávny formát,
* maximálna dĺžka textu.

Napríklad pri poznámkach môžeme obmedziť počet znakov, aby používateľ nezadal extrémne dlhý text.

---

## JSON

JSON = JavaScript Object Notation

Textový formát určený na ukladanie a prenos dát.

Vlastnosti:

* ľahko čitateľný pre človeka,
* ľahko spracovateľný programami,
* vhodný na štruktúrované údaje,
* veľmi podobný Python slovníkom (`dict`).

Príklad:

```json
{
    "id": 1,
    "note": "Buy milk",
    "important": true
}
```

JSON často obsahuje:

* objekty `{}`,
* polia `[]`.

---

## Pre-importovanie v package

Pri práci s balíkmi sa môže používať súbor:

```text
__init__.py
```

Tento súbor sa nachádza v priečinku package.

Môže byť aj prázdny, ale dá sa v ňom pripraviť jednoduchší import pre používateľa balíka.

Používa sa hlavne pri tvorbe väčších balíkov alebo knižníc, ktoré by sa neskôr mohli publikovať napríklad na PyPI.

V tomto kurze to zatiaľ nemusíme používať detailne.

---

## Action Dictionary

Action dictionary je spôsob, ako sa dá namiesto dlhého `if/elif/else` použiť slovník.

Kľúčom môže byť napríklad voľba používateľa a hodnotou môže byť funkcia, ktorá sa má vykonať.

Používa sa napríklad pri menu aplikácie.

Princíp:

```python
actions = {
    "1": add_note,
    "2": list_notes,
    "3": delete_note,
}
```

Používa sa najmä pri väčších menu programoch.

Tento koncept je pokročilejší a zatiaľ ho nie je potrebné používať v projekte, ak je jednoduchšie riešenie cez `if/elif/else` čitateľnejšie.

---

## Poznámky z kontroly projektu

* preferovať `return` pred `print`,
* validovať vstupy používateľa,
* písať malé a zrozumiteľné funkcie,
* oddeliť logiku programu od používateľského rozhrania,
* nepoužívať zbytočné funkcie, ktoré iba vypisujú text,
* myslieť na čitateľnosť a jednoduchú údržbu kódu.
# Webinar 15 - Project Review and Best Practices

## Match Case

Alternatíva k dlhým `if/elif/else` blokom.

Príklad:

```python
choice = 2

match choice:
    case 1:
        print("Add note")
    case 2:
        print("List notes")
    case 3:
        print("Delete note")
    case _:
        print("Invalid choice")
```

### Poznámka

`match/case` funguje až od Pythonu 3.10.

Pri starších verziách Pythonu je potrebné použiť `if/elif/else`.

---

## Funkcie by mali vykonávať logiku

Nevytvárať funkcie, ktoré iba vypisujú text pomocou `print()`.

Lepšie je:

* spracovať údaje vo funkcii,
* vrátiť výsledok pomocou `return`,
* výpis riešiť v hlavnom programe.

---

## Side Effects

`print()` je vedľajší efekt (side effect).

Pri návrhu funkcií je často vhodnejšie použiť:

```python
return value
```

namiesto:

```python
print(value)
```

Výstup programu by mal byť ideálne oddelený od logiky programu.

---

## Validácia vstupu

Používateľský vstup by mal byť kontrolovaný.

Príklady:

* prázdny vstup,
* nesprávny formát,
* maximálna dĺžka textu.

Napríklad pri poznámkach môžeme obmedziť počet znakov, aby používateľ nezadal extrémne dlhý text.

---

## JSON

JSON = JavaScript Object Notation

Textový formát určený na ukladanie a prenos dát.

Vlastnosti:

* ľahko čitateľný pre človeka,
* ľahko spracovateľný programami,
* vhodný na štruktúrované údaje,
* veľmi podobný Python slovníkom (`dict`).

Príklad:

```json
{
    "id": 1,
    "note": "Buy milk",
    "important": true
}
```

JSON často obsahuje:

* objekty `{}`,
* polia `[]`.

---

## Pre-importovanie v package

Pri práci s balíkmi sa môže používať súbor:

```text
__init__.py
```

Tento súbor sa nachádza v priečinku package.

Môže byť aj prázdny, ale dá sa v ňom pripraviť jednoduchší import pre používateľa balíka.

Používa sa hlavne pri tvorbe väčších balíkov alebo knižníc, ktoré by sa neskôr mohli publikovať napríklad na PyPI.

V tomto kurze to zatiaľ nemusíme používať detailne.

---

## Action Dictionary

Action dictionary je spôsob, ako sa dá namiesto dlhého `if/elif/else` použiť slovník.

Kľúčom môže byť napríklad voľba používateľa a hodnotou môže byť funkcia, ktorá sa má vykonať.

Používa sa napríklad pri menu aplikácie.

Princíp:

```python
actions = {
    "1": add_note,
    "2": list_notes,
    "3": delete_note,
}
```

Používa sa najmä pri väčších menu programoch.

Tento koncept je pokročilejší a zatiaľ ho nie je potrebné používať v projekte, ak je jednoduchšie riešenie cez `if/elif/else` čitateľnejšie.

---

## Poznámky z kontroly projektu

* preferovať `return` pred `print`,
* validovať vstupy používateľa,
* písať malé a zrozumiteľné funkcie,
* oddeliť logiku programu od používateľského rozhrania,
* nepoužívať zbytočné funkcie, ktoré iba vypisujú text,
* myslieť na čitateľnosť a jednoduchú údržbu kódu.
# Webinar 15 - Project Review and Best Practices

## Match Case

Alternatíva k dlhým `if/elif/else` blokom.

Príklad:

```python
choice = 2

match choice:
    case 1:
        print("Add note")
    case 2:
        print("List notes")
    case 3:
        print("Delete note")
    case _:
        print("Invalid choice")
```

### Poznámka

`match/case` funguje až od Pythonu 3.10.

Pri starších verziách Pythonu je potrebné použiť `if/elif/else`.

---

## Funkcie by mali vykonávať logiku

Nevytvárať funkcie, ktoré iba vypisujú text pomocou `print()`.

Lepšie je:

* spracovať údaje vo funkcii,
* vrátiť výsledok pomocou `return`,
* výpis riešiť v hlavnom programe.

---

## Side Effects

`print()` je vedľajší efekt (side effect).

Pri návrhu funkcií je často vhodnejšie použiť:

```python
return value
```

namiesto:

```python
print(value)
```

Výstup programu by mal byť ideálne oddelený od logiky programu.

---

## Validácia vstupu

Používateľský vstup by mal byť kontrolovaný.

Príklady:

* prázdny vstup,
* nesprávny formát,
* maximálna dĺžka textu.

Napríklad pri poznámkach môžeme obmedziť počet znakov, aby používateľ nezadal extrémne dlhý text.

---

## JSON

JSON = JavaScript Object Notation

Textový formát určený na ukladanie a prenos dát.

Vlastnosti:

* ľahko čitateľný pre človeka,
* ľahko spracovateľný programami,
* vhodný na štruktúrované údaje,
* veľmi podobný Python slovníkom (`dict`).

Príklad:

```json
{
    "id": 1,
    "note": "Buy milk",
    "important": true
}
```

JSON často obsahuje:

* objekty `{}`,
* polia `[]`.

---

## Pre-importovanie v package

Pri práci s balíkmi sa môže používať súbor:

```text
__init__.py
```

Tento súbor sa nachádza v priečinku package.

Môže byť aj prázdny, ale dá sa v ňom pripraviť jednoduchší import pre používateľa balíka.

Používa sa hlavne pri tvorbe väčších balíkov alebo knižníc, ktoré by sa neskôr mohli publikovať napríklad na PyPI.

V tomto kurze to zatiaľ nemusíme používať detailne.

---

## Action Dictionary

Action dictionary je spôsob, ako sa dá namiesto dlhého `if/elif/else` použiť slovník.

Kľúčom môže byť napríklad voľba používateľa a hodnotou môže byť funkcia, ktorá sa má vykonať.

Používa sa napríklad pri menu aplikácie.

Princíp:

```python
actions = {
    "1": add_note,
    "2": list_notes,
    "3": delete_note,
}
```

Používa sa najmä pri väčších menu programoch.

Tento koncept je pokročilejší a zatiaľ ho nie je potrebné používať v projekte, ak je jednoduchšie riešenie cez `if/elif/else` čitateľnejšie.

---

## Poznámky z kontroly projektu

* preferovať `return` pred `print`,
* validovať vstupy používateľa,
* písať malé a zrozumiteľné funkcie,
* oddeliť logiku programu od používateľského rozhrania,
* nepoužívať zbytočné funkcie, ktoré iba vypisujú text,
* myslieť na čitateľnosť a jednoduchú údržbu kódu.
