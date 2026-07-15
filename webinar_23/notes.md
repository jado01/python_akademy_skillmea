# Webinar 23 – Úvod do Gitu, GitHubu a Git Bash

## Git

Git je distribuovaný systém na správu verzií.

Používa sa na:

- zaznamenávanie zmien v súboroch,
- uchovávanie histórie projektu,
- návrat k starším verziám,
- vytváranie samostatných vývojových vetiev,
- spájanie zmien,
- spoluprácu viacerých ľudí na jednom projekte.

Git pracuje lokálne na počítači. Na vytváranie commitov preto nie je potrebné internetové pripojenie.

Projekt, ktorého zmeny Git sleduje, sa nazýva **repozitár**.

---

## Tri základné časti práce s Gitom

Pri bežnej práci s Gitom rozlišujeme tri základné oblasti:

1. **Working directory / working tree**
   - pracovný priečinok projektu,
   - obsahuje súbory, ktoré práve upravujeme.

2. **Staging area**
   - nazýva sa aj **index**,
   - obsahuje zmeny vybrané do nasledujúceho commitu,
   - umožňuje rozhodnúť, ktoré zmeny chceme zahrnúť do commitu.

3. **Local repository**
   - lokálny repozitár,
   - nachádza sa v skrytom priečinku `.git`,
   - uchováva commity, vetvy a históriu projektu.

Základný tok práce:

```text
Working directory
        ↓
Staging area
        ↓
Local repository
```

Najprv upravíme súbory, potom vyberieme zmeny do staging area a nakoniec vytvoríme commit.

---

## Commit

Commit je uložená snímka stavu projektu v určitom okamihu.

Obsahuje najmä:

- vybrané zmeny zo staging area,
- autora,
- dátum a čas,
- správu opisujúcu vykonanú zmenu,
- odkaz na predchádzajúci commit.

Commity spolu vytvárajú históriu projektu.

Každý commit by mal predstavovať jednu ucelenú a zmysluplnú zmenu. Je vhodné commitovať pravidelne, ale nie každú náhodnú alebo nefunkčnú úpravu.

Príklady vhodných commitov:

```text
Add user authentication
Fix salary validation
Update webinar 23 notes
```

Git pracuje so snímkami stavov projektu. Ak sa súbor nezmenil, Git môže odkázať na jeho predchádzajúcu uloženú verziu namiesto zbytočného ukladania rovnakej informácie znova.

---

## Vetvy – branches

Git umožňuje vytvárať vetvy.

Vetva predstavuje samostatnú líniu vývoja projektu. Môžeme na nej pracovať bez toho, aby sme okamžite menili hlavnú vetvu.

Hlavná vetva sa dnes najčastejšie nazýva:

```text
main
```

V starších repozitároch alebo konfiguráciách sa môžeme stretnúť aj s názvom:

```text
master
```

Novú funkcionalitu alebo opravu môžeme vytvárať na samostatnej vetve a po dokončení ju spojiť s hlavnou vetvou.

Príklad:

```text
main
 ├── feature-login
 └── fix-validation
```

Vetvy umožňujú:

- pracovať na viacerých funkciách oddelene,
- experimentovať bez poškodenia hlavnej vetvy,
- spolupracovať s ďalšími programátormi,
- kontrolovať zmeny pred ich spojením.

---

## Spájanie vetiev – merge

Zmeny z jednej vetvy môžeme spojiť do druhej vetvy. Tento proces sa nazýva:

```text
merge
```

Git dokáže veľa zmien spojiť automaticky.

Ak však dve vetvy upravia rovnakú časť rovnakého súboru rozdielnym spôsobom, môže vzniknúť:

```text
merge conflict
```

Pri konflikte Git nevie automaticky rozhodnúť, ktorú zmenu má zachovať. Programátor musí konflikt skontrolovať, vybrať správny výsledok a následne uložiť vyriešenie konfliktu.

Konflikt teda nevznikne pri každom spájaní vetiev. Nastane iba vtedy, keď Git nedokáže rozdielne zmeny bezpečne spojiť automaticky.

---

## Pull request a merge request

Na GitHube sa návrh na spojenie zmien z jednej vetvy do druhej nazýva:

```text
pull request
```

Pull request umožňuje:

- zobraziť navrhované zmeny,
- porovnať dve vetvy,
- diskutovať o úpravách,
- vykonať kontrolu kódu,
- schváliť alebo zamietnuť zmeny,
- spojiť zmeny do cieľovej vetvy.

Pojem **merge request** označuje podobnú funkciu, ale používa sa napríklad na platforme GitLab.

---

## GitHub

GitHub je internetová platforma na ukladanie a správu Git repozitárov.

Git a GitHub nie sú to isté:

- **Git** je nástroj na správu verzií, ktorý funguje aj lokálne,
- **GitHub** je služba, na ktorej môžeme Git repozitár zverejniť alebo zdieľať.

GitHub umožňuje:

- uchovávať vzdialené repozitáre,
- zálohovať a zdieľať projekty,
- spolupracovať s ďalšími ľuďmi,
- prezerať históriu zmien,
- pracovať s vetvami a pull requestmi,
- kontrolovať kód,
- evidovať úlohy a chyby.

Lokálny repozitár môže existovať aj bez GitHubu. GitHub je vzdialené miesto, s ktorým môžeme lokálny repozitár prepojiť.

---

## Git Bash

Git Bash je terminálové prostredie pre Windows, ktoré sa nainštaluje spolu s Gitom.

Umožňuje:

- používať príkazy Gitu,
- pracovať so súbormi a priečinkami cez terminál,
- používať mnohé príkazy známe z Linuxu a macOS,
- spúšťať shellové príkazy a skripty.

Git Bash nie je samostatný operačný systém. Je to aplikácia, ktorá vo Windowse poskytuje shellové prostredie podobné unixovým systémom.

Po otvorení sa zvyčajne nachádzame v domovskom priečinku používateľa.

Symbol:

```text
~
```

predstavuje domovský priečinok.

---

## Základné príkazy v Git Bash

### Zobrazenie aktuálneho priečinka

```bash
pwd
```

`pwd` znamená **print working directory**.

Vypíše cestu k priečinku, v ktorom sa práve nachádzame.

### Zobrazenie obsahu priečinka

```bash
ls
```

Vypíše súbory a priečinky v aktuálnom priečinku.

Podrobnejší výpis vrátane skrytých súborov:

```bash
ls -la
```

Skryté súbory a priečinky majú v unixovom prostredí názov začínajúci bodkou, napríklad:

```text
.git
```

### Vyčistenie obrazovky terminálu

```bash
clear
```

Odstráni predchádzajúci text z obrazovky terminálu. Nevymaže súbory ani históriu repozitára.

### Zmena priečinka

```bash
cd nazov_priecinka
```

`cd` znamená **change directory**.

Presunie nás do zadaného priečinka.

Návrat o jeden priečinok vyššie:

```bash
cd ..
```

Presun do domovského priečinka:

```bash
cd ~
```

Ak názov alebo cesta obsahuje medzery, môžeme použiť úvodzovky:

```bash
cd "My Projects"
```

### Vytvorenie priečinka

```bash
mkdir nazov_priecinka
```

`mkdir` znamená **make directory**.

Príklad:

```bash
mkdir demo-project
```

### Odstránenie súboru

```bash
rm nazov_suboru
```

`rm` znamená **remove**.

Tento príkaz treba používať opatrne, pretože odstránenie cez terminál nemusí presunúť súbor do koša.

### Odstránenie priečinka

```bash
rm -r nazov_priecinka
```

Parameter `-r` znamená rekurzívne odstránenie priečinka vrátane jeho obsahu.

Tento príkaz treba používať veľmi opatrne. Pred spustením je vhodné skontrolovať aktuálny priečinok pomocou `pwd` a jeho obsah pomocou `ls`.

---

## Rozdiely medzi terminálmi

Príkazy na prácu so súbormi a priečinkami sa môžu líšiť podľa použitého terminálu:

- Git Bash používa najmä unixové príkazy,
- Windows Command Prompt používa príkazy systému Windows,
- PowerShell používa vlastné príkazy a aliasy,
- Linux a macOS používajú unixové shellové príkazy.

Samotné príkazy Gitu, napríklad `git init`, `git status` alebo `git commit`, sú vo všetkých týchto prostrediach veľmi podobné.

---

## Inicializácia Git repozitára

Ak máme existujúci priečinok projektu a chceme, aby v ňom Git začal sledovať históriu zmien, presunieme sa doň:

```bash
cd demo-project
```

Potom spustíme:

```bash
git init
```

Príkaz `git init`:

- inicializuje Git repozitár,
- vytvorí skrytý priečinok `.git`,
- pripraví projekt na sledovanie verzií a vytváranie commitov.

Po inicializácii môže Git Bash v príkazovom riadku zobraziť názov aktuálnej vetvy, napríklad:

```text
(main)
```

alebo podľa konfigurácie:

```text
(master)
```

Samotné `git init` ešte nevytvorí commit ani neodošle projekt na GitHub. Iba pripraví lokálny priečinok ako Git repozitár.

---

## Základný princíp práce

Zjednodušený postup práce s Gitom:

```text
1. Vytvoríme alebo upravíme súbory.
2. Vyberieme zmeny, ktoré chceme uložiť.
3. Vytvoríme commit.
4. Pokračujeme v ďalšej práci.
5. Podľa potreby odošleme commity do vzdialeného repozitára.
```

Konkrétne príkazy na vytvorenie commitu a odoslanie zmien na GitHub budú témou nasledujúcej lekcie.

---

## Zhrnutie

- Git je distribuovaný systém na správu verzií.
- Git sleduje históriu zmien v projekte.
- Git pracuje s pracovným priečinkom, staging area a lokálnym repozitárom.
- Commit je uložená snímka stavu projektu.
- Vetvy umožňujú oddelený vývoj.
- Vetvy môžeme spájať pomocou merge.
- Pri nezlučiteľných zmenách môže vzniknúť merge conflict.
- GitHub je platforma na ukladanie a zdieľanie Git repozitárov.
- Na GitHube sa návrh na spojenie vetiev nazýva pull request.
- Git Bash poskytuje vo Windowse prostredie podobné unixovému terminálu.
- `git init` vytvorí v aktuálnom priečinku lokálny Git repozitár.