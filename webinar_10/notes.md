# Webinár 10 – Tuples, mutability a funkcie (2025-10-??)

## Obsah
- Mutable vs Immutable typy
- Tuples (n-tice)
- Funkcie: definícia, návratové hodnoty, default parametre
- Scope (lokálne vs globálne premenné)

---

## Tuples (n-tice)
- Podobné zoznamom, ale **nemenné (immutable)**.
- Vytvárajú sa okrúhlymi zátvorkami `()` alebo aj bez nich (packing/unpacking).
- Indexovanie funguje ako pri listoch.

```python
person = ("Ján", 35, "Slovensko")
print(person[0])  # Ján
print(person[2])  # Slovensko
```
Kedy použiť:
- Keď sa dáta nemajú meniť (napr. súradnice, RGB, dátum).
- Ako kľúč v dict (tuple je hashovateľný, list nie).

Packing / unpacking:
x = (1, 2, 3)
# rovnaké ako x = 1, 2, 3

a, b, c = x
print(a, b, c)  # 1 2 3

## Funkcie

def greet_nicely():  - funkcia s nazvom ktora nema este zatial ziadnu funkciu

    def - definovanie funkcie
    greet_nicely - meno funkcie
    : - funkciu ukoncujem dvojbotkou

```python
def greet_nicely(): # funkcia s nazvom ktora nema este zatial ziadnu funkciu
    print("Hello")
    print("World!")

greet_nicely()
```
**Premenné vo vnútri funkcie (lokálny scope):**

- v tele funkcie si vieme definovat vlastne premenne, tu potom nevieme pouzit mimo funkcie
```python
def custom_sum(num1, num2):
    sumation = num1 + num2
    print(sumation)

custom_sum(12, 20)
```

- navratova hodnota return:

```python
 def custom_sum(num1, num2):
    sumation = num1 + num2
    return sumation		#navratova funckia

x = custom_sum(12, 20)
print(x)
```
- Viac návratových hodnôt (vráti sa tuple):
```python
def custom_calculator(num1, num2):
    summation = num1 + num2
    difference = num1 - num2
    return summation, difference

pair = custom_calculator(12, 20)
print(pair)  # (32, -8)

summation, difference = custom_calculator(12, 20)
print(summation, difference)  # 32 -8
```
- Default parametre:
```python
def multiply_number_by_x(num, x=10):
    return num * x

print(multiply_number_by_x(10))    # 100
print(multiply_number_by_x(10, 2)) # 20
```
- Pozor na mutability:
```python
def magic_box_scalar(x):
    x += 1           # int je immutable → mimo funkcie sa nezmení
    return x

v = 2
magic_box_scalar(v)
print(v)  # 2

def magic_box_list(x):
    x += [4]         # list je mutable → zmení sa aj „vonku“
    return x

arr = [1, 2, 3]
magic_box_list(arr)
print(arr)  # [1, 2, 3, 4]
```
- Vnorovanie volaní:
```python
def custom_sum(a, b):
    return a + b

print(custom_sum(1, custom_sum(1, 3)))  # 5
```
- Sumovanie zoznamu:
```python
def sum_list(numbers):
    result = 0
    for number in numbers:
        result += number
    return result

numbers = [1, 2, 3, 4, 5]
print(sum_list(numbers))  # 15
```
**Scope (lokálny vs globálny)**
```python
x = 10  # globálna premenná

def plus_global(number):
    return number + x

print(plus_global(20))  # 30
```
- Lokálne „prekrytie“ globálnej:
```python
x = 10

def plus_local(number):
    x = 30              # lokálne „prebije“ globálne x v rámci funkcie
    return number + x

print(plus_local(20))   # 50
print(x)                # 10 (globálna hodnota ostala)
```
## Úlohy na precvičenie

1. Napíš funkciu min_max_tuple(nums), ktorá vráti dvojicu (min, max) bez použitia min()/max().
2. Napíš funkciu safe_append(items, value):
    - ak items je None, pracuj s novým prázdnym zoznamom,
    - inak pridaj value do existujúceho zoznamu,
    - vráť výsledný zoznam. (Tréning na mutability a default argumenty.)
3. Vytvor tuple rgb = (r, g, b) a rozbaľ ho do troch premenných; vypíš ich.
