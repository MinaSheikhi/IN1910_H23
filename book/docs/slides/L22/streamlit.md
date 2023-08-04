---
theme: default
paginate: true
header: 'Lecture 22 - streamlit'
footer: 'Henrik Finsberg - 11.11.22'
marp: true
---

# Lecture 22 - streamlit
Henrik Finsberg - 11.11.22

---

## Mål for dagens forelesning

* Lære hvordan vi kan bygge en interaktiv applikasjon med `streamlit`

---

## Interaktiv visualiserings-applikasjon

* Noen ganger ønsker vi å utforske dataene våre
* Dette kan man gjøre ved å plotte en haug med figurer
* Eller man kan bruke jupyter notebooks
* Hvis du kun ønsker å vise dataene fram til noen som ikke kan kode, er det ofte bedre med en applikasjon som gjemmer bort detaljene

---

## Verktøy for å bygge interaktive visualiseringer

* [Dash](https://dash.plotly.com/)
    - Bygger på plotly.
* [Voilà](https://voila.readthedocs.io/en/stable/)
    - Gjør om jupyter notebooks til web applikasjoner
* [Streamlit](https://streamlit.io)
    - Dette skal vi se nærmere på i dag

---

## Installere `streamlit`

Du kan installere `streamlit` med pip
```
python3 -m pip install streamlit
```

---

## Kjøre en demo applikasjon

```
streamlit hello
```

---

## Dataset

- Vi skal bruke et dataset fra [Kaggle](https://www.kaggle.com)
- Kaggle er et sted som arrangerer konkuranser og legger ut flere datasett.
- Vi skal se på et datasett med data over hjertesvikt pasienter
- https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction
- Her kan dere også sjekke ut [forslag til analyser som er sendt inn](https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction/code?datasetId=1582403&sortBy=voteCount)

---

## Demonstrajon av hva vi skal bygge
Vis hvordan appen vi skal bygge ser ut

---

## Lag en ny fil og start `streamlit`

Lag `app.py` og kjør streamlit med
```
streamlit run app.py
```
Importer streamlit og bruk `st.write` til å skrive noe

---

## La en tittel og en tekst

```python
st.title("Heart Failure Prediction Dataset")
st.text("This is a web app to allow exploration of Heart failure Data")
```

---

## Og litt mer info om datasettet


```python
st.header("Dataset")
st.markdown(
    """
This dataset is taken from
https://www.kaggle.com/datasets/fedesoriano/heart-failure-prediction

At Kaggle, several authors publish their own code where they
have analyzed the different datasets.

For example, the following review https://www.kaggle.com/code/durgancegaur/a-guide-to-any-classification-problem/notebook
is a pretty good one.
"""
)
```

---

## Last inn dataene i pandas og skriv ut litt info

```python
import pandas as pd

df = pd.read_csv("heart.csv")

st.header("Statistics of Dataframe")
st.write(df.describe())
```

---


## Lag et sidebar for ulike sider

- Vi kan lage en sidebar som vi kan bruke til å navigere mellom ulik sider

```python
st.sidebar.title("Navigation")
options = st.sidebar.radio(
    "Select what you want to display:",
    [
        "About",
        "Data Summary",
    ],
)
```

---

## Implementer de ulike sidene som funksjoner

Hvis option er "About" vises about siden og hvis options er "Data summary" vises statistikk om DataFramen

* Implementer en ny side som viser "head" av DataFramen

---

```python
if options == "About":
    show_about_page()
elif options == "Data Summary":
    show_data_summary_page()
elif options == "Data Header":
    show_data_header_page()
```

---

## Plotting med matplotlib

Lag en side hvor du plotter `"Age"` vs `"MaxHR"` i matplotlib.
Bruk `st.pyplot` for å sende figuren til streamlit.

---

```python
def plot_mpl():
    st.header("Plot of Data")

    fig, ax = plt.subplots()
    ax.scatter(x=df["Age"], y=df["MaxHR"])
    ax.grid()
    ax.set_xlabel("Age")
    ax.set_ylabel("MaxHR")

    st.pyplot(fig)
```

---

## Plotting med plotly express

[`plotly`](https://plotly.com/python/) can brukes for å lage mer interactive plots. Plotly kommer også med en pakke som heter `plotly.express` som er litt enklere å komme i gang med

* Lag et plot der du plotter et histogram over alder med plotly express og lag en tilhørende side som du kaller "Histogram".

* Hint:
    ```python
    import plotly.express as px
    plot = px.histogram(df, x="Age")
    st.plotly_chart(plot)
    ```

---

### Legg til en selectbox

Vi ønsker å kunne plotte histogram over alle kolonner.
* Lag en selectbox hvor mulighetene er all kolonnene i DataFramen

* Hint:
    ```python
    column = st.selectbox("Select column", options=df.columns)
    ```

---

```python
def histogram(df):
    st.header("Histogram")

    column = st.selectbox("Select column", options=df.columns)
    plot = px.histogram(df, x=column)
    st.plotly_chart(plot , use_container_width=True)
```

---

## Lag et plot som plotter to kolonner

- La brukeren velge hvilken kolonne som skal være på x- og y-aksen.
- La også brukeren få velge om det skal være et scatter-plot eller et box-plot
* Hint: Du kan bruke `px.scatter(df, x=x, y=y)` og `px.box(df, x=x, y=y)`

---

```python
def two_columns(df):
    col1, col2 = st.columns(2)

    x_axis_val = col1.selectbox("Select the X-axis", options=df.columns)
    y_axis_val = col2.selectbox("Select the Y-axis", options=df.columns)

    plot_type = st.selectbox("Select plot type", options=["scatter", "box"])

    if plot_type == "scatter":
        plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    elif plot_type == "box":
        plot = px.box(df, x=x_axis_val, y=y_axis_val)

    st.plotly_chart(plot, use_container_width=True)
```

---

## Lag en side med Pairplot

* Vi kan bruke `seaborn` til å lage et Pairplot
* Lag også en selectbox er du kan velge hvilken kolonne som besemmer fargen
* Hint:
    ```python
    grid = sns.pairplot(df, hue=column)
    st.pyplot(grid.fig)
    ```

---

## Mål for dagens forelesning

* Lære hvordan vi kan bygge en interaktiv applikasjon med `streamlit`
