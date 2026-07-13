# Webinar 21 – Kompozícia, enkapsulácia a `__str__`

## Kompozícia

Kompozícia umožňuje skladať zložitejšie objekty z jednoduchších objektov. Znamená, že jedna trieda vo svojom atribúte uchováva objekt alebo objekty inej triedy.

Vyjadruje vzťah **„má“**:

- knižnica má knihy,
- manažér má zamestnancov,
- logger má handler,
- tím má členov.

Kompozícia sa od dedenia líši:

- dedenie vyjadruje vzťah **„je“**,
- kompozícia vyjadruje vzťah **„má“**.

Napríklad `Library` nie je druhom knihy, ale obsahuje objekty `Book`.

---

## Príklad kompozície – Logger

Logger zaznamenáva správy, ale konkrétny spôsob ich spracovania prenecháva vloženému handleru.

```python
class Handler:
    def send(self, message):
        raise NotImplementedError


class ConsoleHandler(Handler):
    def send(self, message):
        print(message)


class FileHandler(Handler):
    def __init__(self, path):
        self.path = path

    def send(self, message):
        with open(self.path, "a", encoding="utf-8") as file:
            file.write(message)


class Logger:
    def __init__(self, handler):
        self.handler = handler

    def log(self, message):
        self.handler.send(message)
```

Použitie:

```python
console_logger = Logger(ConsoleHandler())
console_logger.log("Test message")

file_logger = Logger(FileHandler("logs.log"))
file_logger.log("Test message\n")
```

Tok programu pri konzolovom loggeri:

1. vytvorí sa objekt `ConsoleHandler`,
2. objekt sa vloží do objektu `Logger`,
3. zavolá sa `console_logger.log("Test message")`,
4. metóda `log()` zavolá `self.handler.send(message)`,
5. vykoná sa metóda `ConsoleHandler.send()`,
6. správa sa vypíše do konzoly.

`Logger` nemusí poznať detaily výpisu do konzoly alebo zápisu do súboru. Potrebuje iba objekt, ktorý poskytuje metódu `send()`.

Na signalizovanie neimplementovanej metódy sa používa výnimka `NotImplementedError`, nie hodnota `NotImplemented`.

---

# Enkapsulácia

Enkapsulácia spája stav objektu a metódy, ktoré s týmto stavom pracujú.

Jej cieľom je:

- skryť vnútorné detaily implementácie,
- obmedziť nežiaduce priame zmeny atribútov,
- kontrolovať hodnoty ukladané do atribútov,
- poskytnúť bezpečný spôsob práce s objektom.

Namiesto ľubovoľnej priamej zmeny atribútu môžeme hodnotu meniť cez metódu alebo property, ktorá najprv vykoná validáciu.

Napríklad zostatok bankového účtu by sa nemal dať ľubovoľne zmeniť:

```python
account.balance = -1000
```

Bezpečnejšie je meniť ho pomocou metód:

```python
account.deposit(100)
account.withdraw(50)
```

Tieto metódy môžu overiť, či je operácia povolená.

Python nemá úplne súkromné atribúty v rovnakom zmysle ako niektoré iné programovacie jazyky. Podčiarkovníky sú preto najmä signálom pre ostatných programátorov a v prípade dvoch podčiarkovníkov aktivujú mechanizmus name mangling.

---

## Verejný atribút

Atribút bez podčiarkovníka je verejný:

```python
self.balance
```

Môže sa bežne čítať aj meniť zvonka triedy:

```python
print(account.balance)
account.balance = 100
```

---

## Jeden podčiarkovník

```python
self._balance
```

Jeden podčiarkovník je konvencia označujúca interný alebo neverejný atribút.

Python prístup k takému atribútu nezakáže:

```python
account._balance = 100
```

Podčiarkovník však programátorovi oznamuje, že atribút patrí k vnútornej implementácii triedy a nemal by sa používať alebo meniť priamo mimo nej.

---

## Dva podčiarkovníky

```python
self.__balance
```

Dva podčiarkovníky aktivujú mechanizmus nazývaný **name mangling**. Python názov interne zmení tak, aby obsahoval aj názov triedy.

Napríklad atribút:

```python
self.__balance
```

sa v triede `BankAccount` interne zmení približne na:

```python
self._BankAccount__balance
```

Preto nasledujúci prístup bežne nefunguje:

```python
print(account.__balance)
```

Dva podčiarkovníky však neposkytujú absolútnu ochranu. K hodnote sa stále možno dostať cez interne upravený názov:

```python
print(account._BankAccount__balance)
```

Name mangling pomáha predchádzať najmä:

- náhodnému prístupu k internému atribútu,
- náhodnému prepísaniu atribútu,
- konfliktom názvov pri dedení.

Pre bežné interné atribúty sa v Pythone často používa jeden podčiarkovník. Dva podčiarkovníky používame vtedy, keď máme konkrétny dôvod použiť name mangling.

---

# Getter, setter a deleter

- **getter** hodnotu získava a vracia,
- **setter** prijíma a nastavuje novú hodnotu,
- **deleter** hodnotu odstraňuje a používa sa menej často.

---

## Getter a `@property`

Dekorátor `@property` umožňuje používať metódu syntaxou atribútu.

```python
class BankAccount:
    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self.__balance = starting_balance

    @property
    def balance(self):
        return self.__balance
```

Použitie:

```python
account = BankAccount("Miso", 200)
print(account.balance)
```

Hoci je `balance()` metóda, vďaka `@property` sa používa bez okrúhlych zátvoriek:

```python
account.balance
```

Nie:

```python
account.balance()
```

Metóda označená `@property` je getter, pretože sprístupňuje hodnotu na čítanie.

Ak property nemá setter, je zvonka iba na čítanie. Hodnotu možno získať:

```python
print(account.balance)
```

Nemožno ju však priamo nastaviť:

```python
account.balance = 100
```

Takéto priradenie vyvolá `AttributeError`.

---

## Setter a `@balance.setter`

Setter umožňuje kontrolovať nastavenie novej hodnoty.

```python
class BankAccount:
    def __init__(self, owner, starting_balance=0):
        self.owner = owner
        self.__balance = 0
        self.balance = starting_balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")

        self.__balance = value
```

Použitie:

```python
account = BankAccount("Miso", 200)

print(account.balance)

account.balance = 100
print(account.balance)
```

Pri priradení:

```python
account.balance = 100
```

Python automaticky zavolá setter:

```python
@balance.setter
def balance(self, value):
```

Tok programu:

1. vykoná sa `account.balance = 100`,
2. zavolá sa setter `balance(self, 100)`,
3. setter skontroluje prijatú hodnotu,
4. platnú hodnotu uloží do `self.__balance`,
5. pri neplatnej hodnote vyvolá `ValueError`,
6. program sa po skončení setteru vráti na miesto, odkiaľ bol setter vyvolaný.

Názov property, getteru a setteru musí byť rovnaký:

```python
@property
def balance(self):
    return self.__balance


@balance.setter
def balance(self, value):
    self.__balance = value
```

---

## Deleter

Property môže mať aj deleter:

```python
@balance.deleter
def balance(self):
    del self.__balance
```

Zavolal by sa pomocou:

```python
del account.balance
```

Deleter sa používa menej často. V prípade bankového účtu by odstránenie zostatku nedávalo veľký zmysel.

---

# Bezpečnejší bankový účet

Pôvodný príklad so setterom má jednu logickú slabinu.

Setter síce kontroluje, či zostatok nie je záporný, ale tieto operácie:

```python
self.__balance += amount
self.__balance -= amount
```

setter obchádzajú. Metóda `withdraw()` by preto mohla vytvoriť záporný zostatok.

Pri bankovom účte je vhodnejšie sprístupniť zostatok iba na čítanie a meniť ho prostredníctvom kontrolovaných metód `deposit()` a `withdraw()`.

```python
class BankAccount:
    def __init__(self, owner, starting_balance=0):
        if starting_balance < 0:
            raise ValueError("Starting balance cannot be negative")

        self.owner = owner
        self.__balance = starting_balance
        self.history = []

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be greater than zero")

        self.__balance += amount
        self.history.append(("deposit", amount))

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be greater than zero")

        if amount > self.__balance:
            raise ValueError("Insufficient balance")

        self.__balance -= amount
        self.history.append(("withdrawal", amount))
```

Použitie:

```python
account = BankAccount("Miso", 200)

account.deposit(50)
account.withdraw(100)

print(account.balance)
print(account.history)
```

Výsledok:

```text
150
[('deposit', 50), ('withdrawal', 100)]
```

Zostatok možno prečítať:

```python
print(account.balance)
```

Nemožno ho však priamo prepísať:

```python
account.balance = 100
```

Property `balance` totiž nemá setter.

---

# Špeciálna metóda `__str__()`

Metóda `__str__()` určuje používateľsky čitateľnú textovú podobu objektu.

Používa ju napríklad funkcia:

```python
str(object)
```

Funkcia `print()` ju použije pri výpise objektu.

Metóda `__str__()` musí vždy vrátiť reťazec.

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
```

Použitie:

```python
vector = Vector(10, 20)

print(vector)
print(str(vector))
```

Výsledok:

```text
[10, 20]
[10, 20]
```

Pri vykonaní:

```python
print(vector)
```

prebehne zjednodušene tento tok:

1. `print()` dostane objekt `vector`,
2. Python hľadá jeho metódu `__str__()`,
3. vykoná `vector.__str__()`,
4. metóda vráti reťazec `"[10, 20]"`,
5. `print()` tento reťazec vypíše.

Bez vlastnej metódy `__str__()` by sa zobrazila predvolená reprezentácia podobná tejto:

```text
<__main__.Vector object at 0x...>
```

---

# Projekt: systém správy zamestnancov a tímov

Projekt môže obsahovať napríklad:

- zamestnancov,
- manažérov,
- tímy,
- oddelenia,
- pridávanie a odoberanie zamestnancov,
- výpočet počtu zamestnancov,
- výpočet celkových platov,
- presúvanie zamestnancov medzi tímami.

Pri návrhu projektu treba najprv určiť:

1. aké objekty systém potrebuje,
2. aké atribúty majú jednotlivé objekty,
3. aké operácie majú objekty vykonávať,
4. kde ide o dedenie – vzťah „je“,
5. kde ide o kompozíciu – vzťah „má“,
6. ktoré atribúty majú byť verejné a ktoré interné,
7. cez aké metódy sa môže bezpečne meniť stav objektov.

Oddelenie alebo tím môže pomocou kompozície obsahovať zoznam objektov `Employee`.

Napríklad:

```python
class Team:
    def __init__(self, name):
        self.name = name
        self._employees = []
```

Trieda `Team` nie je potomkom triedy `Employee`. Tím obsahuje zamestnancov, preto ide o kompozíciu.

Spôsob implementácie projektu nie je presne určený. Pri návrhu treba použiť vlastnú predstavivosť a rozdeliť problém na menšie objekty a operácie.

Je možné navrhnúť aj vlastný OOP projekt.

---

# Zhrnutie

- Kompozícia skladá objekty z ďalších objektov a vyjadruje vzťah „má“.
- Dedenie vyjadruje vzťah „je“.
- Objekt môže vo svojom atribúte uchovávať iný objekt alebo zoznam objektov.
- Enkapsulácia chráni vnútorný stav objektu a určuje bezpečný spôsob práce s ním.
- Atribút bez podčiarkovníka je verejný.
- Jeden podčiarkovník označuje interný atribút podľa programátorskej konvencie.
- Dva podčiarkovníky aktivujú name mangling.
- Dva podčiarkovníky neposkytujú absolútnu ochranu údajov.
- Getter hodnotu sprístupňuje na čítanie.
- Setter kontroluje a nastavuje novú hodnotu.
- Deleter môže hodnotu odstrániť.
- `@property` umožňuje používať metódu ako atribút.
- Property bez setteru je zvonka iba na čítanie.
- Metódy môžu chrániť stav objektu pomocou validácie.
- `__str__()` vracia používateľsky čitateľnú textovú podobu objektu.
- Metóda `__str__()` musí vždy vrátiť reťazec.