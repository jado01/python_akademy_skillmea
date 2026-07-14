# Webinar 22 – Špeciálne metódy, abstraktné triedy, `__slots__` a UML

## Špeciálne metódy

Špeciálne metódy, označované aj ako **dunder metódy**, majú na začiatku aj na konci názvu dve podčiarkovníky.

Príklady:

```python
__init__()
__str__()
__add__()
__eq__()
```

Python ich automaticky volá pri určitých operáciách.

Napríklad:

```python
vector1 + vector2
```

môže zavolať:

```python
vector1.__add__(vector2)
```

Vďaka špeciálnym metódam môžeme určiť, ako sa majú objekty vlastných tried správať pri:

- matematických operáciách,
- porovnávaní,
- prevode na reťazec,
- použití v podmienkach,
- ďalších vstavaných operáciách Pythonu.

Tento mechanizmus sa nazýva **operator overloading**, teda preťažovanie operátorov.

---

# Metóda `__add__()`

Metóda `__add__()` určuje správanie operátora `+`.

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
        )
```

Použitie:

```python
vector1 = Vector(10, 20)
vector2 = Vector(102, 202)

print(vector1)
print(vector2)
print(vector1 + vector2)
```

Výsledok:

```text
[10, 20]
[102, 202]
[112, 222]
```

Pri operácii:

```python
vector1 + vector2
```

prebehne zjednodušene tento tok:

1. Python zavolá `vector1.__add__(vector2)`.
2. `self` označuje `vector1`.
3. `other` označuje `vector2`.
4. Spočítajú sa príslušné súradnice.
5. Vytvorí sa nový objekt `Vector`.
6. Nový objekt sa vráti ako výsledok sčítania.

Pôvodné vektory sa nemenia. Výsledkom je nový objekt.

---

## Kontrola typu pri sčítaní

Pôvodná verzia predpokladá, že `other` má atribúty `x` a `y`.

Problém môže vzniknúť napríklad pri:

```python
vector1 + 3
```

Číslo `3` nie je objektom triedy `Vector` a nemá atribúty `x` a `y`.

Metódu preto ošetríme pomocou `isinstance()`:

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(
                self.x + other.x,
                self.y + other.y,
            )

        return NotImplemented
```

Ak je `other` objektom triedy `Vector`, metóda vytvorí a vráti nový vektor.

Ak danú kombináciu typov metóda nevie spracovať, vráti špeciálnu hodnotu:

```python
NotImplemented
```

---

## `NotImplemented`

`NotImplemented` je vstavaná špeciálna hodnota Pythonu.

Pri binárnych operátoroch oznamuje:

> Táto metóda nevie vykonať danú operáciu s prijatým typom objektu.

Python potom môže skúsiť inú zodpovedajúcu operátorovú metódu druhého objektu. Ak operáciu nevie vykonať ani jeden objekt, výsledkom bude `TypeError`.

Napríklad:

```python
print(vector1 + 3)
```

vyvolá chybu podobnú:

```text
TypeError: unsupported operand type(s) for +: 'Vector' and 'int'
```

`NotImplemented` sa nesmie zamieňať s výnimkou `NotImplementedError`.

- `NotImplemented` je návratová hodnota používaná najmä pri operátoroch.
- `NotImplementedError` je výnimka, ktorú môže vyvolať neimplementovaná metóda.

---

# Ďalšie operátorové metódy

Python poskytuje veľké množstvo špeciálnych metód.

## Matematické operátory

- `__add__()` – sčítanie pomocou `+`,
- `__sub__()` – odčítanie pomocou `-`,
- `__mul__()` – násobenie pomocou `*`,
- `__truediv__()` – delenie pomocou `/`,
- `__floordiv__()` – celočíselné delenie pomocou `//`,
- `__mod__()` – zvyšok po delení pomocou `%`,
- `__pow__()` – umocnenie pomocou `**`.

## Unárne operátory

- `__neg__()` – záporný operátor `-objekt`,
- `__pos__()` – kladný operátor `+objekt`.

Príklad:

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(+self.x, +self.y)

    def __str__(self):
        return f"[{self.x}, {self.y}]"
```

Použitie:

```python
vector = Vector(10, -20)

print(-vector)
print(+vector)
```

Výsledok:

```text
[-10, 20]
[10, -20]
```

---

# Metóda `__bool__()`

Metóda `__bool__()` určuje, akú pravdivostnú hodnotu bude mať objekt pri použití v podmienke alebo vo funkcii `bool()`.

Metóda musí vrátiť `True` alebo `False`.

Pri vektore môžeme určiť, že nulový vektor `[0, 0]` bude nepravdivý a každý iný vektor bude pravdivý.

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __bool__(self):
        return not (self.x == 0 and self.y == 0)
```

Rovnaký návrat možno zapísať aj kratšie:

```python
def __bool__(self):
    return (self.x, self.y) != (0, 0)
```

Použitie:

```python
vector1 = Vector(10, 20)
vector2 = Vector(0, 0)

print(bool(vector1))
print(bool(vector2))
```

Výsledok:

```text
True
False
```

Objekt možno použiť aj priamo v podmienke:

```python
if vector1:
    print("Vector is not zero")
else:
    print("Vector is zero")
```

Tok programu:

```text
if vector1
→ zavolá sa vector1.__bool__()
→ metóda vráti True alebo False
→ podľa výsledku sa vyberie vetva podmienky
```

---

# Metóda `__eq__()`

Metóda `__eq__()` určuje, čo znamená rovnosť dvoch objektov pri operátore `==`.

Bez vlastnej implementácie sa dva samostatne vytvorené objekty zvyčajne nepovažujú za rovnaké iba preto, že majú rovnaké atribúty.

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return (self.x, self.y) == (other.x, other.y)
```

Použitie:

```python
vector1 = Vector(102, 202)
vector2 = Vector(102, 202)
vector3 = Vector(10, 20)

print(vector1 == vector2)
print(vector1 == vector3)
```

Výsledok:

```text
True
False
```

Tok porovnania:

```text
vector1 == vector2
→ zavolá sa vector1.__eq__(vector2)
→ overí sa typ druhého objektu
→ porovnajú sa dvojice súradníc
→ vráti sa True alebo False
```

Aj pri `__eq__()` je vhodné vrátiť `NotImplemented`, ak metóda nevie porovnať prijatý typ objektu.

---

# Súhrnný príklad triedy `Vector`

```python
class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x + other.x,
            self.y + other.y,
        )

    def __sub__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return Vector(
            self.x - other.x,
            self.y - other.y,
        )

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __pos__(self):
        return Vector(+self.x, +self.y)

    def __bool__(self):
        return (self.x, self.y) != (0, 0)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented

        return (self.x, self.y) == (other.x, other.y)
```

Použitie:

```python
vector1 = Vector(10, 20)
vector2 = Vector(5, 7)
zero_vector = Vector(0, 0)

print(vector1)
print(vector1 + vector2)
print(vector1 - vector2)
print(-vector1)
print(+vector1)
print(vector1 == vector2)
print(bool(vector1))
print(bool(zero_vector))
```

---

# Abstraktné triedy

Abstraktná trieda predstavuje spoločný základ a kontrakt pre konkrétne podtriedy.

Môže určovať:

- ktoré vlastnosti musia potomkovia poskytovať,
- ktoré metódy musia implementovať,
- ktoré hotové metódy automaticky zdedia.

Abstraktná trieda neslúži iba ako odporúčanie. Ak podtrieda neimplementuje všetky požadované abstraktné metódy, nemožno z nej vytvoriť objekt.

V Pythone sa na prácu s abstraktnými triedami používa modul `abc`.

```python
from abc import ABC, abstractmethod
```

- `ABC` je základná trieda pre abstraktné triedy,
- `abstractmethod` je dekorátor označujúci povinnú metódu alebo property.

---

## Abstraktná trieda `Shape`

```python
from abc import ABC, abstractmethod


class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def area(self):
        pass

    def describe(self):
        return f"{self.name}: area: {self.area()}"
```

Trieda `Shape`:

- dedí z `ABC`,
- má abstraktnú property `name`,
- má abstraktnú metódu `area()`,
- má hotovú metódu `describe()`.

Každá konkrétna podtrieda musí implementovať `name` a `area()`.

Metóda `describe()` už má hotovú implementáciu a potomkovia ju automaticky zdedia.

Samotný objekt `Shape` nemožno vytvoriť:

```python
shape = Shape()
```

Tento pokus vyvolá `TypeError`.

---

## Konkrétna trieda `Circle`

```python
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    @property
    def name(self):
        return "Circle"

    def area(self):
        return 3.14 * self.radius**2
```

Použitie:

```python
circle = Circle(10)

print(circle.name)
print(circle.area())
print(circle.describe())
```

Výsledok:

```text
Circle
314.0
Circle: area: 314.0
```

Tok pri vytvorení objektu:

1. Python skontroluje, či `Circle` implementuje všetky abstraktné požiadavky.
2. `Circle` poskytuje property `name`.
3. `Circle` poskytuje metódu `area()`.
4. Objekt možno vytvoriť.
5. Metóda `describe()` sa zdedí z triedy `Shape`.

Ak by `Circle` neimplementoval napríklad `area()`, zostal by abstraktnou triedou a objekt `Circle()` by nebolo možné vytvoriť.

---

## Abstraktné a konkrétne metódy

Abstraktná trieda môže obsahovať oba druhy metód.

### Abstraktná metóda

Určuje, čo musí potomok implementovať:

```python
@abstractmethod
def area(self):
    pass
```

### Konkrétna metóda

Obsahuje hotovú funkcionalitu, ktorú potomkovia zdedia:

```python
def describe(self):
    return f"{self.name}: area: {self.area()}"
```

Abstraktná trieda teda môže kombinovať:

- povinné rozhranie,
- spoločnú hotovú implementáciu.

---

# Koncept `__slots__`

Inštancie bežných tried ukladajú svoje atribúty spravidla v internom slovníku `__dict__`.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y


vector = Vector(10, 20)

print(vector.__dict__)
```

Výsledok:

```text
{'x': 10, 'y': 20}
```

Slovník je meniteľný, takže objektu možno dynamicky pridávať ďalšie atribúty:

```python
vector.description = "My vector"

print(vector.__dict__)
```

Výsledok môže byť:

```text
{'x': 10, 'y': 20, 'description': 'My vector'}
```

---

## Definovanie `__slots__`

Pomocou `__slots__` môžeme určiť, ktoré atribúty smú mať inštancie triedy.

```python
class Vector:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y
```

`__slots__` sa zvyčajne zapisuje ako tuple názvov povolených atribútov.

Použitie:

```python
vector = Vector(10, 20)

print(vector.x)
print(vector.y)
```

Pokus o pridanie iného atribútu vyvolá `AttributeError`:

```python
vector.description = "My vector"
```

---

## `__slots__` a `__dict__`

Pri tejto jednoduchej triede objekt bežne nemá vlastný `__dict__`.

Preto:

```python
print(vector.__dict__)
```

vyvolá `AttributeError`.

`__slots__` môže:

- obmedziť dynamické pridávanie atribútov,
- znížiť pamäťovú réžiu objektov,
- presnejšie vyjadriť povolenú štruktúru objektu.

Úspora pamäte môže byť dôležitá pri vytváraní veľkého množstva malých objektov.

Pri niekoľkých objektoch býva rozdiel zanedbateľný a `__slots__` nie je potrebné používať automaticky v každej triede.

Pri dedení existujú ďalšie pravidlá a výnimky. Napríklad podtrieda môže opäť získať `__dict__`, ak sama vhodne nepoužije `__slots__`.

---

# UML

UML znamená **Unified Modeling Language**.

Je to štandardizovaný vizuálny jazyk používaný na návrh a opis softvérových systémov.

UML nie je programovací jazyk. Pomáha znázorniť:

- triedy,
- atribúty,
- metódy,
- vzťahy medzi triedami,
- dedenie,
- kompozíciu a ďalšie väzby.

---

## UML class diagram

Class diagram, teda diagram tried, znázorňuje štruktúru objektovo orientovaného systému.

Základným prvkom diagramu je trieda. Bežne sa kreslí ako obdĺžnik rozdelený na tri časti:

```text
+------------------------+
|        Student         |
+------------------------+
| name                   |
+------------------------+
| __init__(name)         |
| __str__()              |
+------------------------+
```

Jednotlivé časti predstavujú:

1. názov triedy,
2. atribúty,
3. metódy.

---

## Vzťahy medzi triedami

### Dedenie

Dedenie vyjadruje vzťah „je“.

```text
Circle je Shape.
```

V UML sa znázorňuje čiarou s prázdnou trojuholníkovou šípkou smerujúcou k rodičovskej triede.

### Kompozícia

Kompozícia vyjadruje vzťah „má“.

```text
Course má študentov.
```

V UML sa znázorňuje čiarou s plným kosoštvorcom na strane objektu, ktorý obsahuje ďalšie objekty.

### Asociácia

Asociácia predstavuje všeobecné prepojenie medzi triedami.

Napríklad učiteľ môže vyučovať určitý kurz.

---

## Viditeľnosť v UML

Pri atribútoch a metódach sa môžu používať značky:

- `+` – verejný člen,
- `-` – súkromný člen,
- `#` – chránený člen.

Tieto značky opisujú návrh. Pythonova práca s jedným alebo dvoma podčiarkovníkmi je založená na konvencii a mechanizme name mangling, preto nejde o úplne rovnakú ochranu ako v niektorých iných jazykoch.

---

## Nástroje na kreslenie UML

Medzi nástroje na tvorbu diagramov patria napríklad:

- diagrams.net, pôvodne draw.io,
- Lucidchart,
- PlantUML,
- Mermaid,
- Visual Paradigm.

Na jednoduché diagramy tried je vhodný napríklad diagrams.net.

---

# Zhrnutie

- Špeciálne alebo dunder metódy určujú správanie objektov pri vstavaných operáciách Pythonu.
- `__add__()` určuje správanie operátora `+`.
- `__sub__()` určuje správanie operátora `-`.
- `__neg__()` a `__pos__()` pracujú s unárnymi operátormi.
- `__bool__()` určuje pravdivostnú hodnotu objektu.
- `__eq__()` určuje logiku porovnávania pomocou `==`.
- `NotImplemented` oznamuje, že operácia nie je podporovaná pre prijatý typ.
- `NotImplemented` nie je to isté ako výnimka `NotImplementedError`.
- Abstraktná trieda určuje spoločný základ a povinné rozhranie potomkov.
- `ABC` slúži ako základ abstraktnej triedy.
- `@abstractmethod` označuje metódu, ktorú musia konkrétni potomkovia implementovať.
- Abstraktná trieda môže obsahovať aj hotové metódy spoločné pre všetkých potomkov.
- `__slots__` obmedzuje povolené atribúty a môže znížiť pamäťovú réžiu objektov.
- Inštancia triedy so `__slots__` bežne nemá vlastný `__dict__`.
- UML class diagram znázorňuje triedy, ich atribúty, metódy a vzťahy.
- Dedenie vyjadruje vzťah „je“ a kompozícia vzťah „má“.