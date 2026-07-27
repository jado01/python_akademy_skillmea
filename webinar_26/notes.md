# Webinar 26 – JupyterLab a prvá dátová analýza

## Pokračovanie práce s JupyterLab

### Odstránenie a vystrihnutie bunky

Klávesové skratky používame v príkazovom režime. Do príkazového režimu sa môžeme prepnúť klávesom `Esc`.

- `D D` – odstráni vybranú bunku,
- `X` – vystrihne vybranú bunku,
- `C` – skopíruje vybranú bunku,
- `V` – vloží bunku pod aktuálnu bunku.

`X` teda nie je priamo príkaz na odstránenie. Bunku vystrihne a môžeme ju následne vložiť na iné miesto.

### Pozastavenie vykonávania programu

Modul `time` poskytuje funkcie na prácu s časom.

```python
import time

time.sleep(10)
```

Funkcia `time.sleep(10)` pozastaví vykonávanie aktuálneho kódu približne na 10 sekúnd.

Počas čakania je kernel zaneprázdnený a ďalšie požiadavky na vykonanie kódu musia počkať.

### Terminál v JupyterLab

JupyterLab obsahuje vlastný terminál. Môžeme ho otvoriť priamo v rozhraní JupyterLab bez toho, aby sme museli ukončiť server a vracať sa do pôvodného terminálu.

V termináli môžeme napríklad:

- pracovať so súbormi a priečinkami,
- používať Git,
- spúšťať Python,
- inštalovať potrebné knižnice.

Pri inštalácii balíkov treba dávať pozor, aby sme ich nainštalovali do rovnakého virtuálneho prostredia, ktoré používa kernel notebooku.

## Typy buniek

Jupyter notebook používa tri základné typy buniek:

1. Code
2. Markdown
3. Raw

Typ bunky môžeme zmeniť pomocou ponuky v hornej lište notebooku.

### Code

Do bunky typu Code zapisujeme programový kód.

Pri použití Python kernelu sa po spustení bunky kód odošle Python kernelu, vykoná sa a výsledok sa zobrazí pod bunkou.

```python
print("Hello")
```

### Markdown

Markdown bunka slúži na zapisovanie formátovaného textu.

Notebook preto môže kombinovať:

- vysvetlenie problému,
- nadpisy a zoznamy,
- ukážky kódu,
- spustiteľný programový kód,
- tabuľky, grafy a výsledky.

To je jedna z hlavných výhod Jupyter notebookov. Najprv môžeme používateľovi vysvetliť, čo sa bude vykonávať, a potom pod vysvetlenie pridať kód a jeho výsledok.

#### Základné formátovanie Markdownu

Nadpisy:

```markdown
# Nadpis prvej úrovne
## Nadpis druhej úrovne
### Nadpis tretej úrovne
#### Nadpis štvrtej úrovne
```

Tučné a šikmé písmo:

```markdown
**Tučný text**

*Šikmý text*
```

Nečíslovaný zoznam:

```markdown
- položka 1
- položka 2
```

Číslovaný zoznam:

```markdown
1. položka 1
2. položka 2
```

Ukážka kódu:

````markdown
```python
print("Hello")
```
````

Kompletný príklad Markdown bunky:

````markdown
# This is a heading

Here is some text.

## This is a smaller heading

Here is another text.

### This is an even smaller heading

**This is bold text.**

*This is italic text.*

#### List

- item 1
- item 2

1. first item
2. second item

```python
print("Hello")
```
````

### Raw

Raw bunka obsahuje nespracovaný text.

Jej obsah sa:

- nevykonáva ako programový kód,
- nevykresľuje ako Markdown,
- môže použiť pri exporte notebooku do iných formátov.

## IPython magic príkazy a shell príkazy

Python notebook bežne používa IPython kernel. Ten okrem Pythonu podporuje aj špeciálne magic príkazy.

### Magic príkazy

Riadkové magic príkazy začínajú znakom `%`.

```python
%pwd
%ls
```

- `%pwd` zobrazí aktuálny pracovný priečinok,
- `%ls` zobrazí obsah aktuálneho priečinka.

Nejde o štandardnú syntax Pythonu ani o obyčajné CMD príkazy. Sú to špeciálne príkazy poskytované IPythonom.

### Shell príkazy

Znak `!` odošle príkaz systémovému shellu.

```python
!ls
```

Dostupné shell príkazy sa môžu líšiť podľa operačného systému a používaného shellu.

Balík môžeme zo spustenej bunky nainštalovať napríklad pomocou:

```python
%pip install pandas
```

V notebooku je vhodnejšie používať `%pip` než `!pip`, pretože `%pip` inštaluje balík do prostredia aktuálneho kernelu.

Po inštalácii niektorých balíkov môže byť potrebné reštartovať kernel.

## Export notebooku

Jupyter notebook môžeme exportovať do rôznych formátov, napríklad:

- HTML,
- Markdown,
- Python súbor,
- PDF.

Na export sa používa napríklad nástroj `nbconvert`.

Export do PDF môže vyžadovať dodatočné závislosti. Klasický PDF export používa LaTeX, zatiaľ čo WebPDF export používa HTML a prehliadač Chromium prostredníctvom nástroja Playwright.

---

## Prvá dátová analýza

### Zdroje dát

Na dátovú analýzu potrebujeme údaje. Tie môžu pochádzať z rôznych zdrojov.

#### Databázy

Aplikácia sa môže pripojiť k databáze a načítať potrebné údaje.

Databázy môžu používať napríklad:

- SQL technológie – relačné databázy,
- NoSQL technológie – dokumentové, kľúčovo-hodnotové a ďalšie typy databáz.

Pripojenie sa zvyčajne realizuje pomocou databázového klienta, ovládača alebo knižnice.

#### Exportované súbory

Údaje môžeme dostať ako pripravený export, napríklad:

- CSV,
- JSON,
- XML,
- Excel,
- Parquet.

Takýto súbor si uložíme do počítača a pracujeme s ním lokálne.

#### Message brokery a dátové streamy

Údaje môžu prichádzať priebežne prostredníctvom nástrojov, ako sú:

- RabbitMQ,
- Apache Kafka.

Takýto spôsob sa používa najmä pri udalostiach a dátach prichádzajúcich v reálnom čase.

## CSV

CSV znamená **Comma-Separated Values**.

Je to jednoduchý textový formát určený na ukladanie tabuľkových údajov.

Typický CSV súbor:

```csv
name,age,city
Jana,28,Bratislava
Peter,35,Kosice
```

Vlastnosti CSV:

- jednotlivé záznamy sú uložené v riadkoch,
- hodnoty sú oddelené oddeľovačom,
- tradičným oddeľovačom je čiarka,
- v niektorých súboroch sa používa bodkočiarka alebo iný znak,
- súbor neuchováva formátovanie buniek, vzorce ani grafiku,
- môžeme ho otvoriť v textovom editore, tabuľkovom programe alebo načítať pomocou pandas.

CSV nie je Excel súbor, aj keď oba formáty dokážu reprezentovať tabuľkové údaje.

CSV býva jednoduchý a prenositeľný formát. Pri veľkých dátach však nemá vždy najmenšiu veľkosť. Formáty ako Parquet môžu ukladať tabuľkové dáta efektívnejšie.

## Knižnica pandas

Na prácu s tabuľkovými dátami budeme používať knižnicu pandas.

Ak ju nemáme nainštalovanú, môžeme ju v notebooku nainštalovať:

```python
%pip install pandas
```

Následne ju importujeme pod zaužívanou skratkou `pd`:

```python
import pandas as pd
```

## DataFrame

Tabuľka v pandas sa nazýva `DataFrame`.

CSV súbor môžeme načítať takto:

```python
df = pd.read_csv("iris.csv")
```

- `pd.read_csv()` prečíta CSV súbor,
- vytvorí z neho objekt `DataFrame`,
- premenná `df` odkazuje na načítaný DataFrame.

Cesta `"iris.csv"` sa vyhodnocuje vzhľadom na aktuálny pracovný priečinok. Súbor preto musí byť na správnom mieste alebo musíme uviesť správnu cestu.

V Jupyter notebooku môžeme DataFrame zobraziť tak, že na posledný riadok bunky napíšeme:

```python
df
```

IPython ho zobrazí ako formátovanú tabuľku.

## Prvé a posledné riadky

Prvé riadky DataFrame zobrazíme pomocou:

```python
df.head()
```

Posledné riadky zobrazíme pomocou:

```python
df.tail()
```

Bez argumentu obe metódy štandardne zobrazia päť riadkov.

Počet môžeme zmeniť:

```python
df.head(10)
df.tail(3)
```

## Ďalšie dátové formáty

pandas nepodporuje iba CSV. Obsahuje funkcie na načítanie rôznych formátov a zdrojov, napríklad:

```python
pd.read_json(...)
pd.read_excel(...)
pd.read_html(...)
pd.read_parquet(...)
pd.read_sql(...)
```

Niektoré formáty môžu vyžadovať doinštalovanie ďalšej knižnice.

## Vizualizácia pomocou Matplotlib

pandas dokáže vytvárať grafy pomocou knižnice Matplotlib.

Ak ju nemáme nainštalovanú:

```python
%pip install matplotlib
```

Následne importujeme modul `pyplot` pod zaužívanou skratkou `plt`:

```python
import matplotlib.pyplot as plt
```

Jednoduchý graf z DataFrame môžeme vytvoriť:

```python
df.plot()
```

pandas pri základnom grafe vykreslí číselné stĺpce DataFrame. Typ grafu a zobrazované stĺpce môžeme neskôr upraviť.

Podľa prostredia môžeme graf explicitne zobraziť:

```python
plt.show()
```

Jupyter notebook umožňuje vložiť graf priamo pod bunku s kódom. Vďaka tomu môžeme priebežne vizualizovať medzivýsledky analýzy.

## Datasety na internete

Jedným zo známych zdrojov datasetov je [Kaggle](https://www.kaggle.com/).

Kaggle obsahuje:

- verejné datasety,
- notebooky,
- súťaže z dátovej analýzy a strojového učenia,
- komunitné ukážky riešení.

## Zhrnutie

V tejto lekcii sme si ukázali:

- ďalšiu prácu s bunkami v JupyterLab,
- rozdiel medzi Code, Markdown a Raw bunkou,
- základné formátovanie Markdownu,
- IPython magic a shell príkazy,
- možnosti exportu notebooku,
- základné zdroje dát,
- vlastnosti CSV súborov,
- načítanie CSV do pandas DataFrame,
- použitie `head()` a `tail()`,
- vytvorenie jednoduchého grafu pomocou pandas a Matplotlib.

## Oficiálne zdroje

- [Jupyter Notebook – typy buniek](https://jupyter-notebook.readthedocs.io/en/latest/notebook.html)
- [JupyterLab – príkazy a klávesové skratky](https://jupyterlab.readthedocs.io/en/stable/user/commands.html)
- [JupyterLab – terminál](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html)
- [IPython – dokumentácia](https://ipython.readthedocs.io/en/stable/)
- [pandas – úvod](https://pandas.pydata.org/docs/getting_started/index.html)
- [pandas – vizualizácia](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html)
- [nbconvert – export notebookov](https://nbconvert.readthedocs.io/en/stable/)
- Súbor iris.csv poskytol lektor ako cvičný dataset počas webinára 26.