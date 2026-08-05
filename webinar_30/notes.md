# Webinar 30 – View, copy, spájanie DataFrame a chýbajúce hodnoty

Na webinári sme pokračovali v práci s knižnicou pandas. Venovali sme sa bezpečnej úprave hodnôt, rozdielu medzi view a copy, spájaniu viacerých objektov `DataFrame`, typom joinov a práci s chýbajúcimi hodnotami.

## View a copy

Pri výbere časti objektu `DataFrame` je dôležité rozlišovať medzi pohľadom na pôvodné údaje a samostatnou kópiou.

- view môže zdieľať údaje s pôvodným objektom,
- copy predstavuje samostatnú kópiu údajov.

V praxi sa nemáme spoliehať na to, že výsledok výberu bude vždy view alebo vždy copy.

## Bezpečná úprava pôvodného DataFrame

Ak chceme zmeniť hodnoty v pôvodnom `DataFrame`, použijeme jedno priradenie cez `loc`:

```python
df.loc[df["SalePrice"] >= 181500, "SalePrice"] = 0
```

Tento príkaz:

1. vyberie riadky, kde je `SalePrice` väčšia alebo rovná `181500`,
2. vyberie stĺpec `SalePrice`,
3. nastaví vybrané hodnoty na `0`.

Treba sa vyhýbať reťazenému priraďovaniu:

```python
df[df["SalePrice"] >= 181500]["SalePrice"] = 0
```

Takýto zápis najskôr vytvorí dočasný výsledok a následne sa ho pokúsi zmeniť. Pôvodný `DataFrame` sa preto nemusí upraviť. V aktuálnych verziách pandas s Copy-on-Write chained assignment pôvodný objekt neupraví.

## Vytvorenie nezávislého testovacieho DataFrame

Ak chceme údaje skúšobne upravovať bez ovplyvnenia pôvodného `DataFrame`, vytvoríme explicitnú kópiu:

```python
temp = df.loc[df["SalePrice"] >= 181500].copy()
```

Následne môžeme meniť `temp`:

```python
temp.loc[:, "SalePrice"] = 0
```

Zmení sa iba `temp`. Pôvodný `df` zostane nezmenený.

Bezpečné pravidlo:

- úprava pôvodného objektu → jedno priradenie cez `df.loc[...] = ...`,
- nezávislá pracovná verzia → výber zakončený `.copy()`.

---

# Štruktúrované a neštruktúrované dáta

## Štruktúrované dáta

Štruktúrované dáta majú vopred známu organizáciu, napríklad:

- riadky a stĺpce,
- názvy stĺpcov,
- určené dátové typy,
- jasný význam jednotlivých polí.

Príkladom sú tabuľkové údaje v CSV súbore alebo tabuľke relačnej databázy.

CSV súbor však sám osebe nie je relačná databáza. Je to súborový formát na ukladanie tabuľkových dát.

## Neštruktúrované dáta

Neštruktúrované dáta nemajú pevnú tabuľkovú štruktúru. Patria sem napríklad:

- voľný text,
- dokumenty,
- fotografie,
- zvuk,
- video.

## Relačné databázy

Relačné databázy ukladajú dáta do tabuliek. Tabuľky môžu byť prepojené pomocou kľúčov.

Príklad:

- tabuľka zákazníkov,
- tabuľka produktov,
- tabuľka nákupov.

Záznam v tabuľke nákupov môže obsahovať identifikátor zákazníka a produktu. Pomocou týchto identifikátorov sa vytvárajú vzťahy medzi tabuľkami.

## Nerelačné databázy

Nerelačné alebo NoSQL databázy nepoužívajú jeden spoločný relačný tabuľkový model. Môžu pracovať napríklad s:

- dokumentmi,
- pármi kľúč – hodnota,
- grafmi,
- širokými stĺpcami.

Neznamená to, že musia obsahovať iba neštruktúrované dáta alebo že medzi údajmi nemôžu existovať vzťahy.

## Elasticsearch

Elasticsearch je distribuovaný nástroj na vyhľadávanie a analýzu dokumentov. Často sa používa na:

- fulltextové vyhľadávanie,
- analýzu logov,
- vyhľadávanie slov a výrazov,
- prácu s veľkým množstvom textových dokumentov.

---

# Spájanie objektov DataFrame

V pandas môžeme spájať viacero objektov `DataFrame`. Spôsob spojenia závisí od toho, či ich chceme uložiť:

- pod seba ako nové riadky,
- vedľa seba ako nové stĺpce,
- alebo prepojiť podľa indexu či spoločných kľúčov.

## Ukážkové DataFrame

```python
df1 = pd.DataFrame(
    data={
        "a": [1, 2, 1, 2, 1, 2],
        "b": [3, 4, 3, 4, 3, 4],
    }
)

df2 = pd.DataFrame(
    data={
        "a": [1, 3, 1, 3, 1],
        "b": [5, 4, 5, 4, 5],
    }
)
```

## Spojenie pod seba pomocou `concat()`

Funkcia `pd.concat()` predvolene používa `axis=0`, takže objekty spojí pod seba:

```python
result = pd.concat([df1, df2])
```

Pôvodné indexy sa zachovajú. Ak oba objekty začínali indexom `0`, výsledok môže obsahovať duplicitné indexy.

Pri príkaze:

```python
result.loc[0]
```

sa preto môže vrátiť viac riadkov.

## Vytvorenie nového indexu pri spájaní

Najjednoduchšie môžeme nový index vytvoriť už počas spojenia:

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True,
)
```

Výsledný index bude:

```text
0, 1, 2, 3, ...
```

Alternatívou je následné použitie:

```python
result = result.reset_index(drop=True)
```

Alebo:

```python
result.reset_index(drop=True, inplace=True)
```

Bez `drop=True` by sa pôvodný index uložil ako nový stĺpec.

## Spojenie viacerých DataFrame

Do `concat()` môžeme odovzdať viac objektov:

```python
result = pd.concat(
    [df1, df2, df1, df2],
    ignore_index=True,
)
```

Výsledkom je nový spojený objekt. Pri veľkých dátach treba počítať s tým, že výsledok zaberá ďalšiu pamäť, aj keď moderné pandas môžu niektoré kopírovania odkladať pomocou Copy-on-Write.

## Rozdielne stĺpce

Ak jeden `DataFrame` obsahuje stĺpec navyše:

```python
df2["c"] = 1
```

pandas ich stále dokáže spojiť:

```python
result = pd.concat(
    [df1, df2],
    ignore_index=True,
)
```

Riadky pochádzajúce z `df1` nemajú hodnotu pre stĺpec `c`, preto tam pandas doplní `NaN`.

## Spojenie vedľa seba

Ak chceme objekty pripojiť vedľa seba ako stĺpce, použijeme `axis=1`:

```python
result = pd.concat(
    [df1, df2],
    axis=1,
)
```

Pri horizontálnom spájaní pandas zarovnáva riadky podľa indexu.

Ak index v jednom objekte chýba, na danom mieste vznikne `NaN`. Prítomnosť `NaN` môže zároveň spôsobiť zmenu číselného typu, napríklad z `int` na `float`.

## Rovnaké názvy stĺpcov

Pandas môže vytvoriť výsledok aj s duplicitnými názvami stĺpcov. Takýto výsledok však môže byť neprehľadný.

Ak spojíme dva stĺpce s názvom `a`, výber:

```python
result["a"]
```

môže vrátiť viac stĺpcov namiesto jednej `Series`.

Preto je vhodné stĺpce pred spojením premenovať alebo pri joinoch použiť prípony.

---

# Outer a inner spojenie pri `concat()`

Parameter `join` vo funkcii `concat()` podporuje hodnoty:

- `"outer"`,
- `"inner"`.

Predvolená hodnota je `"outer"`.

## Outer join

Outer spojenie zachová zjednotenie označení z oboch objektov.

Pri horizontálnom spojení ide o zjednotenie indexov:

```python
result = pd.concat(
    [df1, df2],
    axis=1,
    join="outer",
)
```

Výsledok obsahuje všetky indexy. Chýbajúce hodnoty sa doplnia ako `NaN`.

Z pohľadu množín outer join predstavuje:

```text
S1 + S2 + S3
```

Teda všetko z ľavej množiny, spoločnú časť aj všetko z pravej množiny.

## Inner join

Inner spojenie zachová iba spoločné označenia:

```python
result = pd.concat(
    [df1, df2],
    axis=1,
    join="inner",
)
```

Pri `axis=1` zostanú iba indexy, ktoré existujú v oboch objektoch.

Z pohľadu množín inner join predstavuje iba spoločnú časť:

```text
S2
```

## Význam `join` závisí od osi

Pri:

```python
pd.concat([df1, df2], axis=0, join="inner")
```

sa objekty ukladajú pod seba a `inner` ponechá iba stĺpce, ktoré majú oba objekty spoločné.

Pri:

```python
pd.concat([df1, df2], axis=1, join="inner")
```

sa objekty ukladajú vedľa seba a `inner` ponechá iba spoločné indexy.

---

# Spájanie pomocou `join()`

Metóda `DataFrame.join()` predvolene spája objekty podľa indexu.

Podporuje napríklad:

- `left`,
- `right`,
- `inner`,
- `outer`.

## Left join

Left join zachová všetky indexy ľavého objektu:

```python
result = df1.join(
    df2,
    rsuffix="_second",
    how="left",
)
```

Z pohľadu množín predstavuje:

```text
S1 + S2
```

Ak v pravom objekte neexistuje zhodný index, jeho hodnoty budú `NaN`.

## Right join

Right join zachová všetky indexy pravého objektu:

```python
result = df1.join(
    df2,
    rsuffix="_second",
    how="right",
)
```

Z pohľadu množín predstavuje:

```text
S2 + S3
```

## Prípony pri rovnakých názvoch

Ak majú oba objekty rovnaké názvy stĺpcov, musíme ich odlíšiť:

```python
result = df1.join(
    df2,
    rsuffix="_second",
    how="left",
)
```

Parameter `rsuffix` pridá príponu ku konfliktným stĺpcom pravého objektu.

K dispozícii je aj `lsuffix` pre ľavý objekt.

Rozdiel medzi základnými nástrojmi:

- `concat()` spája objekty pozdĺž zvolenej osi,
- `join()` spája najmä podľa indexu,
- `merge()` sa používa na databázové spájanie podľa spoločných stĺpcov alebo kľúčov.

---

# Chýbajúce hodnoty

Chýbajúce hodnoty môžu byť reprezentované napríklad ako:

- `NaN`,
- `None`,
- `pd.NA`,
- `NaT` pri dátume a čase.

Chýbajúca hodnota nie je to isté ako číselná nula.

## Vyhľadanie chýbajúcich hodnôt

Metóda `isna()` pre každú bunku vráti:

- `True`, ak hodnota chýba,
- `False`, ak hodnota nechýba.

```python
df.isna()
```

Výsledkom je nový boolean `DataFrame`. Pôvodné dáta sa nemenia.

## Počet chýbajúcich hodnôt v stĺpcoch

Keďže `True` sa pri sčítaní správa ako `1`, môžeme použiť:

```python
df.isna().sum()
```

Výsledkom je `Series` s počtom chýbajúcich hodnôt v každom stĺpci.

Stĺpce s najväčším počtom chýbajúcich hodnôt zobrazíme:

```python
df.isna().sum().sort_values(
    ascending=False
).head(20)
```

## Početnosť jedinečných hodnôt

Metóda `value_counts()` vráti jedinečné hodnoty a počet ich výskytov:

```python
df["Alley"].value_counts()
```

Parameter `dropna` je predvolene nastavený na `True`, takže chýbajúce hodnoty sa nezapočítajú.

Ak ich chceme zahrnúť:

```python
df["Alley"].value_counts(dropna=False)
```

Výsledok môže vyzerať napríklad:

```text
NaN     1369
Grvl      50
Pave      41
```

## Význam chýbajúcej hodnoty závisí od dát

Pri stĺpci `Alley` nemusí `NaN` znamenať chybu merania. Môže znamenať, že dom jednoducho nemá prístup cez uličku.

Pred nahrádzaním alebo odstraňovaním chýbajúcich hodnôt musíme pochopiť význam daného stĺpca.

Možné významy `NaN`:

- hodnota nebola zmeraná,
- údaj nebol vyplnený,
- údaj sa na daný objekt nevzťahuje,
- vlastnosť neexistuje,
- nastala chyba pri importe alebo spracovaní.

---

# Nahradenie chýbajúcich hodnôt

Metóda `fillna()` nahradí chýbajúce hodnoty zadanou hodnotou.

## Číselný stĺpec

Ak chýbajúca plocha garáže znamená, že dom garáž nemá:

```python
df["GarageArea"].fillna(0)
```

Tento zápis iba vráti novú `Series`. Pôvodný stĺpec sa nezmení.

Výsledok preto uložíme späť:

```python
df["GarageArea"] = df["GarageArea"].fillna(0)
```

## Textový stĺpec

`fillna()` môžeme použiť aj pre textové stĺpce:

```python
df["Alley"] = df["Alley"].fillna("No alley")
```

Nie je teda pravda, že `fillna()` možno používať iba na ne-textové stĺpce. Náhradná hodnota však musí dávať význam vzhľadom na obsah a dátový typ stĺpca.

## Viac stĺpcov naraz

Rozdielne hodnoty môžeme určiť pomocou slovníka:

```python
df = df.fillna(
    {
        "GarageArea": 0,
        "Alley": "No alley",
    }
)
```

---

# Zhrnutie

Na webinári sme precvičili:

- bezpečnú zmenu pôvodného `DataFrame` cez jedno priradenie s `loc`,
- vytvorenie nezávislej pracovnej kópie cez `.copy()`,
- rozdiel medzi štruktúrovanými a neštruktúrovanými dátami,
- základný princíp relačných a nerelačných databáz,
- vertikálne a horizontálne spájanie cez `pd.concat()`,
- použitie `axis=0` a `axis=1`,
- vytvorenie nového indexu cez `ignore_index=True`,
- správanie pri rozdielnych stĺpcoch a indexoch,
- outer a inner spojenie,
- left a right join cez `DataFrame.join()`,
- hľadanie chýbajúcich hodnôt cez `isna()`,
- počítanie chýbajúcich hodnôt cez `sum()`,
- analýzu kategórií cez `value_counts()`,
- zahrnutie `NaN` cez `dropna=False`,
- nahrádzanie chýbajúcich hodnôt cez `fillna()`.

## Dôležité pravidlá

- Nepoužívať chained assignment na zmenu pôvodného `DataFrame`.
- Pôvodné údaje meniť jedným priradením cez `loc`.
- Pri nezávislom testovacom výbere použiť `.copy()`.
- Pri `concat(axis=0)` sa spájajú riadky.
- Pri `concat(axis=1)` sa spájajú stĺpce a údaje sa zarovnávajú podľa indexu.
- `outer` predstavuje zjednotenie a `inner` prienik označení.
- `isna()` zisťuje chýbajúce hodnoty, nie číselné nuly.
- Význam `NaN` treba posúdiť podľa významu konkrétneho stĺpca.
- `fillna()` štandardne vracia nový objekt; výsledok treba uložiť.
- `fillna()` funguje pre číselné aj textové stĺpce.

## Oficiálne zdroje

- [Pandas – Copy-on-Write](https://pandas.pydata.org/docs/user_guide/copy_on_write.html)
- [Pandas – ChainedAssignmentError](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html)
- [Pandas – concat](https://pandas.pydata.org/docs/reference/api/pandas.concat.html)
- [Pandas – fillna](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html)