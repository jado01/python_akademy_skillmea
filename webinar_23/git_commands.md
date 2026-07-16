# Git Bash a Git – praktické príkazy

Tento dokument slúži ako stručný ťahák k príkazom použitým pri práci s Git repozitárom.

## Git Bash a Git

**Git Bash** je terminál, v ktorom môžeme pracovať so súbormi, priečinkami a spúšťať Git príkazy.

**Git** sleduje zmeny súborov a umožňuje vytvárať históriu projektu pomocou commitov.

---

## Pohyb a orientácia

### `pwd`

Zobrazí cestu k aktuálnemu priečinku.

```bash
pwd
```

Pred použitím Git príkazov je vhodné overiť, či sa nachádzame v správnom repozitári.

### `ls`

Zobrazí viditeľné súbory a priečinky.

```bash
ls
```

### `ls -l`

Zobrazí podrobný zoznam položiek, každú na samostatnom riadku.

```bash
ls -l
```

### `ls -la`

Zobrazí podrobný zoznam vrátane skrytých položiek.

```bash
ls -la
```

- `-l` znamená podrobný výpis,
- `-a` znamená všetky položky vrátane skrytých.

Takto môžeme vidieť napríklad `.git` alebo `.gitignore`.

### `ls -1`

Zobrazí iba názvy položiek, každý na samostatnom riadku.

```bash
ls -1
```

Použitý znak je číslica `1`, nie malé písmeno `l`.

### `cd`

Prejde do vybraného priečinka.

```bash
cd projects
```

Prechod do vnoreného priečinka:

```bash
cd projects/02_employee_management
```

Prechod o jednu úroveň vyššie:

```bash
cd ..
```

---

## Vytváranie priečinkov a súborov

### `mkdir`

Vytvorí nový priečinok.

```bash
mkdir other_projects
```

Vytvorenie priečinka pomocou celej cesty:

```bash
mkdir projects/02_employee_management
```

Nadradený priečinok musí existovať.

### `mkdir -p`

Vytvorí cieľový priečinok a podľa potreby aj chýbajúce nadradené priečinky.

```bash
mkdir -p projects/02_employee_management
```

Ak cieľový priečinok už existuje, príkaz neskončí chybou.

### `touch`

Vytvorí nový prázdny súbor.

```bash
touch README.md
```

Vytvorenie súboru pomocou celej cesty:

```bash
touch projects/02_employee_management/README.md
```

Ak súbor už existuje, jeho obsah sa nevymaže. Aktualizuje sa iba čas poslednej zmeny.

### Otvorenie súboru vo VS Code

```bash
code README.md
```

Alebo pomocou celej cesty:

```bash
code projects/02_employee_management/README.md
```

---

## Presúvanie a premenovanie

### `mv`

Presunie alebo premenuje súbor či priečinok na disku.

```bash
mv povodny_nazov novy_nazov
```

### `git mv`

Presunie alebo premenuje sledovaný súbor či priečinok a zároveň pripraví zmenu do staging area.

```bash
git mv povodna_cesta nova_cesta
```

Príklad presunutia priečinka:

```bash
git mv projects/password_generator projects/other_projects/
```

Príklad premenovania:

```bash
git mv "projects/Password Generator" projects/other_projects/password_generator
```

Ak cesta obsahuje medzery, treba použiť úvodzovky.

`git mv` je približne skrátený zápis týchto krokov:

```bash
mv povodna_cesta nova_cesta
git add -A
```

Git pri commite porovná pôvodný a nový obsah a môže zmenu rozpoznať ako premenovanie alebo presun.

---

## Základné oblasti Gitu

Pri práci s Gitom rozlišujeme:

1. **Working tree** – aktuálne súbory, s ktorými pracujeme.
2. **Staging area** – zmeny pripravené do nasledujúceho commitu.
3. **Lokálny repozitár** – história commitov uložená v počítači.
4. **Vzdialený repozitár** – repozitár uložený napríklad na GitHube.

Bežný postup:

```text
úprava súborov
→ git add
→ git commit
→ git push
```

---

## Kontrola stavu

### `git status`

Zobrazí stav pracovného stromu a staging area.

```bash
git status
```

Je vhodné ho použiť:

1. pred začatím práce,
2. počas vykonávania zmien,
3. pred commitom,
4. po commite,
5. po pushi.

Červené zmeny väčšinou ešte nie sú pripravené do commitu.

Zelené zmeny sú pripravené v staging area a budú súčasťou nasledujúceho commitu.

Čistý pracovný strom:

```text
nothing to commit, working tree clean
```

---

## Príprava zmien do commitu

### `git add`

Pripraví konkrétny súbor do staging area.

```bash
git add README.md
```

Pomocou celej cesty:

```bash
git add projects/02_employee_management/README.md
```

### `git add -A`

Pripraví všetky zmeny v repozitári:

- nové súbory,
- upravené súbory,
- odstránené súbory,
- presuny a premenovania.

```bash
git add -A
```

Pred použitím je vhodné skontrolovať `git status`, aby sme nepridali nechcené zmeny.

---

## Kontrola pripravených zmien

### `git diff`

Zobrazí zmeny, ktoré ešte nie sú v staging area.

```bash
git diff
```

### `git diff --cached`

Zobrazí obsah zmien pripravených do nasledujúceho commitu.

```bash
git diff --cached
```

### `git diff --cached --stat`

Zobrazí stručný štatistický prehľad pripravených zmien.

```bash
git diff --cached --stat
```

### `git diff --cached --summary`

Zobrazí stručný súhrn presunov, premenovaní a ďalších pripravených zmien.

```bash
git diff --cached --summary
```

Príklad:

```text
rename projects/old/file.py => projects/new/file.py (100%)
```

Hodnota `100%` znamená, že obsah zostal rovnaký a zmenilo sa iba umiestnenie alebo názov.

### `git diff --cached --name-status`

Zobrazí pripravené súbory spolu s typom zmeny.

```bash
git diff --cached --name-status
```

Typické značky:

- `A` – nový súbor,
- `M` – upravený súbor,
- `D` – odstránený súbor,
- `R100` – súbor bol presunutý alebo premenovaný bez zmeny obsahu.

---

## Vytvorenie commitu

### `git commit`

Vytvorí commit zo zmien pripravených v staging area.

```bash
git commit -m "správa commitu"
```

Príklady:

```bash
git commit -m "refactor: reorganize academy projects"
```

```bash
git commit -m "docs: add employee management project overview"
```

Dobrá commit správa stručne vysvetľuje, čo sa zmenilo.

Často používané začiatky:

- `feat:` – nová funkcionalita,
- `fix:` – oprava chyby,
- `docs:` – dokumentácia,
- `refactor:` – zmena štruktúry bez pridania funkcionality,
- `test:` – testy,
- `chore:` – technická alebo pomocná úloha.

---

## História commitov

### `git log`

Zobrazí históriu commitov.

```bash
git log
```

Pri dlhom výstupe Git otvorí stránkovací prehliadač.

Ovládanie:

- `Space` – ďalšia stránka,
- `b` – predchádzajúca stránka,
- šípky – pohyb po riadkoch,
- `q` – ukončenie a návrat do Git Bash.

Text `(END)` znamená, že sme na konci výpisu. Pre návrat treba stlačiť `q`.

### Posledný commit

```bash
git log -1 --oneline
```

- `-1` zobrazí iba posledný commit,
- `--oneline` ho zobrazí na jednom riadku.

Príklad:

```text
a1b2c3d docs: add employee management project overview
```

### Stručná história

```bash
git log --oneline
```

### Výpis bez stránkovacieho prehliadača

```bash
git --no-pager log --oneline
```

---

## Odoslanie na GitHub

### `git push`

Odošle lokálne commity z aktuálnej vetvy do prepojenej vzdialenej vetvy.

```bash
git push
```

Po úspešnom pushi je vhodné overiť:

```bash
git status
```

Typický výsledok:

```text
Your branch is up to date with 'origin/main'.
nothing to commit, working tree clean
```

---

## Dôležité poznámky

### Git nesleduje prázdne priečinky

Prázdny priečinok sa na GitHube nezobrazí.

Priečinok sa začne zobrazovať až vtedy, keď obsahuje sledovaný súbor.

### Presuny pred commitom

Ak súbory presunieme viackrát pred vytvorením commitu, Git pri commite zaznamená výsledný stav.

Dočasné umiestnenia sa do histórie samostatne nedostanú.

### Práca s medzerami v cestách

Cesty obsahujúce medzery treba uzavrieť do úvodzoviek:

```bash
git mv "povodny priecinok" novy_priecinok
```

---

## Odporúčaný pracovný postup

```bash
git status
```

Upraviť alebo vytvoriť súbory.

```bash
git status
git diff
git add konkretna_cesta
git status
git diff --cached
git commit -m "typ: stručný opis zmeny"
git status
git push
git status
```

Pri programovaní projektu:

```text
malá etapa
→ vlastný kód
→ spustenie a test
→ kontrola zmien
→ commit
→ push
→ ďalšia etapa
```