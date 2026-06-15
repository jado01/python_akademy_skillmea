# Webinar 16 - Advanced Functions, Dictionaries and Recursion

## Set

`set` je dátová štruktúra určená na uchovávanie jedinečných hodnôt.

Príklad:

```python
numbers = {1, 2, 3, 2, 1}
print(numbers)
```

Výstup:

```text
{1, 2, 3}
```

Duplicitné hodnoty sú automaticky odstránené.

---

## Interné funkcie

Ak funkcia začína podčiarkovníkom:

```python
def _prompt_note():
    pass
```

znamená to, že ide o internú funkciu.

Takéto funkcie:

* sú súčasťou modulu alebo balíka,
* nie sú určené na používanie zvonku,
* môžu sa v budúcnosti zmeniť.

Používajú sa najmä pri tvorbe knižníc.

---

## Type Hints

Type hints sú dostupné približne od Pythonu 3.6.

Slúžia ako napoveda typov.

Príklad:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Type hints:

* nie sú povinné,
* Python ich nekontroluje počas behu programu,
* zlepšujú čitateľnosť kódu,
* pomáhajú editorom a IDE.

Ak sa rozhodneme používať type hints, mali by sme ich používať konzistentne.

---

# Funkcie

## Pozicionálne a pomenované argumenty

Do funkcie môžeme posielať:

* pozicionálne argumenty,
* pomenované argumenty.

Príklad:

```python
print("Janko", "Hrasko", "Bratislava", sep="/")
```

Výstup:

```text
Janko/Hrasko/Bratislava
```

---

## *args

Pomocou jednej hviezdičky môžeme prijímať ľubovoľný počet nepomenovaných argumentov.

```python
def mean(*numbers):
    print(numbers)

mean(1, 2)
```

Výstup:

```text
(1, 2)
```

Praktický príklad:

```python
def mean(*numbers):
    return sum(numbers) / len(numbers)

print(mean(1, 2, 3, 1, 2, 3))
```

---

## **kwargs

Pomocou dvoch hviezdičiek môžeme prijímať ľubovoľný počet pomenovaných argumentov.

```python
def process_person(**kwargs):
    print(kwargs)

process_person(
    name="Janko",
    surname="Hrasko",
    address="Bratislava"
)
```

Výstup:

```python
{
    "name": "Janko",
    "surname": "Hrasko",
    "address": "Bratislava"
}
```

Prístup ku konkrétnemu argumentu:

```python
def process_person(**kwargs):
    print(kwargs["name"])
```

---

### Iterácia cez kwargs

```python
def process_person(**kwargs):
    for key in kwargs.keys():
        print(key)
```

---

### Kombinácia args a kwargs

```python
def process_person(*args, **kwargs):
    print(args)
    print(kwargs)

process_person(
    1, 2, 3, 4,
    name="Janko",
    surname="Hrasko"
)
```

### Poznámky

* `*args` = nepomenované argumenty
* `**kwargs` = pomenované argumenty
* nepomenované argumenty musia byť pred pomenovanými

---

# Dictionaries

## Spájanie slovníkov pomocou cyklu

```python
person = {}

for key in personal_data.keys():
    person[key] = personal_data[key]

for key in address_data.keys():
    person[key] = address_data[key]
```

---

## Spájanie slovníkov pomocou rozbalenia

Pomocou `**` vieme rozbaliť obsah slovníka.

```python
person = {
    **personal_data,
    **address_data,
    "is_good_person": True
}
```

Tento spôsob je kratší a čitateľnejší.

---

# Recursion

Rekurzia znamená, že funkcia volá samu seba.

Príklad:

```python
def visualise_recursion(l):
    if len(l) == 1:
        print(l[0])
        return

    print(l[0])
    visualise_recursion(l[1:])
    print("finish")
```

---

## Faktoriál pomocou cyklu

```python
x = 5

result = 1

for i in range(2, x + 1):
    result *= i

print(result)
```

---

## Faktoriál pomocou rekurzie

```python
def fact(n):
    if n == 1:
        return 1

    return n * fact(n - 1)

print(fact(5))
```

---

## Súčet čísel v zozname pomocou rekurzie

```python
def recursion_sum(numbers):
    if len(numbers) == 0:
        return 0

    return numbers[0] + recursion_sum(numbers[1:])

numbers = [1, 2, 3, 4]

print(recursion_sum(numbers))
```

---

## Fibonacciho postupnosť

Fibonacciho postupnosť je číselná postupnosť, v ktorej každé ďalšie číslo vznikne súčtom dvoch predchádzajúcich.

Príklad:

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Úloha:

Naprogramovať Fibonacciho postupnosť pomocou rekurzie.

---

# Poznámky z kontroly projektov

* používať malé a zrozumiteľné funkcie,
* preferovať `return` pred `print`,
* validovať vstupy používateľa,
* dbať na čitateľnosť kódu,
* pri väčších projektoch využívať type hints.
