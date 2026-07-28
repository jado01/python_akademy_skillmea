# Webinar 27 – Základy práce s dátami v pandas

## Kaggle a použitý dataset

[Kaggle](https://www.kaggle.com/) je platforma, na ktorej sa nachádzajú datasety, dátové projekty, súťaže a notebooky zamerané na dátovú analýzu a strojové učenie.

Počas webinára sme používali dataset **House Prices – Advanced Regression Techniques**, ktorý obsahuje informácie o nehnuteľnostiach a ich predajných cenách.

Pracovali sme so súborom:

```text
train.csv
```

Pred samotnou analýzou je dôležité pochopiť:

- čo jednotlivé riadky predstavujú,
- čo znamenajú jednotlivé stĺpce,
- v akých jednotkách sú hodnoty uložené,
- ktoré hodnoty môžu chýbať,
- aké dátové typy sa nachádzajú v jednotlivých stĺpcoch.

Pochopenie významu dát je jedným z prvých krokov každej dátovej analýzy.

## Chýbajúce hodnoty

V dátovej analýze sa často stretávame s označeniami `NA` a `NaN`.

- `NA` všeobecne označuje chýbajúcu alebo nedostupnú hodnotu – *Not Available*.
- `NaN` znamená *Not a Number*. V pandas sa často používa aj na označenie chýbajúcej číselnej hodnoty.

Chýbajúca hodnota môže napríklad znamenať, že daný údaj nebol vyplnený alebo že sa na konkrétny záznam nevzťahuje.

## Spojité a diskrétne dáta

### Spojité dáta

Spojité dáta môžu nadobúdať veľké množstvo hodnôt v určitom rozsahu.

Príklady:

- cena,
- teplota,
- výška,
- hmotnosť,
- plocha.

### Diskrétne dáta

Diskrétne dáta nadobúdajú oddelené, presne určené hodnoty.

Príkladom je stĺpec `MSSubClass`, ktorý označuje triedu budovy pomocou jednej z vopred definovaných hodnôt.

## Import knižnice pandas

Najskôr importujeme knižnicu pandas. Bežne sa používa skratka `pd`:

```python
import pandas as pd
```

## Kontrola dostupných súborov

V Jupyter notebooku môžeme skontrolovať súbory v aktuálnom priečinku:

```python
!ls
```

Znak `!` umožňuje spustiť príkaz operačného systému priamo z bunky notebooku.

## Načítanie CSV súboru

CSV súbor načítame do objektu `DataFrame`:

```python
df = pd.read_csv("train.csv")
```

Premenná `df` teraz obsahuje tabuľkové dáta zo súboru `train.csv`.

## Základné informácie o DataFrame

### Typ objektu

Pomocou funkcie `type()` zistíme typ objektu:

```python
type(df)
```

Výsledkom je pandas `DataFrame`.

### Rozmery DataFrame

Atribút `shape` vráti počet riadkov a stĺpcov:

```python
df.shape
```

Výsledkom je tuple v tvare:

```text
(počet_riadkov, počet_stĺpcov)
```

Hodnoty môžeme rozbaliť do samostatných premenných:

```python
n_rows, n_cols = df.shape
```

- `n_rows` obsahuje počet riadkov,
- `n_cols` obsahuje počet stĺpcov.

### Prvé riadky

Metóda `head()` štandardne zobrazí prvých päť riadkov:

```python
df.head()
```

Môžeme určiť aj vlastný počet:

```python
df.head(10)
```

### Posledné riadky

Metóda `tail()` štandardne zobrazí posledných päť riadkov:

```python
df.tail()
```

Aj tu môžeme zadať vlastný počet:

```python
df.tail(10)
```

### Názvy stĺpcov

Atribút `columns` vráti názvy všetkých stĺpcov:

```python
df.columns
```

Nepoužívame okrúhle zátvorky, pretože `columns` je atribút, nie metóda.

### Súhrnné informácie

Metóda `info()` zobrazí základné informácie o DataFrame:

```python
df.info()
```

Uvidíme napríklad:

- počet riadkov,
- názvy stĺpcov,
- počet neprázdnych hodnôt,
- dátové typy stĺpcov,
- približnú spotrebu pamäte.

## Dátové typy v pandas

Dátové typy v pandas sa môžu odlišovať od bežných typov v Pythone.

Medzi časté typy patria:

- `int64` – celé čísla,
- `float64` – desatinné čísla,
- `object` – často textové alebo zmiešané hodnoty,
- `bool` – hodnoty `True` a `False`.

Ak sa v číselnom stĺpci nachádzajú chýbajúce hodnoty, pandas môže použiť typ `float64`, aj keď ostatné hodnoty vyzerajú ako celé čísla.

Pandas pri práci s číselnými dátami na pozadí využíva knižnicu NumPy.

Dátové typy všetkých stĺpcov zobrazíme pomocou:

```python
df.dtypes
```

Typ konkrétneho stĺpca môžeme zistiť napríklad takto:

```python
df.dtypes["MoSold"]
```

## Výber jedného stĺpca

Ku konkrétnemu stĺpcu môžeme pristúpiť pomocou hranatých zátvoriek:

```python
df["MSSubClass"]
```

Názov stĺpca zapisujeme ako textový reťazec.

Ak má stĺpec vhodný názov bez medzier a špeciálnych znakov, môžeme použiť aj bodkovú notáciu:

```python
df.MSSubClass
```

Zápis s hranatými zátvorkami je však všeobecnejší a spoľahlivejší.

Výber jedného stĺpca týmto spôsobom vráti objekt `Series`:

```python
type(df["MSSubClass"])
```

Výsledok:

```text
pandas.core.series.Series
```

`Series` predstavuje jeden stĺpec s vlastnými hodnotami a indexom.

Aj nad objektom `Series` môžeme používať metódy `head()` a `tail()`:

```python
df["MSSubClass"].head(10)
df["MSSubClass"].tail()

df["PoolQC"].head()
df["PoolQC"].tail(12)
```

## Výber viacerých stĺpcov

Viacero stĺpcov vyberieme pomocou zoznamu ich názvov:

```python
df[["PoolQC", "PoolArea"]]
```

Zoznam môžeme najskôr uložiť do premennej:

```python
column_list = ["PoolQC", "PoolArea"]
df[column_list]
```

Dôležitý rozdiel:

```python
df["PoolQC"]
```

vráti `Series`, zatiaľ čo:

```python
df[["PoolQC"]]
```

vráti `DataFrame` s jedným stĺpcom.

Vnútorné hranaté zátvorky predstavujú zoznam požadovaných stĺpcov.

## Vlastnosti objektu Series

Jeden stĺpec môžeme uložiť do premennej:

```python
col = df["PoolQC"]
```

Následne môžeme zisťovať jeho vlastnosti:

```python
type(col)
col.name
col.dtype
col.index
```

Príklady výsledkov:

```text
'PoolQC'
dtype('O')
RangeIndex(start=0, stop=1460, step=1)
```

Ak neurčíme vlastný index, pandas vytvorí `RangeIndex`:

- začína od `0`,
- zvyšuje sa o `1`,
- končí pred hodnotou zodpovedajúcou počtu riadkov.

Objekt `Series` môžeme previesť na bežný Python zoznam:

```python
df["LotArea"].tolist()
```

## Filtrovanie podľa hodnôt

Porovnanie stĺpca s hodnotou vytvorí sériu hodnôt `True` a `False`:

```python
df["SalePrice"] > 200000
```

Každá hodnota hovorí, či daný riadok spĺňa podmienku.

Boolean sériu následne môžeme použiť na filtrovanie DataFrame:

```python
df[df["SalePrice"] > 485000]
```

Pri filtrovaní môžeme používať operátory:

- `>` – väčšie ako,
- `<` – menšie ako,
- `>=` – väčšie alebo rovné,
- `<=` – menšie alebo rovné,
- `==` – rovné,
- `!=` – nerovné.

## Zložené podmienky

Najskôr môžeme vytvoriť jednoduchú podmienku:

```python
df["SaleType"] == "WD"
```

Počet riadkov, ktoré ju spĺňajú, zistíme pomocou:

```python
(df["SaleType"] == "WD").sum()
```

Hodnota `True` sa pri sčítaní správa ako `1`, preto výsledok predstavuje počet vyhovujúcich riadkov.

Viac podmienok spojíme operátorom `&`, ktorý znamená logické „a zároveň“:

```python
df[
    (df["SaleType"] == "WD")
    & (df["SalePrice"] > 200000)
]
```

Jednotlivé podmienky musia byť v okrúhlych zátvorkách.

Podmienky môžeme uložiť aj samostatne:

```python
cond1 = df["SaleType"] == "WD"
cond2 = df["SalePrice"] > 200000

df[cond1 & cond2]
```

Pri boolean filtrovaní v pandas sa často používajú:

- `&` – obe podmienky musia platiť,
- `|` – musí platiť aspoň jedna podmienka,
- `~` – negácia podmienky.

## Negácia podmienky

Znak `~` obráti výsledok podmienky:

```python
df[
    ~(df["SaleType"] == "WD")
    & (df["SalePrice"] > 200000)
]
```

Výsledkom budú domy:

- ktorých typ predaja nie je `WD`,
- a zároveň majú cenu vyššiu ako `200000`.

## Metóda `isin()`

Metóda `isin()` overuje, či sa hodnota nachádza medzi zadanými možnosťami:

```python
df[df["SalePrice"].isin([200000, 230000])]
```

Výsledok obsahuje riadky, ktorých hodnota `SalePrice` je `200000` alebo `230000`.

## Výber pomocou `loc`

`loc` slúži na výber riadkov a stĺpcov podľa ich označení, teda podľa názvov indexov a stĺpcov.

Základný tvar:

```python
df.loc[riadky, stĺpce]
```

Všetky riadky a dva vybrané stĺpce:

```python
df.loc[:, ["MSSubClass", "MSZoning"]]
```

Dvojbodka `:` na mieste riadkov znamená „vyber všetky riadky“.

Výber riadkov s indexmi od `3` po `6`:

```python
df.loc[3:6, ["MSSubClass", "MSZoning"]]
```

Pri `loc` je pri tomto type indexu zahrnutá aj koncová hodnota `6`.

## Výber pomocou `iloc`

`iloc` slúži na pozičný výber. Pracuje s číselnými pozíciami riadkov a stĺpcov, nie s ich názvami.

Základný tvar:

```python
df.iloc[pozície_riadkov, pozície_stĺpcov]
```

Prvé dva riadky a prvé dva stĺpce:

```python
df.iloc[0:2, 0:2]
```

Prvých šesť riadkov a stĺpce na pozíciách `2`, `3`, `4` a `5`:

```python
df.iloc[:6, [2, 3, 4, 5]]
```

Pri pozičnom rozsahu v `iloc` sa koncová pozícia nezahŕňa. Rozsah `0:2` teda vyberie pozície `0` a `1`.

V `iloc` nepoužívame názvy stĺpcov. Pristupujeme k nim iba podľa ich číselnej pozície.

## Rozdiel medzi `loc` a `iloc`

- `loc` vyberá podľa názvov alebo označení indexu a stĺpcov.
- `iloc` vyberá podľa číselných pozícií.
- Pri rozsahu v `loc` sa koncové označenie spravidla zahŕňa.
- Pri rozsahu v `iloc` sa koncová pozícia nezahŕňa.