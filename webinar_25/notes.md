# Webinar 25 – História príkazov a JupyterLab notebooky

Väčšina webinaru bola venovaná prezeraniu a hodnoteniu projektov ostatných študentov. Tieto konkrétne riešenia nie sú súčasťou poznámok.

## Vyhľadávanie v histórii príkazov

### `Ctrl + R`

V Git Bash spustí spätné interaktívne vyhľadávanie v histórii príkazov:

```text
(reverse-i-search)`':
```

Počas vyhľadávania píšeme časť hľadaného príkazu. Bash priebežne zobrazí najnovší príkaz z histórie, ktorý obsahuje zadaný text.

Ak napríklad začneme písať:

```text
source
```

môže sa nájsť:

```bash
source skillmea/Scripts/activate
```

Opakovaným stláčaním `Ctrl + R` prechádzame ďalšie staršie výsledky, ktoré zodpovedajú hľadanému textu.

- `Enter` – potvrdí a vykoná nájdený príkaz,
- `Ctrl + G` – oficiálny spôsob zrušenia vyhľadávania a obnovenia pôvodného riadka,
- `Ctrl + C` – v Git Bash môže vyhľadávanie tiež prerušiť, ale zároveň zruší aktuálne zadávaný príkaz.

Oficiálna dokumentácia: [Bash – Searching for Commands in the History](https://www.gnu.org/software/bash/manual/html_node/Searching.html)

---

## Notebooky v JupyterLab

JupyterLab umožňuje vytvárať notebooky, v ktorých môžeme interaktívne zapisovať a vykonávať Python kód.

Notebook sa ukladá ako súbor s príponou:

```text
.ipynb
```

## Vytvorenie notebooku

V JupyterLab vyberieme kernel:

```text
Python 3 (ipykernel)
```

Otvorí sa nový notebook, ktorý môže mať pred uložením názov:

```text
Untitled.ipynb
```

Kernel je proces, ktorý vykonáva kód napísaný v bunkách. Pri použití `Python 3 (ipykernel)` beží interaktívny Python založený na IPythone.

## Uloženie notebooku

Notebook uložíme pomocou:

```text
Ctrl + S
```

Pri prvom uložení môžeme zvoliť jeho názov.

JupyterLab síce priebežne vykonáva automatické ukladanie, ale je vhodné prácu pravidelne uložiť aj manuálne.

---

## Bunky

Notebook sa skladá z buniek, po anglicky `cells`.

Kódová bunka môže obsahovať:

- Python príkazy,
- výrazy,
- priradenia,
- volania funkcií,
- viac riadkov kódu.

Každú bunku možno upravovať a spúšťať samostatne.

## Výstup bunky

Ak je posledným riadkom bunky výraz, Jupyter automaticky zobrazí jeho výsledok.

Ak bunka končí iba priradením hodnoty do premennej, bežne sa nezobrazí žiadny výstup. Hodnota sa však uloží do pamäte kernelu a možno ju použiť v ďalších bunkách.

---

## Spustenie buniek

### `Ctrl + Enter`

Vykoná aktuálnu bunku a ponechá označenie v tej istej bunke.

Je vhodné na opakované skúšanie alebo upravovanie jedného výpočtu.

### `Shift + Enter`

Vykoná aktuálnu bunku a presunie sa do nasledujúcej bunky.

Ak sa nachádzame v poslednej bunke, môže sa pod ňou vytvoriť nová bunka.

Táto skratka je vhodná na postupné vykonávanie notebooku zhora nadol.

Oficiálna dokumentácia: [Jupyter Notebook – Keyboard shortcuts](https://jupyter-notebook.readthedocs.io/en/v7.6.0/notebook.html#keyboard-shortcuts)

---

## Poradie vykonávania buniek

Pri notebooku nie je rozhodujúca iba poloha bunky v dokumente. Dôležité je poradie, v akom boli bunky skutočne vykonané.

Kernel si počas behu pamätá:

- vytvorené premenné,
- importované moduly,
- definované funkcie a triedy,
- výsledky predchádzajúcich operácií.

Preto môže bunka umiestnená vyššie používať hodnotu vytvorenú v bunke umiestnenej nižšie, ak bola spodná bunka vykonaná skôr.

To môže viesť k neprehľadnému stavu. Notebook môže počas práce fungovať, ale po reštartovaní kernelu môže zlyhať, ak bunky nie sú usporiadané v správnom poradí.

## Odporúčaný postup

Notebook je vhodné pripravovať tak, aby fungoval pri vykonaní buniek zhora nadol.

Pred dokončením práce je dobré:

1. reštartovať kernel,
2. vykonať všetky bunky v poradí zhora nadol,
3. skontrolovať, či nevznikla chyba.

Reštartovaním kernelu sa vymažú premenné a ostatný stav uložený v pamäti. Samotný notebook môže uchovávať kód a zobrazené výstupy, ale na obnovenie pracovného stavu treba bunky znovu vykonať.

---

## Zhrnutie

- `Ctrl + R` vyhľadáva staršie príkazy v histórii Git Bash.
- Notebooky sa ukladajú ako súbory `.ipynb`.
- Python kód sa vykonáva v samostatných bunkách.
- `Ctrl + Enter` vykoná bunku a zostane v nej.
- `Shift + Enter` vykoná bunku a pokračuje na ďalšiu.
- Kernel si pamätá výsledky vykonaných buniek.
- Dôležité je poradie vykonania, nielen vizuálne poradie buniek.
- Hotový notebook by mal fungovať po reštarte kernelu a spustení všetkých buniek zhora nadol.