# Webinar 29 – Úprava DataFrame v pandas

Na webinári sme pokračovali v práci s knižnicou pandas. Venovali sme sa vytváraniu a odstraňovaniu stĺpcov, transformácii hodnôt, pridávaniu riadkov a úprave indexu.

## Zobrazenie názvov stĺpcov

Atribút `columns` vráti názvy všetkých stĺpcov objektu `DataFrame`.

```python
df.columns
```

Výsledkom je objekt `Index`. Ak potrebujeme obyčajný Python zoznam, môžeme použiť:

```python
df.columns.tolist()
```

## Vytvorenie nového stĺpca

Nový stĺpec môžeme vytvoriť priradením hodnoty pod nový názov.

### Priradenie skalárnej hodnoty

```python
df["X"] = 0
```

Do všetkých riadkov stĺpca `X` sa uloží hodnota `0`.

- skalár predstavuje jednu hodnotu,
- vektor predstavuje viac hodnôt usporiadaných v jednom rozmere.

### Priradenie zoznamu hodnôt

Ak má `DataFrame` 1460 riadkov, môžeme mu priradiť zoznam rovnakej dĺžky:

```python
df["X"] = list(range(1460))
```

Stĺpec bude obsahovať hodnoty od `0` po `1459`.

Pri priraďovaní obyčajného zoznamu musí jeho dĺžka zodpovedať počtu riadkov. V opačnom prípade pandas vyvolá chybu.

### Priradenie objektu Series

```python
df["Y"] = pd.Series(range(1459))
```

Objekt `Series` sa pri priradení zarovnáva podľa indexu. Riadky, ku ktorým sa nepriradí žiadna hodnota, dostanú chýbajúcu hodnotu `NaN`.

## Prístup k stĺpcu cez bodku

Ak má stĺpec jednoduchý platný názov bez medzier, niekedy k nemu môžeme pristupovať cez bodku:

```python
df.X
```

Odporúčaný a univerzálnejší zápis je však:

```python
df["X"]
```

Hranaté zátvorky fungujú aj pri názvoch s medzerami, špeciálnymi znakmi alebo názvoch, ktoré sa zhodujú s existujúcimi metódami pandas.

## Vytvorenie stĺpca z existujúceho stĺpca

Nový stĺpec môžeme vypočítať z hodnôt iného stĺpca.

Nasledujúci príklad prepočíta rozlohu pozemku zo štvorcových stôp na metre štvorcové:

```python
df["LotArea_sqm"] = df["LotArea"] * 0.092903
```

Pandas vykoná násobenie nad každou hodnotou stĺpca `LotArea`.

Vybrané stĺpce môžeme následne zobraziť a zoradiť:

```python
df[["LotArea_sqm", "LotArea"]].sort_values("LotArea_sqm")
```

`sort_values()` predvolene zoraďuje hodnoty vzostupne, teda od najmenšej po najväčšiu.

Pre zoradenie od najväčšej hodnoty použijeme:

```python
df[["LotArea_sqm", "LotArea"]].sort_values(
    "LotArea_sqm",
    ascending=False,
)
```

## Transformácia hodnôt pomocou `apply()`

Metóda `apply()` umožňuje aplikovať funkciu na každú hodnotu objektu `Series`.

Najskôr môžeme vytvoriť klasickú funkciu:

```python
def is_big(value):
    if value > 9000:
        return "Big"
    return "Small"
```

Funkciu následne aplikujeme na celý stĺpec:

```python
df["LotArea"].apply(is_big)
```

Výsledok môžeme uložiť do nového stĺpca:

```python
df["Is_Big"] = df["LotArea"].apply(is_big)
```

## Použitie lambda funkcie

Jednoduchú funkciu môžeme zapísať aj ako lambda výraz:

```python
df["LotArea"].apply(
    lambda value: "Big" if value > 9000 else "Small"
)
```

Lambda funkcia je vhodná pre krátku jednorazovú operáciu. Pri zložitejšej logike je prehľadnejšia klasická pomenovaná funkcia.

## Podmienené hodnoty pomocou `np.where()`

Na jednoduché podmienené vytváranie hodnôt môžeme použiť funkciu `where()` z knižnice NumPy:

```python
np.where(
    df["LotArea"] > 9000,
    "Big",
    "Small",
)
```

Funkcia dostane:

1. podmienku,
2. hodnotu použitú pri splnení podmienky,
3. hodnotu použitú pri nesplnení podmienky.

Výsledok môžeme uložiť do nového stĺpca:

```python
df["Is_Big"] = np.where(
    df["LotArea"] > 9000,
    "Big",
    "Small",
)
```

Pri jednoduchých podmienkach je `np.where()` často vhodnejšie a výkonnejšie než `apply()` s vlastnou Python funkciou.

## Vytvorenie viacerých stĺpcov cez `assign()`

Metóda `assign()` umožňuje vytvoriť alebo upraviť viac stĺpcov v jednom volaní:

```python
new_df = df.assign(
    LotArea_sqm=df["LotArea"] * 0.092903,
    Z=1,
    YY=1,
)
```

`assign()` štandardne vráti nový `DataFrame`. Pôvodný `df` zostane nezmenený, pokiaľ výsledok nepriradíme späť:

```python
df = df.assign(
    LotArea_sqm=df["LotArea"] * 0.092903,
    Z=1,
    YY=1,
)
```

## Pridávanie nových riadkov

Pripravíme si jednoduchý `DataFrame`:

```python
data = {
    "MSSubClass": [20, 60, 70],
    "MSZoning": ["RL", "RM", "RL"],
    "LotArea": [8450, 9600, 11250],
    "Street": ["Pave", "Pave", "Grvl"],
    "Neighborhood": ["CollgCr", "Veenker", "Crawfor"],
    "SalePrice": [208500, 181500, 223500],
}

df = pd.DataFrame(data)
```

Výsledok:

| index | MSSubClass | MSZoning | LotArea | Street | Neighborhood | SalePrice |
|------:|-----------:|----------|--------:|--------|--------------|----------:|
| 0 | 20 | RL | 8450 | Pave | CollgCr | 208500 |
| 1 | 60 | RM | 9600 | Pave | Veenker | 181500 |
| 2 | 70 | RL | 11250 | Grvl | Crawfor | 223500 |

Nový dom môžeme reprezentovať slovníkom:

```python
new_house = {
    "MSSubClass": 20,
    "MSZoning": "RL",
    "LotArea": 10000,
    "Street": "Pave",
    "Neighborhood": "CollgCr",
    "SalePrice": 200000,
}
```

Riadok pridáme pomocou `loc` a označenia nového indexu:

```python
df.loc[10] = new_house
```

Číslo `10` je označenie indexu, nie desiata pozícia v tabuľke.

Výsledný index môže vyzerať takto:

```text
0, 1, 2, 10
```

### Pridanie riadka na koniec

Počet riadkov získame z prvej hodnoty `shape`:

```python
df.shape[0]
```

Pri jednoduchom indexe môžeme nový riadok pridať na koniec:

```python
df.loc[len(df)] = new_house
```

Tento postup je vhodný najmä vtedy, keď index tvorí súvislý rozsah od `0`. Pri indexe s medzerami alebo vlastnými označeniami treba dávať pozor, aby sme neprepísali existujúci riadok.

## Obnovenie indexu

Metóda `reset_index()` vytvorí nový číselný index.

```python
df.reset_index()
```

Pôvodný index sa predvolene uloží do nového stĺpca s názvom `index`.

Ak ho nechceme zachovať, použijeme:

```python
df.reset_index(drop=True)
```

Táto operácia štandardne vráti nový `DataFrame`. Pôvodný `df` zostane nezmenený.

Výsledok môžeme priradiť späť:

```python
df = df.reset_index(drop=True)
```

Alebo môžeme použiť operáciu na pôvodnom objekte:

```python
df.reset_index(drop=True, inplace=True)
```

## Odstraňovanie stĺpcov

Stĺpec môžeme odstrániť pomocou `drop()`:

```python
df.drop(columns=["Street"])
```

Bez uloženia výsledku zostane pôvodný `df` nezmenený.

Trvalú zmenu môžeme vykonať priradením:

```python
df = df.drop(columns=["Street"])
```

Alebo pomocou `inplace=True`:

```python
df.drop(columns=["Street"], inplace=True)
```

Naraz môžeme odstrániť aj viac stĺpcov:

```python
df.drop(
    columns=["Street", "Neighborhood"],
    inplace=True,
)
```

## Osi v pandas

`DataFrame` má dve osi:

- `axis=0` predstavuje riadky a index,
- `axis=1` predstavuje stĺpce.

Odstránenie stĺpca pomocou osi:

```python
df.drop(["MSSubClass"], axis=1)
```

Odstránenie riadka s indexom `0`:

```python
df.drop([0], axis=0)
```

Pri názvoch stĺpcov je často čitateľnejšie použiť parameter `columns`:

```python
df.drop(columns=["MSSubClass"])
```

## Odstránenie stĺpca pomocou `del`

Stĺpec môžeme odstrániť aj príkazom `del`:

```python
del df["LotArea"]
```

Táto operácia priamo zmení pôvodný `DataFrame` a odstránený stĺpec nevracia.

## Odstránenie a získanie stĺpca pomocou `pop()`

Metóda `pop()` odstráni jeden stĺpec a zároveň ho vráti ako objekt `Series`:

```python
removed_sale_price = df.pop("SalePrice")
```

Po operácii:

- stĺpec `SalePrice` už nebude v `df`,
- jeho pôvodné hodnoty budú uložené v `removed_sale_price`.

`pop()` pracuje so stĺpcom, nie s riadkom.

## Odstránenie duplicitných riadkov

Duplicitné riadky odstránime pomocou:

```python
df.drop_duplicates()
```

Metóda predvolene vráti nový `DataFrame`. Pôvodný môžeme prepísať:

```python
df = df.drop_duplicates()
```

Alebo použiť:

```python
df.drop_duplicates(inplace=True)
```

Podľa potreby môžeme kontrolovať duplicity iba vo vybraných stĺpcoch:

```python
df.drop_duplicates(
    subset=["MSZoning", "LotArea"],
    inplace=True,
)
```

## Zhrnutie

Na úpravu `DataFrame` sme použili:

- `df.columns` na zobrazenie názvov stĺpcov,
- priradenie cez `df["column"]` na vytvorenie alebo zmenu stĺpca,
- `apply()` na aplikovanie funkcie na hodnoty stĺpca,
- lambda funkcie na krátke transformácie,
- `np.where()` na vektorové podmienené hodnoty,
- `assign()` na vytvorenie viacerých stĺpcov,
- `loc` na pridanie alebo zmenu riadka podľa indexu,
- `reset_index()` na vytvorenie nového indexu,
- `drop()` a `del` na odstránenie riadkov alebo stĺpcov,
- `pop()` na odstránenie a získanie stĺpca,
- `drop_duplicates()` na odstránenie duplicitných riadkov.

Pri práci s pandas treba vždy sledovať, či operácia:

- vracia nový objekt,
- alebo priamo mení pôvodný `DataFrame` pomocou `inplace=True`.