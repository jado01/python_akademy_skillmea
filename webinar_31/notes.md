# Webinar 31 – Dátové typy, chýbajúce hodnoty a GroupBy

## Dátové typy stĺpcov

Každý stĺpec v DataFrame má určitý dátový typ, napríklad:

- `int64` – celé čísla,
- `float64` – desatinné čísla,
- `bool` – logické hodnoty,
- `object` – často textové údaje,
- `datetime64` – dátum a čas.

Dátové typy všetkých stĺpcov zobrazíme pomocou:

```python
df.dtypes
```

Výsledkom je `Series`, v ktorej názvy stĺpcov tvoria index a hodnoty predstavujú ich dátové typy.

Počet stĺpcov jednotlivých dátových typov môžeme zobraziť takto:

```python
df.dtypes.value_counts()
```

---

## Výber číselných a nečíselných stĺpcov

Na výber všetkých číselných stĺpcov môžeme použiť:

```python
df_numeric = df.select_dtypes(include="number")
```

Na výber nečíselných stĺpcov:

```python
df_non_numeric = df.select_dtypes(exclude="number")
```

Tento spôsob je vhodnejší než manuálna kontrola iba dátových typov `int64` a `float64`, pretože DataFrame môže obsahovať aj ďalšie číselné typy.

Obmedzený spôsob pomocou masky by vyzeral napríklad takto:

```python
numeric_columns = (df.dtypes == np.int64) | (df.dtypes == np.float64)
df_numeric = df.loc[:, numeric_columns]
```

Negácia tejto podmienky musí mať správne umiestnené zátvorky:

```python
non_numeric_columns = ~(
    (df.dtypes == np.int64) | (df.dtypes == np.float64)
)

df_non_numeric = df.loc[:, non_numeric_columns]
```

Tento spôsob však zachytí iba konkrétne uvedené dátové typy.

---

# Chýbajúce hodnoty

Chýbajúca hodnota sa v pandas často zobrazuje ako `NaN`.

`NaN` neznamená číslo nula. Znamená, že daná hodnota nie je v datasete dostupná.

## Vyhľadanie chýbajúcich hodnôt

Metóda `isna()` vráti:

- `True`, ak hodnota chýba,
- `False`, ak hodnota nechýba.

```python
df["Alley"].isna()
```

Opakom je metóda `notna()`:

```python
df["Alley"].notna()
```

Tá vráti:

- `True`, ak hodnota existuje,
- `False`, ak hodnota chýba.

Ak chceme zistiť, či stĺpec obsahuje aspoň jednu nechýbajúcu hodnotu:

```python
df["Alley"].notna().any()
```

Ak chceme zistiť, či jednotlivé stĺpce obsahujú aspoň jednu chýbajúcu hodnotu:

```python
df.isna().any()
```

Výsledkom je `Series` s hodnotami `True` alebo `False` pre jednotlivé stĺpce.

---

## Odstránenie chýbajúcich hodnôt

Nasledujúci príkaz odstráni všetky riadky, ktoré obsahujú aspoň jednu chýbajúcu hodnotu:

```python
df.dropna()
```

Odstránenie stĺpcov obsahujúcich aspoň jednu chýbajúcu hodnotu:

```python
df.dropna(axis=1)
```

V pandas označujeme osi takto:

- `axis=0` – riadky,
- `axis=1` – stĺpce.

Metóda `dropna()` pôvodný DataFrame automaticky nezmení. Výsledok preto musíme uložiť:

```python
df = df.dropna()
```

Prípadne môžeme použiť:

```python
df.dropna(inplace=True)
```

Použitie `dropna()` treba dobre zvážiť. Pri odstránení riadkov alebo stĺpcov môžeme prísť o veľké množstvo užitočných údajov.

Môžeme určiť, že chceme odstrániť iba riadky, v ktorých chýbajú všetky hodnoty:

```python
df.dropna(how="all")
```

Alebo môžeme kontrolu obmedziť na konkrétne stĺpce:

```python
df.dropna(subset=["GarageYrBlt"])
```

---

## Vyhľadanie číselných stĺpcov s chýbajúcimi hodnotami

Najskôr vyberieme iba číselné stĺpce:

```python
df_numeric = df.select_dtypes(include="number")
```

Potom zistíme, ktoré z nich obsahujú aspoň jednu chýbajúcu hodnotu:

```python
df_numeric.isna().any()
```

Ak chceme získať iba názvy takýchto stĺpcov:

```python
numeric_columns_with_na = df_numeric.columns[
    df_numeric.isna().any()
]
```

---

## Počet chýbajúcich hodnôt

Počet chýbajúcich hodnôt v konkrétnom stĺpci zistíme pomocou:

```python
df["GarageYrBlt"].isna().sum()
```

Riadky, v ktorých hodnota chýba, môžeme zobraziť takto:

```python
df.loc[df["GarageYrBlt"].isna()]
```

---

# Nahradenie chýbajúcich hodnôt

Chýbajúce hodnoty môžeme za určitých okolností nahradiť vypočítanou hodnotou.

## Priemer

```python
df["GarageYrBlt"].mean()
```

Nahradenie chýbajúcich hodnôt priemerom:

```python
garage_year_mean = df["GarageYrBlt"].mean()

df.loc[
    df["GarageYrBlt"].isna(),
    "GarageYrBlt"
] = garage_year_mean
```

## Medián

Medián predstavuje prostrednú hodnotu zoradených údajov:

```python
garage_year_median = df["GarageYrBlt"].median()

df.loc[
    df["GarageYrBlt"].isna(),
    "GarageYrBlt"
] = garage_year_median
```

Rovnakú operáciu môžeme zapísať aj pomocou `fillna()`:

```python
df["GarageYrBlt"] = df["GarageYrBlt"].fillna(
    df["GarageYrBlt"].median()
)
```

## Minimum a maximum

```python
df["GarageYrBlt"].min()
df["GarageYrBlt"].max()
```

Aj tieto hodnoty môžeme technicky použiť na nahradenie chýbajúcich údajov.

Spôsob nahradenia však musí dávať zmysel vzhľadom na význam dát. Napríklad chýbajúci rok výstavby garáže môže znamenať, že dom žiadnu garáž nemá. Nahradenie priemerným rokom by v takom prípade vytvorilo zavádzajúci údaj.

Pred nahradením chýbajúcich hodnôt preto musíme pochopiť, čo ich neprítomnosť znamená.

---

# GroupBy

`groupby()` slúži na rozdelenie dát do skupín podľa jednej alebo viacerých hodnôt.

Princíp sa označuje ako:

1. **Split** – rozdelenie dát do skupín,
2. **Apply** – vykonanie operácie nad každou skupinou,
3. **Combine** – spojenie výsledkov.

Príkladom môže byť rozdelenie nehnuteľností podľa štvrte a vypočítanie priemernej ceny v každej štvrti.

---

## Zoskupenie podľa jedného stĺpca

Priemerná predajná cena podľa štvrte:

```python
df.groupby("Neighborhood")["SalePrice"].mean()
```

Pandas:

1. rozdelí riadky podľa hodnoty v stĺpci `Neighborhood`,
2. pre každú skupinu vyberie `SalePrice`,
3. vypočíta priemernú cenu,
4. spojí výsledky.

Samotné volanie:

```python
df.groupby("Neighborhood")
```

vráti objekt `DataFrameGroupBy`. Ten reprezentuje pripravené zoskupenie dát, nad ktorým môžeme vykonávať ďalšie operácie.

---

## Výsledok ako DataFrame

Ak chceme, aby názov skupiny zostal bežným stĺpcom:

```python
df.groupby(
    "Neighborhood",
    as_index=False
)["SalePrice"].mean()
```

Rovnaký výsledok môžeme dosiahnuť pomocou `reset_index()`:

```python
df.groupby("Neighborhood")["SalePrice"].mean().reset_index()
```

---

## Viaceré agregačné operácie

Pomocou `agg()` môžeme nad skupinami vykonať viacero výpočtov:

```python
df.groupby("Neighborhood").agg(
    avg_price=("SalePrice", "mean"),
    min_price=("SalePrice", "min"),
    max_price=("SalePrice", "max"),
    total_houses=("SalePrice", "size"),
)
```

V tomto zápise definujeme:

- názov nového výsledného stĺpca,
- pôvodný stĺpec,
- agregačnú operáciu.

---

## Zoskupenie podľa viacerých stĺpcov

Dáta môžeme zoskupiť podľa viacerých hodnôt:

```python
df.groupby(
    ["MSZoning", "BldgType"]
)["SalePrice"].mean()
```

Týmto spôsobom vytvoríme skupiny podľa kombinácie hodnôt v stĺpcoch `MSZoning` a `BldgType`.

---

## Rozdiel medzi `count()` a `size()`

`count()` počíta iba nechýbajúce hodnoty vo vybranom stĺpci:

```python
df.groupby("Neighborhood")["SalePrice"].count()
```

`size()` počíta počet riadkov v každej skupine bez ohľadu na chýbajúce hodnoty:

```python
df.groupby("Neighborhood").size()
```

Ak chceme zistiť počet záznamov v skupine, `size()` býva presnejšou voľbou.

---

# Transformácia skupín

Metóda `transform()` vykoná operáciu nad skupinami, ale výsledok vráti v rovnakej dĺžke ako pôvodný DataFrame.

Priemernú cenu štvrte môžeme pridať ku každému domu:

```python
df["NeighborhoodAvgPrice"] = (
    df.groupby("Neighborhood")["SalePrice"]
    .transform("mean")
)
```

Každý riadok tak dostane priemernú cenu štvrte, do ktorej patrí.

Rozdiel medzi cenou domu a priemerom jeho štvrte:

```python
df["DifferenceFromNeighborhoodAvg"] = (
    df["SalePrice"] - df["NeighborhoodAvgPrice"]
)
```

---

# Filtrovanie skupín

Pomocou `filter()` môžeme ponechať iba skupiny, ktoré spĺňajú určitú podmienku.

Napríklad ponecháme iba štvrte s minimálne 50 nehnuteľnosťami:

```python
df_filtered = df.groupby("Neighborhood").filter(
    lambda group: len(group) >= 50
)
```

Vo výsledku zostanú všetky pôvodné riadky zo skupín, ktoré splnili podmienku.

---

# Cvičenia

## 1. Počet domov v jednotlivých štvrtiach

```python
df.groupby("Neighborhood").size()
```

Výsledok môžeme zoradiť:

```python
df.groupby("Neighborhood").size().sort_values(
    ascending=False
)
```

---

## 2. Priemerná cena domu v každej štvrti

```python
df.groupby("Neighborhood")["SalePrice"].mean()
```

Zoradenie od najvyššej priemernej ceny:

```python
df.groupby("Neighborhood")["SalePrice"].mean().sort_values(
    ascending=False
)
```

---

## 3. Priemerná cena podľa zóny

```python
df.groupby("MSZoning")["SalePrice"].mean()
```

---

## 4. Pre každú štvrť vypíš počet domov, priemernú cenu a priemernú rozlohu pozemku

```python
df.groupby("Neighborhood").agg(
    number_of_houses=("SalePrice", "size"),
    average_price=("SalePrice", "mean"),
    average_lot_area=("LotArea", "mean"),
)
```

Ak chceme výsledok s bežným indexom:

```python
df.groupby("Neighborhood").agg(
    number_of_houses=("SalePrice", "size"),
    average_price=("SalePrice", "mean"),
    average_lot_area=("LotArea", "mean"),
).reset_index()
```

---

## 5. Priemerná cena pre každú kombináciu zóny a typu budovy

```python
df.groupby(
    ["MSZoning", "BldgType"]
)["SalePrice"].mean()
```

Pre prehľadnejší výsledok:

```python
df.groupby(
    ["MSZoning", "BldgType"],
    as_index=False
)["SalePrice"].mean()
```

---

## 6. Priemer štvrte a rozdiel ceny každého domu od priemeru

Najskôr vytvoríme stĺpec s priemernou cenou štvrte:

```python
df["NeighborhoodAvgPrice"] = (
    df.groupby("Neighborhood")["SalePrice"]
    .transform("mean")
)
```

Potom vypočítame rozdiel:

```python
df["DifferenceFromNeighborhoodAvg"] = (
    df["SalePrice"] - df["NeighborhoodAvgPrice"]
)
```

Kladná hodnota znamená, že dom je drahší než priemer štvrte. Záporná hodnota znamená, že je lacnejší.

---

# Zhrnutie

Na webinári sme sa naučili:

- zisťovať dátové typy stĺpcov,
- vyberať číselné a nečíselné stĺpce,
- vyhľadávať chýbajúce hodnoty,
- odstraňovať alebo nahrádzať chýbajúce údaje,
- používať `groupby()` na vytváranie skupín,
- vykonávať agregačné operácie,
- zoskupovať podľa viacerých stĺpcov,
- používať `agg()`, `transform()` a `filter()`,
- vytvárať nové stĺpce založené na skupinových výpočtoch.

Pri práci s chýbajúcimi hodnotami je dôležité nerozhodovať iba podľa technickej možnosti. Najskôr musíme pochopiť význam dát a dôvod, prečo hodnota chýba.