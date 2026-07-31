# Webinar 28 – Pokračovanie práce s pandas

## Apache Spark

Apache Spark je nástroj určený na distribuované spracovanie veľkého množstva dát.

Niektoré spôsoby práce s tabuľkovými dátami sú podobné pandas. Spark poskytuje aj pandas API on Spark, ktoré umožňuje používať známu syntax pandas nad distribuovanými dátami.

Pandas je vhodný najmä pre dáta, ktoré sa zmestia do pamäte jedného počítača. Spark dokáže dáta spracúvať paralelne a rozdeliť prácu medzi viac počítačov.

V tomto webinári sme so Sparkom ešte priamo nepracovali.

## Formátovanie a kontrola zdrojového kódu

### Formatter

Formatter automaticky upravuje vzhľad zdrojového kódu podľa stanovených pravidiel.

Dokáže upraviť napríklad:

- odsadenie,
- medzery,
- dĺžku riadkov,
- zalomenie dlhých výrazov,
- jednotný štýl zápisu.

Príkladom Python formattera je **Black**.

### Linting

Linting je automatická kontrola zdrojového kódu.

Linter dokáže upozorniť napríklad na:

- nepoužité importy,
- nepoužité premenné,
- podozrivé časti kódu,
- porušenie pravidiel štýlu,
- niektoré možné chyby.

Formatter upravuje najmä vzhľad kódu, zatiaľ čo linter ho analyzuje a upozorňuje na problémy.

## Vytvorenie vlastného datasetu

Pandas `DataFrame` nemusíme načítať iba zo súboru CSV. Môžeme ho vytvoriť aj priamo zo slovníka.

```python
import pandas as pd

df = pd.DataFrame({
    "city": [
        "Bratislava",
        "Košice",
        "Žilina",
        "Bratislava",
        "Košice",
        "Žilina",
    ]
})
```

Kľúče slovníka sa stanú názvami stĺpcov a zoznamy sa stanú ich hodnotami.

Ak neurčíme vlastný index, pandas automaticky vytvorí číselný index začínajúci od nuly.

## NumPy

NumPy je knižnica určená na efektívnu prácu s číselnými dátami a viacrozmernými poľami.

Pandas pri mnohých operáciách využíva dátové štruktúry a funkcie NumPy.

Bežný import:

```python
import numpy as np
```

## Generovanie náhodných čísel

Modul `numpy.random` obsahuje nástroje na generovanie pseudonáhodných hodnôt.

Metóda `randint()` môže vygenerovať náhodné celé čísla:

```python
np.random.randint(5, 200, size=6)
```

Parametre znamenajú:

- `5` – dolná hranica, ktorá sa môže vygenerovať,
- `200` – horná hranica, ktorá sa už nevygeneruje,
- `size=6` – počet vygenerovaných hodnôt.

Generované hodnoty preto patria do intervalu:

```text
5 až 199
```

Ide o interval zapísaný matematicky ako:

```text
[5, 200)
```

## DataFrame s náhodnými hodnotami

```python
df = pd.DataFrame({
    "city": [
        "Bratislava",
        "Košice",
        "Žilina",
        "Bratislava",
        "Košice",
        "Žilina",
    ],
    "year": [2023, 2023, 2023, 2024, 2024, 2024],
    "sales": np.random.randint(5, 200, size=6),
})
```

Stĺpec `sales` bude obsahovať šesť pseudonáhodných celých čísel.

## Seed a opakovateľné výsledky

Počítačové generátory bežne vytvárajú pseudonáhodné čísla. Ich výsledky vychádzajú z počiatočného stavu generátora.

Pomocou seedu môžeme zabezpečiť, aby sme pri každom spustení dostali rovnakú postupnosť hodnôt:

```python
np.random.seed(42)
```

Číslo `42` je ľubovoľne zvolená počiatočná hodnota.

```python
np.random.seed(42)

df = pd.DataFrame({
    "city": [
        "Bratislava",
        "Košice",
        "Žilina",
        "Bratislava",
        "Košice",
        "Žilina",
    ],
    "year": [2023, 2023, 2023, 2024, 2024, 2024],
    "sales": np.random.randint(5, 200, size=6),
})
```

Seed je užitočný napríklad:

- pri opakovaní experimentov,
- pri testovaní,
- pri porovnávaní výsledkov,
- pri delení dát v strojovom učení.

### Modernejší spôsob práce s generátorom

Vo webinári sme používali `np.random.seed()` a `np.random.randint()`. V novšom kóde NumPy odporúča vytvoriť samostatný generátor:

```python
rng = np.random.default_rng(42)
sales = rng.integers(5, 200, size=6)
```

Oba prístupy je užitočné poznať, pretože starší zápis sa stále nachádza v mnohých projektoch a návodoch.

## Vlastný index DataFrame

Pri vytvorení `DataFrame` môžeme určiť vlastný index:

```python
np.random.seed(42)

df = pd.DataFrame({
    "city": [
        "Bratislava",
        "Košice",
        "Žilina",
        "Bratislava",
        "Košice",
        "Žilina",
    ],
    "year": [2023, 2023, 2023, 2024, 2024, 2024],
    "sales": np.random.randint(5, 200, size=6),
    "cost": np.random.randint(20, 150, size=6),
}, index=["A", "A", "B", "B", "B", "C"])
```

Index nemusí byť jedinečný. V tomto príklade sa hodnoty `A` a `B` opakujú.

Ak cez `loc` vyberieme opakujúcu sa hodnotu indexu, pandas vráti všetky zodpovedajúce riadky.

## Výber pomocou `loc`

`loc` pracuje primárne s označeniami riadkov a stĺpcov. Môže pracovať aj s boolean podmienkami.

Všetky riadky s označením `A`:

```python
df.loc["A"]
```

Hodnoty stĺpca `city` pre riadky s indexom `A`:

```python
df.loc["A", "city"]
```

Rozsah označení od `A` po `C` a stĺpec `city`:

```python
df.loc["A":"C", "city"]
```

Rozsah riadkov aj stĺpcov:

```python
df.loc["A":"C", "city":"cost"]
```

Vybrané indexy a vybrané stĺpce:

```python
df.loc[["A", "C"], ["city", "sales"]]
```

Vybrané indexy a všetky stĺpce od začiatku po `sales`:

```python
df.loc[["A", "C"], :"sales"]
```

Pri labelovom rozsahu v `loc` sa zahŕňa začiatočná aj koncová hodnota, ak sa v indexe nachádzajú.

## Výber pomocou `iloc`

`iloc` pracuje s číselnými pozíciami riadkov a stĺpcov.

Prvý riadok:

```python
df.iloc[0]
```

Prvé dva riadky:

```python
df.iloc[:2]
```

Všetky riadky okrem posledného:

```python
df.iloc[:-1]
```

Pri `iloc` sa pozície počítajú od nuly.

Rozsah `0:2` preto vyberie pozície `0` a `1`, ale pozíciu `2` už nie.

## Boolean filtrovanie

Riadky, ktorých predaj je vyšší ako `100`:

```python
df.loc[df["sales"] > 100]
```

Výraz:

```python
df["sales"] > 100
```

vytvorí boolean `Series` s hodnotami `True` a `False`.

`loc` následne vyberie iba riadky, pri ktorých je výsledkom `True`.

Rovnaký filter môžeme zapísať aj skrátene:

```python
df[df["sales"] > 100]
```

## Prvé a posledné riadky

Prvých päť riadkov:

```python
df.head()
```

Alternatívne:

```python
df.iloc[:5]
```

Posledných päť riadkov:

```python
df.tail()
```

Alternatívne:

```python
df.iloc[-5:]
```

Metódy `head()` a `tail()` sú pri bežnom prezeraní dát čitateľnejšie. `iloc` je užitočný pri všeobecnejšom pozičnom výbere.

## Rozdiel medzi pozíciou a označením indexu

Riadok na pozícii `10`:

```python
df.iloc[10]
```

Keďže sa pozície počítajú od nuly, ide o jedenásty riadok.

Riadok, ktorého index má označenie `10`:

```python
df.loc[10]
```

Tieto výrazy môžu vrátiť rovnaký riadok pri štandardnom `RangeIndex`, ale pri vlastnom indexe môžu predstavovať úplne odlišné riadky.

## Výber jedného stĺpca

Všetky hodnoty stĺpca `SaleCondition`:

```python
df.loc[:, "SaleCondition"]
```

Výsledkom je pandas `Series`.

Ak chceme zachovať výsledok ako `DataFrame`, názov stĺpca odovzdáme v zozname:

```python
df.loc[:, ["SaleCondition"]]
```

## Výber stĺpca podľa pozície

Stĺpec na pozícii `2`:

```python
df.iloc[:, 2]
```

Výsledkom je `Series`.

Ak chceme `DataFrame`, pozíciu odovzdáme v zozname:

```python
df.iloc[:, [2]]
```

## Výber rozsahu riadkov cez `loc`

Riadky s indexovými označeniami od `5` po `15`:

```python
df.loc[5:15]
```

Pri `loc` sa koncová hodnota `15` zahŕňa, ak sa v indexe nachádza.

## Výber konkrétnych riadkov a stĺpcov

```python
df.loc[
    [3, 5, 7],
    ["MSZoning", "Street", "LandContour"],
]
```

Týmto vyberieme:

- riadky s indexovými označeniami `3`, `5` a `7`,
- stĺpce `MSZoning`, `Street` a `LandContour`.

## Kombinácia `loc` a `iloc`

Najskôr vyberieme riadky podľa indexových označení:

```python
df.loc[[3, 5, 7]]
```

Z výsledku potom vyberieme prvé tri stĺpce podľa ich pozície:

```python
df.loc[[3, 5, 7]].iloc[:, :3]
```

Každá operácia vytvorí medzivýsledok, nad ktorým sa vykoná nasledujúca operácia.

## Kombinácia podmienky a pozičného výberu

Úloha:

> Nájsť domy predané v roku 2009 a z výsledku vybrať každý tretí riadok.

Najskôr vytvoríme podmienku:

```python
df["YrSold"] == 2009
```

Vyfiltrujeme vyhovujúce riadky:

```python
df.loc[df["YrSold"] == 2009]
```

Z vyfiltrovaného výsledku vyberieme každý tretí riadok:

```python
df.loc[df["YrSold"] == 2009].iloc[::3]
```

## Slicing

Zápis:

```python
start:stop:step
```

obsahuje:

- `start` – počiatočnú pozíciu,
- `stop` – koncovú pozíciu, ktorá sa pri pozičnom slicingu nezahŕňa,
- `step` – veľkosť kroku.

Každý tretí riadok:

```python
df.iloc[::3]
```

Prázdna hodnota pred prvou dvojbodkou znamená začiatok a prázdna hodnota medzi dvojbodkami znamená koniec dát.

## Zoradenie hodnôt

Metóda `sort_values()` zoradí `DataFrame` podľa zvoleného stĺpca.

Zoradenie podľa plochy pozemku:

```python
df.sort_values("LotArea")
```

Parameter `ascending` určuje smer zoradenia.

Od najmenšej hodnoty po najväčšiu:

```python
df.sort_values("LotArea", ascending=True)
```

Hodnota `True` je predvolená.

Od najväčšej hodnoty po najmenšiu:

```python
df.sort_values("LotArea", ascending=False)
```

Textové stĺpce sa môžu zoradiť abecedne.

## Päť domov s najväčším pozemkom

Najskôr zoradíme dáta zostupne:

```python
df.sort_values("LotArea", ascending=False)
```

Potom vyberieme prvých päť riadkov:

```python
df.sort_values("LotArea", ascending=False).iloc[:5]
```

Nakoniec vyberieme požadované stĺpce:

```python
df.sort_values("LotArea", ascending=False).iloc[:5].loc[
    :,
    ["MSZoning", "SalePrice", "LotArea"],
]
```

Jednotlivé operácie sa vykonávajú zľava doprava:

```text
zoradenie
→ výber prvých piatich riadkov
→ výber požadovaných stĺpcov
```

## Zmena hodnôt v DataFrame

Všetky hodnoty stĺpca `MSZoning` môžeme zmeniť na `1`:

```python
df.loc[:, "MSZoning"] = 1
```

Týmto prepíšeme celý stĺpec.

## Priradenie objektu Series do stĺpca

```python
df.loc[:, "MSZoning"] = pd.Series(list(range(1, 6)))
```

Najskôr vznikne zoznam:

```python
list(range(1, 6))
```

Výsledok:

```python
[1, 2, 3, 4, 5]
```

Zo zoznamu sa vytvorí pandas `Series`, ktorého predvolený index je `0` až `4`.

Pri priradení `Series` pandas zarovnáva hodnoty podľa indexu. Ak má `DataFrame` štandardný index:

- riadky s indexom `0` až `4` dostanú hodnoty `1` až `5`,
- ostatné riadky nemajú zodpovedajúcu hodnotu v `Series`,
- preto dostanú chýbajúcu hodnotu `NaN`.

Pri vlastnom indexe môže byť výsledok odlišný, pretože pandas porovnáva indexové označenia, nie iba poradie hodnôt.

## Dôležité zhrnutie

### `loc`

- výber primárne podľa označení indexu a názvov stĺpcov,
- podporuje boolean filtrovanie,
- pri labelovom rozsahu zahŕňa aj koncovú hodnotu,
- číslo v `loc` predstavuje označenie indexu, nie automaticky pozíciu.

### `iloc`

- výber podľa celočíselných pozícií,
- pozície začínajú od nuly,
- používa bežné pravidlá Python slicingu,
- koncová pozícia rozsahu sa nezahŕňa.

Zjednodušene:

```text
loc  → označenia a hodnotové podmienky
iloc → číselné pozície
```

## Užitočné zdroje

- [Pandas – indexing and selecting data](https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html)
- [NumPy – `random.randint`](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randint.html)
- [Pandas API on Spark](https://spark.apache.org/docs/latest/api/python/reference/pyspark.pandas/)