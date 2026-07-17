# Webinar 24 – Úvod do dátovej analýzy

## Dátová analýza a pandas

`pandas` je jedna z najpoužívanejších Python knižníc na prácu s dátami. Poskytuje nástroje na načítanie, spracovanie, čistenie, analýzu a úpravu dát.

Oficiálna stránka: [pandas](https://pandas.pydata.org/)

---

## Verzie programov a knižníc

Verzie softvéru sa často zapisujú vo formáte:

```text
MAJOR.MINOR.PATCH
```

Napríklad:

```text
2.1.3
```

### MAJOR verzia

Prvé číslo označuje hlavnú verziu programu.

Zvyšuje sa pri zmenách, ktoré nemusia byť spätne kompatibilné. Kód fungujúci s verziou `1.x.x` preto nemusí fungovať s verziou `2.x.x`.

### MINOR verzia

Druhé číslo označuje vedľajšiu verziu.

Pri sémantickom verzovaní sa zvyšuje pri pridaní novej funkcionality, ktorá zostáva spätne kompatibilná.

### PATCH verzia

Tretie číslo označuje opravnú verziu.

Zvyšuje sa najmä pri opravách chýb, ktoré nemenia existujúce verejné rozhranie programu.

Príklad:

```text
1.0.2 → 1.2.3
```

Obe verzie majú rovnakú major verziu, preto by pri dodržaní sémantického verzovania mali zostať spätne kompatibilné.

Prechod na:

```text
2.0.0
```

môže obsahovať nekompatibilné zmeny.

Nie každý program alebo knižnica musí pravidlá sémantického verzovania dodržiavať úplne presne.

Viac informácií: [Semantic Versioning](https://semver.org/)

---

## Virtuálne prostredie

Virtuálne prostredie je oddelené Python prostredie určené pre konkrétny projekt.

Môže obsahovať vlastné:

- nainštalované knižnice,
- verzie knižníc,
- Python interpreter odvodený od použitej inštalácie Pythonu,
- spustiteľné príkazy nainštalovaných balíkov.

Vďaka tomu môžu rôzne projekty používať rôzne verzie rovnakých knižníc bez vzájomného ovplyvňovania.

Príklad:

```text
Projekt A → pandas 2.x
Projekt B → pandas 3.x
```

### Virtuálne prostredie nie je bezpečnostný sandbox

Virtuálne prostredie izoluje najmä Python balíky. Nie je bezpečnostnou bariérou a nebráni programu v prístupe k súborom, sieti alebo operačnému systému.

Pojmy virtuálne prostredie a sandbox preto nie sú synonymá.

---

## Vytvorenie virtuálneho prostredia

V Git Bash:

```bash
python -m venv skillmea
```

Význam jednotlivých častí:

- `python` – spustí Python interpreter,
- `-m` – spustí zvolený Python modul ako program,
- `venv` – modul na vytváranie virtuálnych prostredí,
- `skillmea` – názov a cesta vytváraného prostredia.

Názov `skillmea` je ľubovoľný. Často sa používa aj názov `.venv`.

Oficiálna dokumentácia: [Python venv](https://docs.python.org/3/library/venv.html)

---

## Aktivácia virtuálneho prostredia

V Git Bash na Windows:

```bash
source skillmea/Scripts/activate
```

Po aktivácii sa na začiatku príkazového riadka zvyčajne zobrazí názov prostredia:

```text
(skillmea)
```

Aktivácia upraví premennú `PATH`, takže príkazy `python`, `pip` a ďalšie nainštalované nástroje používajú aktívne virtuálne prostredie.

Virtuálne prostredie technicky možno používať aj bez aktivácie, ak priamo spustíme jeho Python interpreter. Aktivácia je však pri bežnej práci pohodlnejšia.

### Deaktivácia

```bash
deactivate
```

Tým sa terminál vráti k pôvodnému Python prostrediu.

Pri otvorení nového terminálu treba virtuálne prostredie znovu aktivovať.

---

## Virtuálne prostredie a Git

Priečinok virtuálneho prostredia sa zvyčajne neukladá do Git repozitára.

Ak sa prostredie volá `skillmea`, do `.gitignore` sa pridá:

```text
skillmea/
```

Virtuálne prostredia nie sú všeobecne prenosné. Na inom počítači je lepšie vytvoriť nové prostredie a potrebné balíky opätovne nainštalovať.

---

## Užitočné príkazy Git Bash

### Aktuálny priečinok

```bash
pwd
```

`pwd` znamená `print working directory`. Zobrazí absolútnu cestu k aktuálnemu priečinku.

### Obsah priečinka

```bash
ls
```

Zobrazí súbory a priečinky v aktuálnom umiestnení.

### Zmena priečinka

```bash
cd nazov_priecinka
```

Prechod do nadradeného priečinka:

```bash
cd ..
```

### Otvorenie aktuálneho priečinka vo VS Code

```bash
code .
```

Bodka označuje aktuálny priečinok.

### Vyčistenie terminálu

```bash
clear
```

Možno použiť aj klávesovú skratku:

```text
Ctrl + L
```

---

## pip a nainštalované balíky

`pip` je nástroj na inštaláciu a správu Python balíkov.

### Zobrazenie nainštalovaných balíkov

```bash
pip list
```

Presnejší spôsob, ktorý jednoznačne použije `pip` patriaci aktuálnemu Python interpreteru:

```bash
python -m pip list
```

Príkaz zobrazí nainštalované balíky a ich verzie.

`pip list` zobrazuje plochý zoznam balíkov. Nezobrazuje grafický ani hierarchický strom závislostí.

Oficiálna dokumentácia: [pip list](https://pip.pypa.io/en/stable/cli/pip_list/)

---

## Závislosti

Závislosť je ďalší balík, ktorý program alebo knižnica potrebuje na svoje fungovanie.

Pri inštalácii JupyterLab sa nenainštaluje iba jeden balík. `pip` nainštaluje aj jeho požadované závislosti a podľa potreby závislosti týchto závislostí.

Takto vzniká strom závislostí:

```text
JupyterLab
├── závislosť A
│   └── ďalšia závislosť
├── závislosť B
└── závislosť C
```

Po inštalácii môžeme všetky nainštalované balíky vidieť cez `pip list`, ale samotnú stromovú štruktúru tento príkaz nezobrazuje.

---

## pyenv

`pyenv` je nástroj na inštalovanie a prepínanie viacerých verzií Pythonu.

Príklad použitia:

```text
jeden projekt → Python 3.11
iný projekt → Python 3.13
```

Rozdiel:

- `pyenv` spravuje verzie Pythonu,
- `venv` vytvára oddelené prostredia a spravuje balíky jednotlivých projektov.

Tieto nástroje riešia odlišné problémy a môžu sa používať spolu.

Oficiálny projekt: [pyenv](https://github.com/pyenv/pyenv)

---

## JupyterLab

JupyterLab je webové vývojové prostredie určené najmä na interaktívnu prácu s dátami, notebookmi, textovými súbormi a terminálom.

Spúšťa sa ako lokálny server a používateľské rozhranie sa otvorí vo webovom prehliadači.

Oficiálna stránka: [Jupyter](https://jupyter.org/)

### Inštalácia

Najprv treba aktivovať virtuálne prostredie. Potom sa JupyterLab nainštaluje pomocou:

```bash
python -m pip install jupyterlab
```

Možno použiť aj:

```bash
pip install jupyterlab
```

Oficiálny návod: [JupyterLab installation](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)

### Spustenie

Vo virtuálnom prostredí:

```bash
jupyter lab
```

JupyterLab spustí lokálny server a zvyčajne otvorí prehliadač na adrese podobnej:

```text
http://localhost:8888/lab
```

Číslo portu nemusí byť vždy `8888`. Ak je port obsadený, Jupyter môže použiť iný.

Priečinok, z ktorého JupyterLab spustíme, ovplyvňuje počiatočné umiestnenie zobrazené v jeho prehliadači súborov.

### Ukončenie

Treba sa vrátiť do terminálu, v ktorom JupyterLab beží, a stlačiť:

```text
Ctrl + C
```

Terminál môže následne vyžiadať potvrdenie ukončenia servera.

Ak chceme JupyterLab spustiť neskôr znova, treba otvoriť terminál, prejsť do správneho projektu, aktivovať virtuálne prostredie a znovu zadať príkaz na spustenie.

---

## Odporúčaný pracovný postup

1. Prejsť do priečinka projektu.
2. Vytvoriť virtuálne prostredie.
3. Aktivovať ho.
4. Nainštalovať potrebné balíky.
5. Skontrolovať nainštalované balíky.
6. Spustiť JupyterLab.
7. Po práci ukončiť JupyterLab.
8. Deaktivovať virtuálne prostredie.

Príklad použitých príkazov:

```bash
python -m venv skillmea
source skillmea/Scripts/activate
python -m pip install jupyterlab
python -m pip list
jupyter lab
deactivate
```