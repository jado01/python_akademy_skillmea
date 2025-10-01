# Webinár 11 – Dictionaries (slovníky) (2025-10-??)

## Obsah
- Základné vlastnosti dictionary
- Vnorené slovníky a zoznamy slovníkov
- Mutable povaha dictionary
- Vytváranie cez `dict()`
- Práca s kľúčmi (`[]`, `get`)
- Odstraňovanie (`del`, `pop`, `clear`)
- Iterovanie cez kľúče, hodnoty a páry

## Examples
- `01_basic_dict.py` – základné operácie so slovníkom (prístup, zmena, pridanie kľúča)
- `02_nested_dict.py` – vnorený slovník a prístup k vnoreným hodnotám
- `03_iterating_dict.py` – rôzne spôsoby iterovania cez dictionary

---

## Dictionary – základ
- Používajú sa zložené zátvorky `{}`.
- Každý prvok má **kľúč → hodnotu**.
- Kľúč musí byť **immutable** (napr. string, číslo, tuple).
- Hodnota môže byť čokoľvek (immutable aj mutable).

```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
}
print(person)
```
- viem vytvarat aj polia s viacerimi dictionary
- tu i viem vypisat vsetko naraz
- viem pristupovat ku konkretnemu slovniku a aj ku hodnote v slovniku

**Zoznamy slovnikov**
```python
students = [
    {"name": "Miso", "age": 29},
    {"name": "Janko", "age": 31},
]

print(students)
print(students[0])
print(students[1]["name"])
```
**Vnorený slovník**
```python
person = {
    "name": "Janko",
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04",
    },
}
print(person["adress"]["street"])
```
**Mutable povaha slovníka**
```python
person = {"name": "Janko", "surname": "Hrasko"}
person["name"] = "Janka"  # zmena hodnoty
print(person)
```
- dictionary je sam o sebe mutable typ, mozme ho zvacsovat a zmensovat, vieme v nom menit veci
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

person["name"] = "Janka"

print(person)
print(person["adress"]["street"])
```
**Vytváranie cez dict()**
```python
person1 = dict(name="Miso", age=29)
person2 = dict([("name", "Bob"), ("age", 24)])  # zoznam tuple dvojíc
print(person1)
print(person2)
```
- dictionary vieme robit aj cez konstruktor dict
	-	tento konstruktor je trochu obmedzeny pretoze argumenty budu vzdy reprezentovane ako string
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

person1 = dict(name = "Miso", age =29)
person2 = dict([("name", "Bob"), ("age", 24)])		#pole taplov, kde tapla ma 2 hodnoty, kluc a hodnotu

print(person1)
print(person2)
```
**Bezpečný prístup cez .get()**
```python
pokemons = {}
print(pokemons.get("pikachu", "Is not there"))
```
- funkcia get - ak chceme nieco z dictionary a to tam nie je tak nam tao vypise chybu ak pouzivame  hranate zatvorky, ak pouzije funkciu get tak to nezahlasi chybu ale napise none, vieme pouzit vp funkcii get aj druhy parameter, ktory vrati hodnotu ak ten kluc neexistuje
```python
person1 = dict(name = "Miso", age =29)
person2 = dict([("name", "Bob"), ("age", 24)])

pokemons = {}

print(pokemons.get("pikachu", "Is not there"))
```
**Odstraňovanie kľúčov**
```python
person = {"name": "Janko", "surname": "Hrasko"}

del person["name"]
x = person.pop("surname")  # vymaže a zároveň vráti
print(person)
print(x)

person.clear()  # vymaže všetko
print(person)   # {}
```
- del, pop, clear

```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

del person["name"]  #vymaze name
x = person.pop("surname")   #vymaze ale vie aj popnut, takze teraz bude surname v x
print(person)
print(x)
person.clear()  #vymaze cely dictionary
print(person)
```
**Iterovanie cez dictionary**
- len kluce
```python
for key in person:
    print(key)
```
- Kľúč + hodnota
```python
for key in person:
    print(f"key -> {key}, value -> {person[key]}")
```
- len hodnoty
```python
for value in person.values():
    print(value)
```
- Páry (ako tuple)
```python
for x in person.items():
    print(x)  # (key, value)
```
- Rozbalenie tuple
```python
for key, value in person.items():
    print(key, value)
```
 - ked chceme iterovat cez dictionary:
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

for key in person:
    print(key)
```
---
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

for key in person:
    print(f"kez -> {key}, value -> {person[key]}")
```
---
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

for value in person.values():
    print(value)
```
---
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

for x in person.items():    #items vrati tuples, kde prvy items tuple je kluc a druhy hodnota
    print(x)				# items iteruje cez pary a vracia cez tuple
```
---
```python
person = {
    "name": "Janko",
    "surname": "Hrasko",
    123: "Ahoj",
    12.3: "Janko Hrasko",
    "123": "Miso",
    (1, 2, 3): [1, 2, 3, 4],
    "adress": {
        "street": "Ulicova",
        "street number": 12,
        "postal code": "821 04"
    },
}

for key, value in person.items():	# tuple vieme rozbalit do premennych
    print(key, value)
```
---
