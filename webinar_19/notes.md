# Webinar 19 – Class Attributes a Class Methods

## Class Attribute (atribút triedy)

Class atribút:

* patrí triede, nie objektu
* existuje iba raz pre celú triedu
* všetky objekty ho zdieľajú
* vieme k nemu pristupovať cez triedu aj cez objekt

Príklad:

```python
class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand
```

Vytvorenie objektov:

```python
c1 = Car("Mercedes")
c2 = Car("Volkswagen")
```

Prístup k atribútu:

```python
print(c1.number_of_wheels)
print(c2.number_of_wheels)
print(Car.number_of_wheels)
```

Výstup:

```text
4
4
4
```

---

## Class Attribute vs Instance Attribute

### Class Attribute

```python
number_of_wheels = 4
```

* spoločný pre všetky objekty
* uložený na úrovni triedy

### Instance Attribute

```python
self.brand = brand
```

* každý objekt má vlastnú hodnotu

Príklad:

```python
c1 = Car("Mercedes")
c2 = Car("Volkswagen")
```

```text
c1.brand -> Mercedes
c2.brand -> Volkswagen
```

---

## Špeciálny atribút **dict**

Každý objekt obsahuje slovník svojich atribútov.

```python
print(c1.__dict__)
```

Výstup:

```python
{'brand': 'Mercedes'}
```

Obsahuje iba atribúty objektu.

---

### Atribúty triedy

Prístup k atribútom triedy:

```python
print(c1.__class__.__dict__)
```

Obsahuje:

* class atribúty
* metódy
* interné veci Pythonu

---

## Zmena atribútu na úrovni objektu

```python
c1.number_of_wheels = 3
```

Vznikne nový atribút iba pre objekt `c1`.

```python
print(c1.number_of_wheels)
print(c2.number_of_wheels)
print(Car.number_of_wheels)
```

Výstup:

```text
3
4
4
```

---

## Zmena atribútu na úrovni triedy

```python
Car.number_of_wheels = 5
```

Výstup:

```text
3
5
5
```

Poznámka:

Objekt `c1` zostane na hodnote 3, pretože má vlastný instance atribút.

---

# Pozor na Mutable Data Types

Nevhodné:

```python
class Bag:
    items = []
```

Všetky objekty používajú ten istý zoznam.

```python
b1 = Bag()
b2 = Bag()

b1.items.append("apple")
```

Výstup:

```python
print(b1.items)
print(b2.items)
print(Bag.items)
```

```text
['apple']
['apple']
['apple']
```

Problém:

```text
zmena na jednom mieste
=
zmena všade
```

Pre zoznamy, slovníky a sety používame radšej instance atribúty v `__init__()`.

---

# Praktické použitie Class Attributes

Počítanie vytvorených objektov:

```python
class DBClient:
    instances_created = 0

    def __init__(self, url):
        self.url = url

        if DBClient.instances_created >= 2:
            print("Sorry, too many connections")
            return

        DBClient.instances_created += 1
```

Použitie:

```python
c1 = DBClient("url1")
c2 = DBClient("url2")

print(DBClient.instances_created)
```

Výstup:

```text
2
```

---

# Instance Methods (metódy inštancie)

Najčastejší typ metódy.

Prvý parameter:

```python
self
```

`self` predstavuje konkrétny objekt.

Príklad:

```python
class Car:
    def __init__(self, brand):
        self.brand = brand

    def wrm(self):
        print(f"Wrm {self.brand}")
```

Použitie:

```python
c1 = Car("Mercedes")

c1.wrm()
```

Výstup:

```text
Wrm Mercedes
```

Každý objekt dostane vlastné `self`.

---

# Class Methods

Class method sa viaže na triedu.

Používa dekorátor:

```python
@classmethod
```

Namiesto `self` používa:

```python
cls
```

`cls` odkazuje na triedu.

Má prístup:

* ku class atribútom
* nemá prístup k instance atribútom

---

Príklad:

```python
class Car:
    number_of_wheels = 4

    def __init__(self, brand):
        self.brand = brand

    @classmethod
    def print_wheels(cls):
        print(cls.number_of_wheels)
```

Volanie:

```python
Car.print_wheels()
```

Výstup:

```text
4
```

---

# Praktický príklad Class Method

Konverzia teploty.

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        c = (fahrenheit - 32) * 5 / 9
        return cls(c)
```

Použitie:

```python
t1 = Temperature(25)

print(t1.to_fahrenheit())
```

Výstup:

```text
77.0
```

---

Vytvorenie objektu pomocou class method:

```python
t2 = Temperature.from_fahrenheit(77)

print(t2.celsius)
```

Výstup:

```text
25.0
```

---

# Zapamätať si

## self

```text
odkaz na objekt
```

Používa sa v instance metódach.

---

## cls

```text
odkaz na triedu
```

Používa sa v class metódach.

---

## Kedy použiť class attribute

* spoločná hodnota pre všetky objekty
* počítadlá
* konfigurácia
* konštanty

Príklady:

```python
number_of_wheels = 4
instances_created = 0
```

---

# Domáca úloha

Vytvoriť aspoň jednu vlastnú `@classmethod`.

Napríklad:

* SmartBulb
* Bike
* Person
* Temperature

a vyskúšať vytvorenie objektu pomocou class method.
