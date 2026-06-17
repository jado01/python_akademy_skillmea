# Webinar 17 - List Comprehensions, Generators, Lambda, Map/Filter/Reduce

## List Comprehension

List comprehension je skrátený zápis na vytváranie zoznamov.

Klasický zápis:

```python
result = []

for num in range(1, 20):
    if num % 2 == 0:
        result.append(num)
```

Pomocou list comprehension:

```python
result = [num for num in range(1, 20) if num % 2 == 0]
```

### Syntax

```python
[new_value for item in iterable if condition]
```

### Použitie else

Ak chceme použiť aj `else`, podmienka musí byť pred cyklom:

```python
result = [num if num % 2 == 0 else -num for num in range(1, 20)]
```

---

## Generators

Generator je špeciálny typ funkcie, ktorý používa kľúčové slovo `yield`.

```python
def count_to(n):
    i = 1

    while i < n:
        yield i
        i += 1
```

### Vlastnosti

* `yield` premení funkciu na generator
* generator si pamätá svoj stav
* hodnoty generuje postupne
* neukladá všetky hodnoty do pamäte naraz
* po vyčerpaní vyvolá `StopIteration`

Použitie:

```python
g = count_to(3)

print(next(g))
print(next(g))
```

### Výhody

Generatory sú vhodné pri práci s veľkými dátami, pretože nezaťažujú RAM vytvorením celého zoznamu naraz.

Príklad čítania súboru:

```python
def read_numbers(path):
    with open(path, "r") as f:
        for line in f:
            yield int(line.strip())
```

### Generator expression

List comprehension:

```python
numbers = [x for x in range(10)]
```

Generator:

```python
numbers = (x for x in range(10))
```

Rozdiel:

* list vytvorí všetky hodnoty naraz
* generator vytvára hodnoty postupne

---

## Lambda Functions

Lambda je anonymná (nepomenovaná) funkcia.

Klasická funkcia:

```python
def square(num):
    return num * num
```

Lambda verzia:

```python
lambda num: num * num
```

### Syntax

```python
lambda arguments: expression
```

Obmedzenie:

* môže obsahovať iba jeden výraz
* výsledok sa automaticky vracia (`return` netreba)

---

## map()

Aplikuje funkciu na všetky prvky kolekcie.

```python
numbers = [2, 3, 4, 5, 6]

list(map(lambda num: num * num, numbers))
```

Výsledok:

```python
[4, 9, 16, 25, 36]
```

---

## filter()

Filtruje prvky podľa podmienky.

```python
list(filter(lambda num: num % 2 == 0, numbers))
```

Výsledok:

```python
[2, 4, 6]
```

Funkcia použitá vo `filter()` musí vracať:

```python
True
```

alebo

```python
False
```

---

## reduce()

Funkcia `reduce()` nie je vstavaná, treba ju importovať:

```python
from functools import reduce
```

Slúži na zredukovanie celej kolekcie na jednu hodnotu.

```python
reduce(lambda a, b: a + b, numbers)
```

Výsledok:

```python
20
```

---

## Functional Programming

Funkcie:

* `map()`
* `filter()`
* `reduce()`

sú súčasťou konceptu funkcionálneho programovania.

Myšlienka:

> Program sa skladá z funkcií a transformácií dát namiesto menenia stavu programu.
