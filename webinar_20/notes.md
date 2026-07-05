# Webinar 20 - Programátorské špecializácie a OOP

## Programátorské špecializácie

Programovanie zahŕňa veľké množstvo oblastí. Programátor sa preto zvyčajne špecializuje na určitý typ aplikácií, technológií alebo problémov.

### Webový vývoj

- **Frontend developer** vytvára používateľskú časť webovej aplikácie, ktorú vidíme a ovládame v prehliadači.
- **Backend developer** vytvára serverovú logiku, API, spracovanie dát a komunikáciu s databázou.
- **Databázový špecialista (DBA)** spravuje databázy, ich výkon, bezpečnosť, dostupnosť a zálohovanie. Nie je obmedzený iba na webové projekty.
- **DevOps engineer** automatizuje nasadzovanie aplikácií, prevádzku infraštruktúry, testovanie a monitorovanie.
- **Full-stack developer** pracuje na frontende aj backende. Rozsah jeho práce závisí od konkrétneho tímu a projektu.

### Dátová oblasť

- **Data Analyst (DA)** spracúva a analyzuje dáta, pripravuje reporty a vizualizácie a hľadá v dátach užitočné informácie.
- **Data Scientist (DS)** pracuje so štatistikou, experimentmi a modelmi strojového učenia.
- **Database Administrator (DBA)** spravuje databázové systémy používané aj v dátových projektoch.
- **MLOps engineer** zabezpečuje nasadzovanie, prevádzku, monitorovanie a automatizáciu modelov strojového učenia.

### Aplikačné programovanie

- desktopové aplikácie pre počítače,
- mobilné aplikácie pre telefóny a tablety,
- aplikácie pre inteligentné zariadenia, napríklad hodinky.

### Ďalšie oblasti

- **IoT** - programovanie senzorov, mikrokontrolérov a inteligentných zariadení,
- **kybernetická bezpečnosť**,
- **systémové programovanie** - operačné systémy, ovládače a nízkoúrovňové nástroje,
- **vývoj hier**.

---

# Objektovo orientované programovanie

## Inštančná metóda

Inštančná metóda pracuje s konkrétnou inštanciou triedy. Jej prvým parametrom je `self`.

```python
from datetime import date


class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def age(self):
        return date.today().year - self.birth_year


person = Person("Miso", 1996)
print(person.name)
print(person.age())
```

---

## Triedna metóda

Triedna metóda je označená dekorátorom `@classmethod`. Jej prvým parametrom je `cls`, ktorý odkazuje na triedu.

Používa sa vtedy, keď metóda potrebuje pracovať so stavom triedy, napríklad s triednym atribútom.

```python
class Person:
    species = "Homo sapiens"

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @classmethod
    def rename_species(cls, new_name):
        cls.species = new_name


print(Person.species)
Person.rename_species("Sapiens")
print(Person.species)
```

Zmena triedneho atribútu sa týka celej triedy, nie iba jednej inštancie.

---

## Statická metóda

Statická metóda je označená dekorátorom `@staticmethod`.

Takáto metóda:

- neprijíma automaticky `self` ani `cls`,
- nepotrebuje stav konkrétnej inštancie ani triedy,
- logicky súvisí s danou triedou,
- mohla by existovať aj ako samostatná funkcia mimo triedy.

Statické metódy nám pomáhajú združiť súvisiacu funkcionalitu na jednom mieste.

```python
from datetime import date


class Person:
    species = "Homo sapiens"

    def __init__(self, name, birth_year):
        if not Person.is_valid_name(name):
            raise ValueError("Name must be a string")

        self.name = name
        self.birth_year = birth_year

    def age(self):
        return date.today().year - self.birth_year

    @classmethod
    def rename_species(cls, new_name):
        cls.species = new_name

    @staticmethod
    def is_valid_name(name):
        return isinstance(name, str)


person = Person("Miso", 1996)
print(person.name)
```

Metóda `is_valid_name()` slúži na validáciu mena. Funkcia `isinstance()` overí, či je hodnota inštanciou zadaného typu.

---

# Dedenie

Dedenie umožňuje vytvoriť novú triedu z existujúcej triedy.

- **rodičovská trieda** poskytuje atribúty a metódy,
- **potomok (podtrieda)** ich môže používať, rozšíriť alebo prepísať.

Rodičovskú triedu uvedieme v okrúhlych zátvorkách za názvom novej triedy.

## Zdedenie konštruktora

Ak podtrieda nemá vlastný konštruktor, použije konštruktor rodičovskej triedy.

```python
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    pass


dog = Dog("Miso")
print(dog.name)
```

---

## Zdedenie správania

Podtrieda môže používať metódy rodičovskej triedy.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    pass


dog = Dog("Miso")
print(dog.speak())
```

---

## Prepisovanie metód (overriding)

Podtrieda môže zmeniť zdedené správanie tým, že vytvorí metódu s rovnakým názvom.

Pri volaní sa použije metóda z najkonkrétnejšej triedy daného objektu.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Haf haf"


dog = Dog("Miso")
print(dog.speak())
```

Dedenie pokračuje smerom od rodiča k potomkovi. Trieda môže byť zároveň potomkom jednej triedy a rodičom ďalšej triedy.

---

## Funkcia `super()`

Funkcia `super()` poskytuje prístup k implementácii metód podľa dedičskej hierarchie. Často sa používa na zavolanie rodičovskej verzie prepísanej metódy.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Haf haf"

    def fetch(self):
        return f"Dog {self.name} fetched the ball."


class LoudDog(Dog):
    def speak(self):
        original_sound = super().speak()
        return original_sound + "!!!"


loud_dog = LoudDog("Ferko")
print(loud_dog.speak())
print(loud_dog.fetch())
```

Trieda `LoudDog`:

- zdedila konštruktor pôvodne definovaný v triede `Animal`,
- zdedila metódu `fetch()` z triedy `Dog`,
- prepísala metódu `speak()`, ale zároveň v nej použila implementáciu z triedy `Dog`.

---

# Pomocné funkcie

## `isinstance()`

Funkcia `isinstance()` zisťuje, či je objekt inštanciou zadanej triedy alebo niektorého z jej rodičov.

## `issubclass()`

Funkcia `issubclass()` zisťuje, či je jedna trieda podtriedou druhej triedy.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I am an animal"


class Dog(Animal):
    def speak(self):
        return "Haf haf"

    def fetch(self):
        return f"Dog {self.name} fetched the ball."


class LoudDog(Dog):
    def speak(self):
        return super().speak() + "!!!"


dog = Dog("Jozo")
loud_dog = LoudDog("Ferko")

print(isinstance(dog, Dog))             # True
print(isinstance(dog, Animal))          # True
print(isinstance(dog, LoudDog))         # False
print(isinstance(loud_dog, LoudDog))    # True

print(issubclass(LoudDog, Dog))         # True
print(issubclass(Dog, LoudDog))         # False
```

---

# Viacnásobné dedenie

Python umožňuje, aby trieda dedila od viacerých rodičovských tried naraz.

```python
class Flyer:
    def move(self):
        return "I am flying"


class Swimmer:
    def swim(self):
        return "I am swimming"


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
print(duck.move())
print(duck.swim())
```

## MRO

MRO znamená **Method Resolution Order**. Určuje poradie, v akom Python prehľadáva triedy pri hľadaní metódy alebo atribútu.

Poradie môžeme zobraziť pomocou metódy `mro()`:

```python
print(Duck.mro())
```

Pri viacnásobnom dedení je MRO dôležité najmä vtedy, keď viaceré rodičovské triedy obsahujú metódu s rovnakým názvom.

---

# Zhrnutie

- Inštančná metóda pracuje s objektom cez `self`.
- Triedna metóda pracuje s triedou cez `cls`.
- Statická metóda nepotrebuje `self` ani `cls`, ale logicky patrí k triede.
- Dedenie umožňuje opätovne použiť a rozšíriť existujúce správanie.
- Overriding mení zdedenú metódu v podtriede.
- `super()` sprístupňuje ďalšiu implementáciu metódy podľa MRO.
- `isinstance()` kontroluje objekt a `issubclass()` vzťah medzi triedami.
- MRO určuje poradie vyhľadávania pri dedení.
