---
theme: default
paginate: true
header: 'Lecture 6 - Dataklasser og type annoteringer programmering'
footer: 'Henrik Finsberg - 09.09.22'
marp: true
---


# Lecture 6 - Dataklasser og type annoteringer
Henrik Finsberg - 09.09.22

---

## Sjekk fra forrige time

* Hva kalles `p`?
    ```python
    p = Person(name="Henrik")
    ```
* Hva er `self`?
    ```python
    class Person:
        def __init__(self, name):
            self.name = name
    ```
* Hva kaller vi `name` ?
    ```python
    print(p.name)
    ```

---

## Svar

* En instans
* `self` er instansen
* Et atributt (data atributter + metoder)

---

* Hva skjer med en metode om vi skriver `@property` på linjen over metoden?
    ```python
    class Sphere:
        @property
        def radius(self):
            ...
    ```

* Hva er fordelen med properties?
* Hvordan kan man gjøre en instans av en klasse kallbar?

---

* Metoden blir omgjort til et data atributt som kun er lesbar (ikke skrivbar)
* Vi kan sørge for at oppdaterte variabler blir brukt. Vi kan sørge for at data atributter ikke kan endres. Vi kan gjemme bort komplisert kode. Vi kan også implemeter en *setter* metode hvis vi ønsker å gjøre data atributtet skrivbart (og legge til eventuelle tester for gyldig input)
* Implementere en spesiell metode `__call__`.

---

## Mål for dagens forelesning

* Type annoteringer (type hints)
    - Hva er det
    - Hvordan bruker man det
    - Hvorfor vi bør bruke det
    - `mypy` - statisk type sjekker
* Dataklasser
    - Klasser med mange ferdige utfylte metoder (f.eks `__str__` or `__init__`)
    - Bruker type annoteringer

---

## `type` lar oss sjekke typen til en variabel

```python
class Person:
    pass


x = 42
y = "42"
p = Person()
print(f"{type(x) = }")
print(f"{type(y) = }")
print(f"{type(p) = }")
```
* En annen måte å si dette på (i Python) er at `x` er en instans av klassen `int` eller `p` er en instans av klassen `Person`

---

## Vi kan sjekke om et objekt er en instans av en klasse ved å bruke `isinstance`

```python
print(f"{isinstance(x, int) = }")  # True
print(f"{isinstance(x, str) = }")  # False
print(f"{isinstance(p, Person) = }")  # True
print(f"{isinstance(p, (int, Person)) = }")  # True
```

---

## Denne informasjonen er kun tilgjengelig når vi kjører koden (*at runtime*)

* I mange andre programmeringsspråk (f.eks C++) må typen kunne bestemmes før programmet kjører (*at compile time*)
* Slike språk kalles statisk typede / skrevne (statically typed languages)
    - Statisk betyr at typen til en variable kan ikke endre seg (med noen få unntak)
* I python kan vi fint endre typen til en variable
    ```python
    x = "Hello"
    x = 42
    x += 1
    ```
* Python kalles et dynamisk typet / skrevet språk (dynamically typed language)

---

## Vi kan spesifisere typen ved hjelp av type annoteringer

Dette gjøres ved å spesifisere typen etter variablenavnet og ett kolon
```python
class Person:
    pass


pi: float = 3.142
name: str = "Henrik"
p: Person = Person()
```

---

## Type annoteringer for funksjoner

```python
def circumference(radius: float) -> float:
    return 2 * pi * radius
```

* Her burkes `->` for å spesifisere retur type.
* Typen til arugmenter spesifiseres med kolon etterfulgt av typen

---

## Merk at type annoteringer ikke endrer typen når vi kjører programmet

* Du kan fint skrive feil type, og programmet vil forstatt kjøre
* Type annoteringer ekvivalent med kommentarer
* Så hva er vitsen?

---

## Hvorfor bruke type annoteringer?

* Dokumentasjon
    ```python
    class Person:
        def __init__(self, name, age, email):
            self.name = name
            self.age = age
            self.email = email
    ```
    vs
    ```python
    class Person:
        def __init__(self, name: str, age: int, email: Email) -> None:
            self.name = name
            self.age = age
            self.email = email
    ```
    Så finner du plutselig ut at det finnes en klasse `Email`

---

```python
class Email:
    def __init__(self, value: str) -> None:
        self._value = value

    @property
    def as_str(self) -> str:
        return self._value

    @property
    def username(self) -> str:
        return self._value.split("@")[0]

    @property
    def domain(self) -> str:
        return self._value.split("@")[1]
```

---

* Du får bedre hjelp fra editoren din. Prøv
    ```python
    class Person:
        def __init__(self, name: str, age: int, email: Email) -> None:
            self.name = name
            self.age = age
            self.email = email  # Prøv å skriv email. og se hva du får å muligheter
    ```
* Du kan bruke en statisk type sjekker (`mypy`) for å sjekke typene, samt til å fange opp feil i koden uten å faktisk kjøre koden

---

## Installere `mypy`

Du kan installere `mypy` med `pip`

```
python3 -m pip install mypy
```
Deretter kan du kjøre `mypy` på en enkelt fil
```
mypy file.py
```

---

## `mypy` for første gang

* Kjør `mypy` på følgende fil
    ```python
    # file.py
    pi: float = 3.14
    ```
* Prøv å endre typen til noe annet og kjør `mypy` igjen. Får du en feilmelding?

---


## Funksjoner som ikke returnerer noe skal ha retur type `None`

```python
def print_hello(name: str, hello: str = "Hello") -> None:
    print(f"{hello} {name}")
```

---

## Typer for lister og dictionary finner in `typing` module

```python
from typing import List, Dict

# Liste av typen str
names: List[str] = ["Ken", "Donna", "John"]
# Dictionary med keys av typen str og values av typen int
age_dict: Dict[str, int] = {
    "Barbara": 23,
    "Ken": 43,
    "Kim": 21,
    "John": 31,
    "Donna": 19,
}
```


---

## Kontrollspørsmål

Hva er typen til disse variablene?

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
```

* Veldig vaskelig å si :)

---

Hva med nå?

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    @property
    def courses(self):
        return list(self.grades.keys())
```

* `grades` er i det minste noe som har to metoder `.values` og `.keys`
* Vi vet fortsatt ikke hva `name` skal være, men det er kanskje opplagt ut i fra navnet?

---

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    @property
    def average_grade(self):
        return sum(self.grades.values()) / len(self.grades)

    @property
    def courses(self):
        return list(self.grades.keys())


s = Student(
    name="Henrik",
    grades={
        "Calculus 1": 5,
        "Physics": 4,
        "IN1910": 6,
        "Ex Phil": 3,
    },
)
```

---


## Svar

```python
from typing import List, Dict


class Student:
    def __init__(self, name: str, grades: Dict[str, int]) -> None:
        self.name = name
        self.grades = grades

    @property
    def average_grade(self) -> float:
        return sum(self.grades.values()) / len(self.grades)

    @property
    def courses(self) -> List[str]:
        return list(self.grades.keys())


s = Student(
    name="Henrik",
    grades={
        "Calculus 1": 5,
        "Physics": 4,
        "IN1910": 6,
        "Ex Phil": 3,
    },
)
```

---

## Alternativ for python3.9+

```python
class Student:
    def __init__(self, name: str, grades: dict[str, int]) -> None:
        self.name = name
        self.grades = grades

    @property
    def average_grade(self) -> float:
        return sum(self.grades.values()) / len(self.grades)

    @property
    def courses(self) -> list[str]:
        return list(self.grades.keys())


s = Student(
    name="Henrik",
    grades={
        "Calculus 1": 5,
        "Physics": 4,
        "IN1910": 6,
        "Ex Phil": 3,
    },
)
```

---

## Type annoteringer er god dokumentasjon

```python
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
```

vs

```python
class Student:
    def __init__(self, name: str, grades: Dict[str, int]) -> None:
        self.name = name
        self.grades = grades
```

---

## Annet eksempel

Her lager vi en liste av strenger (`List[str]`) og en dictionary hvor nøklene er strenger og verdiene er heltall (`Dict[str, int]`)

```python
from typing import Dict, List


def extract_ages_from_dict(age_dict: Dict[str, int], names: List[str]) -> List[int]:
    ages = []
    for name in names:
        if name in age_dict:
            ages.append(age_dict[name])

    return ages


names = ["Ken", "Donna", "John"]
age_dict = {"Barbara": 23, "Ken": 43, "Kim": 21, "John": 31, "Donna": 19}
ages = extract_ages_from_dict(age_dict, names)
# ages = [43, 19, 31]
```

---

## La oss prøve å legge på type annoteringer på denne klassen

```python
import datetime


class Person:
    def __init__(self, name, year_born):
        self.name = name
        self.year_born = year_born

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name}, year_born={self.year_burn})"

    def age_this_year(self):
        return datetime.datetime.now().year - self.year
```

---

## Kjør `mypy` for å sjekke at alt er i orden

```python
import datetime


class Person:
    def __init__(self, name: str, year_born: int) -> None:
        self.name = name
        self.year_born = year_born

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name}, year_born={self.year_burn})"

    def age_this_year(self) -> int:
        return datetime.datetime.now().year - self.year
```

---

## Mypy gir oss beskjed om at noe er galt

```
$ mypy person.py
person.py:10: error: "Person" has no attribute "year_burn"; maybe "year_born"?
person.py:13: error: "Person" has no attribute "year"
Found 2 errors in 1 file (checked 1 source file)
```

* Her har vi lagt inn noen skrivefeil med vilje, og vi ser at `mypy` fanger opp disse!
* Dette hadde ikke blitt fanget opp med mindre man hadde skrevet tester.

---

## Hvis en variable kan være flere typer bruker vi `Union`

```python
import datetime
from typing import Union


def compute_age_this_year(year_born: Union[int, str]) -> int:
    this_year = datetime.datetime.now().year
    if isinstance(year_born, str):
        return this_year - int(year_born)
    else:
        return this_year - year_born
```

---

Denne funksjonen kan brukes på to måter. Ved å sende inn et heltall
```python
compute_age_this_year(1999)
```
eller en streng
```python
compute_age_this_year("1999")
```
`year_born` er derfor av typen `Union[int, str]`.

* Merk i python3.10+ kan man skrive
    ```python
    def compute_age_this_year(year_born: int | str) -> int:
        ...
    ```

---

## Et veldig typisk eksempel er at en variabel er enten en spesifikk type eller `None`

```python
from typing import Union


def print_hello(name: str, city: Union[str, None] = None) -> None:
    msg = f"Hello {name}"
    if city is not None:
        msg += f" from {city}"
    print(msg)


print_hello("Henrik")  # prints 'Hello Henrik'
print_hello("Henrik", "Oslo")  # prints 'Hello Henrik from Oslo'
```

---

## Dette er så vanlig at du istedenfor kan bruke `Optional`

```python
from typing import Union


def print_hello(name: str, city: Optional[str] = None) -> None:
    msg = f"Hello {name}"
    if city is not None:
        msg += f" from {city}"
    print(msg)


print_hello("Henrik")  # prints 'Hello Henrik'
print_hello("Henrik", "Oslo")  # prints 'Hello Henrik from Oslo'
```
Altså
```python
Union[str, None] = Optional[str]
```

---

## Er det noe galt med funksjonen i dette eksempelet?

```python
from typing import Dict


def extract_name_and_capitalize(data: Dict[str, str]) -> str:
    name = data.get("name")
    return name.capitalize()


person = {"name": "henrik", "age": "35", "city": "oslo"}
print(extract_name_and_capitalize(person))
```
* Prøv å kjøre `mypy`

---

## `dict.get` returner en default verdi hvis nøkkelen ikke finnes

Med andre ord `data.get("name")` returnerer `None` dersom `name` ikke er en nøkkel i dictionarien.

* To måter å løse dette på
* Vi kan sende inn en default verdi som er en streng
    ```python
    data.get("name", "Ola Normann")
    ```
* Eller vi kan håndtere tilfelle hvor `data.get("name")` returnerer `None`.

---

I så fall må funksjonen returnerer `Optional[str]`

```python
from typing import Dict, Optional


def extract_name_and_capitalize(data: Dict[str, str]) -> Optional[str]:
    name = data.get("name")
    if name is None:
        return None
    return name.capitalize()


person1 = {"name": "henrik", "age": "35", "city": "oslo"}
print(extract_name_and_capitalize(person1))  # prints 'Henrik'
person2 = {"age": "40"}
print(extract_name_and_capitalize(person2))  # prints None
```

---

Klare for ett komplisert eksempel? Hva er galt her

```python
from typing import Dict, List, Optional


def extract_name_and_capitalize(data: Dict[str, str]) -> Optional[str]:
    name = data.get("name")
    if name is None:
        return None
    return name.capitalize()


def count_letters_in_names(names: List[str]) -> int:
    return sum(len(name) for name in names)


data = [
    {"name": "henrik"},
    {"name": "johannes"},
    {"name": "ada"},
]

names = []
for d in data:
    name = extract_name_and_capitalize(d)
    names.append(name)

print(count_letters_in_names(names))
```

---

I linjen
```python
name = extract_name_and_capitalize(d)
```
kan `name` potensielt være `None`, som vil si at listen `names` potensielt kan inneholde `None`. Det kan potensielt bli et problem om man sender denne inn til `count_letters_in_names`.

* En mulig fiks er a sjekke om `name` er `None` før man legger den til i lista.

---

## Dataklasser

Klasser med (noen) ferdig utyfyle spesielle metoder

---

## Dataklasser er klasser hvor innholdet typisk er data

Men det er ikke noe krav til dette.

For eksempel

```python
class Student:
    def __init__(self, name: str, grades: Dict[str, int]) -> None:
        self.name = name
        self.grades = grades
```

kan skrives om til

```python
from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grades: Dict[str, int]
```

---

## Dataklasser kommer med en del ferdige metoder

Blant annet

* `__init__` (for å initialisere instansen)
* `__repr__` (for å printe)
* `__eq__`  (for å sjekke om to instanser er like)
    ```python
    s1 = Student("Henrik", {"Calculus": 5})
    s2 = Student("Henrik", {"Calculus": 5})
    print(s1 == s2)
    ```

* Merk at for å bruke dataklasser er vi nødt til å bruke type annoteringer (nok en grunn til å lære seg å bruke dem!)

---

## Dataklasser er vanlige klasser

Eneste forskjellen er at vi får en del metoder implementert gratis. Det betyr at vi også kan legge til vanlige metoder på klassen

```python
from dataclasses import dataclass
from typing import Dict


@dataclass
class Student:
    name: str
    grades: Dict[str, int]

    @property
    def average_grade(self) -> float:
        return sum(self.grades.values()) / len(self.grades)

    @property
    def courses(self) -> list[str]:
        return list(self.grades.keys())


s = Student(
    name="Henrik",
    grades={
        "Calculus 1": 5,
        "Physics": 4,
        "IN1910": 6,
        "Ex Phil": 3,
    },
)
print(s)
```

---

## Dataklasser med default verdier

Vi kan også sette default verdier

```python
import typing
from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    email: typing.Optional[str] = None
    cellphone: typing.Optional[str] = None


p1 = Contact(name="Eirill")
p2 = Contact(name="Henrik", email="henriknf@simula.no")
p3 = Contact(name="Elon", email="elon@musk.com", cellphone="81549300")
```

* Her settes `email` og `cellphone` til `None` hvis de ikke gitt

---

## Rekkefølgen på argumentene

```python
import typing
from dataclasses import dataclass


@dataclass
class Contact:
    name: str
    email: typing.Optional[str] = None
    cellphone: typing.Optional[str] = None
```
Følgende er ekvivalent
```python
p1 = Contact(name="Elon", email="elon@musk.com", cellphone="81549300")
p2 = Contact("Elon", "elon@musk.com", "81549300")
```
* Men det anbefales å bruke nøkkelordargumenter (keyword arguments), dvs `p1` (hvorfor? - se andre linje i `python -c 'import this'`)

---

## Et alternativ til dataklasser er `NamedTuple`

```python
import typing


class ContactNT(typing.NamedTuple):
    name: str
    email: typing.Optional[str] = None
    cellphone: typing.Optional[str] = None


p_dc = Contact(name="Elon", email="elon@musk.com", cellphone="81549300")
p_nt = ContactNT(name="Elon", email="elon@musk.com", cellphone="81549300")
print(p_dc)
print(p_nt)
```

---

## Forskjeller mellom `NamedTuple` og dataklasser

* `NamedTuple` er immutable, mens datklasser er ikke det (selv om det finnes måter å gjøre dataklasser immutable på også)
    ```python
    p_dc.email = "Elon Musk"  # Fungerer
    p_nt.email = "Elon Musk"  # Fungerer ikke
    ```
* På samme måte kan vi også sette dynamiske attributter
    ```python
    p_dc.new_attribute = 42  # Fungerer
    p_nt.new_attribute = 42  # Fungerer ikke
    ```
* `NamedTuple` er et tuple, så vi kan skrive følgende
    ```python
    name, email, cellphone = p_nt
    ```

---

## Så `NamedTuple`, dataklasser eller vanlige klasser?

* Prøv først `NamedTuple`. Hvis det ikke er nok (for eksempel at du trenger dynamiske atributter) kan du prøve dataklasser, og hvis det ikke er nok kan du bruke en vanlig klasse
* Fordelen med en vanlig klasse er at du slipper å importere noe (og det fungerer også med eldre versjoner av python)
* Ulempen er at du må skrive mer kode og det er også flere fordeler med å bruke objecter som ikke kan endres etter at de er laget. Hvorfor?

---

## Mål for dagens forelesning

* Type annoteringer (type hints)
    - Hva er det
    - Hvordan bruker man det
    - Hvorfor vi bør bruke det
    - `mypy` - statisk type sjekker
* Dataklasser
    - Klasser med mange ferdige utfylte metoder (f.eks `__str__` or `__init__`)
    - Bruker type annoteringer
