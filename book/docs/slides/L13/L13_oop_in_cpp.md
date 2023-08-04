---
theme: default
paginate: true
header: ' Lecture 13 - Objektorientert programmering i C++'
footer: 'Henrik Finsberg - 05.10.22'
marp: true
---


# Lecture 13 - Objektorientert programmering i C++
Henrik Finsberg - 05.10.22

---

## Kontrollspørsmål fra forrige time

1. Hva er en referanse variabel?
2. Hva er forskjellen på en funksjon der vi bruker *call by value* og en funksjon er vi bruker *call by reference*.
3. Hva er en peker?
4. Hvis vi har en peker som peker på en `int`. Hvordan kan vi hente ut verdien, og hvordan kan vi endre verdien?

---

## Kontrollspørsmål fra forrige time (svar)

* En referansevariabel er et alias for en annen variabel. Endrer man på referanse variabelen endrer man også på den originale variabelen.
    ```c++
    int a = 1.0;
    int &b = a;
    ```
* Når vi bruker *call by value* (`void halve(double x)`) kopieres variabelen når den sendes in i funksjonen, men når vi bruker *call by reference* `void halve(double &x)` brukes en referansevariabel som lar oss endre verdien av variabelen vi sender inn fra funksjonen
* En peker er en variabel hvor verdien er adressen til en annen variabel
   ```c++
   int *p = &a
   ```

---

* Vi må huske å dereferere pekeren først
    ```c++
    int a = 4;
    // En peker som peker på a
    int *p = &a;
    // Hent ut verdien ved å dereferere pekeren
    int b = *p;
    // Endre verdien som pekes på ved å dereferere pekeren
    *p += 1;
    ```
* Hva er verdien av `a` og `b` nå?

---

## Mål for dagens forelesning

Vite
- hvordan man larger klasser (`class`) og strukturer (`struct`)
- forkjellen på  `class`, `struct`
- forskjellen på `public` og `private` variabler
- hva funksjons overlasting (function overloading) er for noe
- hva medlemsinitialiseringslister er for noe

---


* Python
    ```python
    class Person:

        def say_hello(self):
            print("Hello")
    ```
* C++
    ```c++
    #include <iostream>

    class Person
    {
        void say_hello()
        {
            std::cout << "Hello \n";
        }
    };
    ```
* Merk at vi bruker krølleparenteser for å definere hva som er inne i klassen, og siste krølle parentes avsluttes med `;`

---

## Lage en instans av klassen

```c++
#include <iostream>

class Person
{
    void say_hello()
    {
        std::cout << "Hello \n";
    }
};

int main()
{
    Person p;
    p.say_hello();

    return 0;
}
```

* Det er bare et problem. Vi har ikke tilgang til metoden `say_hello`

---

## I klasser er alle medlemmer private, med midre vi spesifiserer annerledes

* At en funksjon er privat betyr at klassen kun kan bruke funksjonen internt

* For å gjøre en funksjon tilgjengelig må vi deklarere den som `public`

    ```C++
    class Person
    {
      public:
        void say_hello()
        {
            std::cout << "Hello \n";
        }
    };
    ```
* `public` kalles for tilgangsspesifikasjon (access specifier)

---

## La oss lage en privat metode som returner ett navn

* Private metoder deklareres ved å bruke tilgangsspesifikasjonen `private`.

* Lag en private metode med signaturen `std::string name()` som returnerer ett generisk navn og bruk denne inne i `say_hello` metoden

---

```C++
class Person
{
  private:
    // Merk at dette er en metode som returnerer en `std::string`
    std::string name()
    {
        return "Ola Normann";
    }

  public:
    void say_hello()
    {
        std::cout << "Hello " << name() << "\n";
    }
};
```

---

## `private` / `public` gjelder fram til neste `public` / `private`

```C++
class Person
{
  private:
    // Alt her er privat
  public:
    // Alt her er offentlig
  private:
    // Alt her er privat igjen
};
```

* Det er også en tilgangsspesifikasjon som heter `protected` men denne vil vi ikke gå igjennom i dette kurset.

---

## En `struct` er en klasse hvor alle medlemsfelt er offentlige som standard
Det vil si at denne koden fungerer
```c++
#include <iostream>

struct Person
{
    void say_hello()
    {
        std::cout << "Hello \n";
    }
};

int main()
{
    Person p;
    p.say_hello();

    return 0;
}
```

---

## Men på samme måte som med klasser kan vi bruke `private` og `public`

```C++
struct Person
{
  private:
    std::string name()
    {
        return "Ola Normann";
    }

  public:
    void say_hello()
    {
        std::cout << "Hello " << name() << "\n";
    }
};
```
---

## Struct vs Class

* `structs` er en datastruktur for å gruppere data
    - Disse finnes også i C (som ikke et objektorientert språk)
    - I C kan ikke structs ha metoder (funksjoner) men det kan de i C++
    - eksisterer hovedsakelig i C++ for at `C++` skal være kompatibel med `C`


* `class` er klasser (omtrent) slik vi kjenner dem i python
    - Brukes typisk når du skal gjøre mer enn å bare gruppere data, dvs lage objekter med egenskaper og oppførsel


---

## Oppgave

* Lag en klasse `Person`. Klassen skal ha
    - to offentlige medlemsvariabler `year_born` av typen `int` og `name` av typen `std::string`.
    - En privat metode `int _compute_age` for å beregne alder
    - En offentlig metode `void print` for printe informasjon om navn og alder

* Jeg liker at private variabler og metoder har navn som starter med `_` slik at det blir mest likt som python.

---

* Kall programmet på følgende måte
    ```c++
    int main()
    {

        Person p;
        p.name = "Henrik";
        p.year_born = 1987;

        p.print();

        return 0;
    }
    ```
---

```C++
#include <iostream>
#include <string>

class Person
{
  private:
    int _compute_age()
    {
        return 2022 - year_born;
    }

  public:
    std::string name;
    int year_born;

    void print()
    {
        int age = _compute_age();
        std::cout << "Person with name " << name << " is ";
        std::cout << age << " years old\n";
    }
};
```

---

## Konstruktører i C++

* Konstruktøren til en klasse er en metode med samme navn som klassen.
* Denne må være public

    ```C++
    class Person
    {
      public:
        Person()
        {
            std::cout << "Calling default constructor\n";
        }
    };
    ```

---

## Vi kan også la konstruktøren ta argumenter med standard verdier

* Gjør medlemsvariablene private og bruk konstruktøren til å sette medlemsvariablene
* Merk at vi må endre navn på medlemsvariablene for å unnge navnekollisjoner


---

```C++
#include <iostream>
#include <string>

class Person
{
  private:
    int _compute_age()
    {
        return 2022 - _year_born;
    }

    std::string _name;
    int _year_born;

  public:
    Person(std::string name = "Henrik", int year_born = 1987)
    {
        _name = name;
        _year_born = year_born;
        std::cout << "Calling default constructor\n";
    }

    void print()
    {
        int age = _compute_age();
        std::cout << "Person with name " << _name << " is ";
        std::cout << age << " years old\n";
    }
};

int main()
{

    Person p;
    p.print();

    return 0;
}
```

---

## Vi kan også sende inn egne argumenter inn til konstruktøren

* Da bruker vi krølleparenteser og sender inn argumentene i den rekkefølgen de er spesifisert i konstruktøren.
* Eksempel
    ```c++
    int main()
    {

        Person p{"Ola", 2002};
        p.print();

        return 0;
    }
    ```

---


## Hvor er `self`?

* C++ har noe som kalles et implisitt selv-refererende system
* Alle variabler som er definert inne klassen er automatisk tilgjengelig
* Det kan derfor være lurt å ha en eller annen konvensjon på hva medlemsvariabler skal hete
    - For eksempel at de starter med `_`, `m_` eller `m` (`m` for *member*)
* Dersom du er nødt til å ha tak i objektet på en eller annen måte kan man bruke `this` som er en peker til objektet.
* Man kan også bruke `this` for å aksessere medlemsvariables ved å bruke `this->radius` for eksempel (noe som heller ikke er uvanlig) - mer om `->` senere.



---

## Oppgave

* Lag en klasse `Circle`. Konstruktøren skal ta inn
    - `radius` av typen `double` som skal være radius i sirkelen
    - `cx` av typen `double` som skal være x-koordinaten til sentrum av sirkelen
    - `cy` av typen `double` som skal være y-koordinaten til sentrum av sirkelen
* Lag en metode `double area()` som beregner arealet av sirkelen
    - Vi må også definiere `PI` (eventuelet bruke `M_PI` fra `math.h`)
    - Vi kan også bruke `pow` fra `cmath` til å kvadrere.
---

```C++
#include <cmath>
#include <iostream>
#include <math.h>

class Circle
{
  private:
    double _radius;
    double _cx;
    double _cy;

  public:
    Circle(double radius, double cx = 0, double cy = 0)
    {
        _radius = radius;
        _cx = cx;
        _cy = cy;
    }
    double area()
    {
        return M_PI * std::pow(_radius, 2);
    }
};

int main()
{

    Circle c{1};
    std::cout << "Area is " << c.area() << "\n";

    return 0;
}
```

---

## Setter og getter metoder

* Setter og getter metoder blir analogt til `@property` i python
* Det er vanlig at disse metodene får navn `get_...` og `set_...`
* Implementer en metode `void set_radius(double)` som setter radiusen og en metode `double get_radius()` som henter ut radiusen
* Gjør en sjekk i `set_radius` slik at radiusen som settes ikke kan være negative. Kast en `invalid_argument` feil hvis dette skjer.

---

```C++
class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double radius, double cx = 0, double cy = 0)
    {
        set_radius(radius);
        _center = {cx, cy};
    }

    double get_radius()
    {
        return _radius;
    }
    void set_radius(double radius)
    {
        if (radius < 0)
        {
            throw std::invalid_argument("Radius cannot negative");
        }
        _radius = radius;
    }
};
```

---

## En `struct` for et punkt (`Point`)

* Lag en `struct` som heter `Point` som tar inn to `double` verdier `x` og `y`
* Lag en funksjon `distance` som tar inn to structs av typen `Position` og returnerer avstanden mellom dem
* Hint:
  * Avstanden mellom $(x_1, y_1)$ og $(x_2, y_2)$ er

    $$d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$$

  * `sqrt` og `pow` can importeres fra `cmath`.

---

```c++
double distance(Point p1, Point p2)
{
    return std::sqrt(std::pow(p1.x - p2.x, 2) + std::pow(p1.y - p2.y, 2));
}
```

---

## Setrum av sirkelen kan være point

- La istedet `Circle` ha en variabel `_center` som er av typen `Point`

---

```C++
#include <cmath>
#include <iostream>
#include <math.h>

struct Point
{
    double x;
    double y;
};

class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double radius, double cx = 0, double cy = 0)
    {
        _radius = radius;
        _center = {cx, cy};
    }
    double area()
    {
        return M_PI * std::pow(_radius, 2);
    }
    void print()
    {
        std::cout << "Circle with radius " << _radius;
        std::cout << " and center (" << _center.x << ", " << _center.y << ")\n";
    }
};

int main()
{

    Circle c{1, 1.0, 2.0};
    std::cout << "Area is " << c.area() << "\n";
    c.print();

    return 0;
}
```

---

## Nå ville det vært fint om vi kunne velge hvordan vi skal lage en sirkel

```C++
// På den original måten
Circle c1{1, 1.0, 2.0};

// eller ved å bruke et Point direkte
Point p{0.0, 1.0};
Circle c2{2, p};
```
* Hvordan kan vi gjøre dette?
* Vi kan implementere en ny konstruktør, så får kompilatoren finne ut hvilken konstrukør som skal brukes.

---

```C++
class Circle
{
    ... public : Circle(double radius, Point center)
    {
        _radius = radius;
        _center = center;
    }
};
```

---

## Funksjon overlasting (*function overloading*)

Det å ha flere funksjoner med samme navn som tar ulike typer argumenter kalles funksjon overlasting (function overloading på engelsk)

* Kompilatoren vil finne ut hvilken *versjon* av funksjonen som skal brukes

---

## Implementere `range` funksjonen

Tenk deg at du ønsker å lage en funksjon som heter `range` som oppfører seg slik som `range` i python.


```python
# range(end)
list(range(6))
# printer [0, 1, 2, 3, 4, 5]
```

```python
# range(start, end)
list(range(1, 6))
# printer [1, 2, 3, 4, 5]
```

```python
# range(start, end, step)
list(range(0, 6, 2))
# printer [0, 2, 4]
```

---

## I C++ kan vi lage flere funksjoner med samme navn, men ulik input

- Implementer `std::vector<int> range(int start, int end, int step)`
- Implementer `std::vector<int> range(int start, int end)`
- Implementer `std::vector<int> range(int end)`

* Kan vi slippe å implementere noen av disse ved å bruke default argumenter?

* Oppgave til dere: Implementer tilsvarende metoder med typen `double`.

    `range.cpp`

---

```c++
#include <iostream>
#include <vector>

std::vector<int> range(int start, int end, int step = 1)
{
    std::vector<int> x;
    for (int i = start; i < end; i += step)
    {
        x.push_back(i);
    }
    return x;
}

std::vector<int> range(int end)
{
    return range(0, end);
}

int main()
{
    auto x = range(5);
    std::cout << "x: ";
    for (auto xi : x)
        std::cout << xi << ", ";

    auto y = range(1, 6, 2);
    std::cout << "\ny: ";
    for (auto yi : y)
        std::cout << yi << ", ";
    std::cout << "\n";

    return 0;
}
```

---

Utfordrende oppgave: Implementer deres egen versjon av `range` i python (kall den for eksempel `myrange`).

---

## Konstrukører i Circle

```C++
class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double radius, double cx = 0, double cy = 0)
    {
        set_radius(radius);
        _center = {cx, cy};
    }
    Circle(double radius, Point center)
    {
        set_radius(radius);
        _center = center;
    }
};
```

---

## Det er anbefalt å bruke medlemsinitialiseringslister der det er mulig


```C++
class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double radius, double cx = 0, double cy = 0) : _radius(radius), _center({cx, cy})
    {
        // Her kan man også sjekke radiusen
        if (_radius < 0)
            throw std::invalid_argument("Radius cannot negative");
    }
    Circle(double radius, Point center) : _center(center)
    {
        // Eller man kan bruke set_radius
        set_radius(radius);
    }
};
```

---

# Det er også vanlig å kun deklarere metodene i klassen

Da er det enkelt for brukeren å kun se hvilke metoder som er tilgjengelig uten å drukne i detaljer.
```c++
class Circle
{
  private:
    double _radius;
    Point _center;

  public:
    Circle(double, double, double);
    Circle(double radius, Point center);
    double get_radius();
    void set_radius(double radius);
    double area();
    void print();
};
```

---

Da kan vi putte implementasjonen en annen plass. Merk at vi her bruker `::` for å si at metoden tilhører `Circle` klassen.

```c++
Circle::Circle(double radius, double cx = 0, double cy = 0) : _radius(radius), _center({cx, cy})
{
    if (_radius < 0)
        throw std::invalid_argument("Radius cannot negative");
}
Circle::Circle(double radius, Point center) : _center(center)
{
    set_radius(radius);
}

double Circle::get_radius()
{
    return _radius;
}
```

---


## Eksempel hvor vi returnere en `struct`

Følgende ligning beskriver hastiget og posisjon til et legeme i fritt fall med masse $m$
$$\frac{{\rm d}v}{{\rm d}t} = -g, \qquad \frac{{\rm d}y}{{\rm d}t}=v.$$

```C++
struct Solution
{
    std::vector<double> t;
    std::vector<double> v;
    std::vector<double> y;
};

// Return er en `struct` med løsningen
Solution falling_body(double v0, double y0, double dt, double T);
```

---


## Lag en funksjon som løser differensialligningen og returnerer en `struct`

Gjenbruk deler av koden fra forrige versjon fra forrige forelensning.

---

```c++
#include <iostream>
#include <vector>

const double G = 9.81;

struct Solution
{
    std::vector<double> t;
    std::vector<double> v;
    std::vector<double> y;
};

Solution falling_body(double v0, double y0, double dt, double T)
{
    Solution sol{{0.0}, {v0}, {y0}};

    double t = 0.0;
    int i = 0;
    while (t < T)
    {
        t = i * dt;
        sol.t.push_back(sol.t[i] + dt);
        sol.v.push_back(sol.v[i] - G * dt);
        sol.y.push_back(sol.y[i] + sol.v[i + 1] * dt);
        i++;
    }
    return sol;
}

int main()
{
    // Initial betingelser
    double y0 = 100.0;
    double v0 = 0.0;

    double T = 4.0;
    double dt = 0.01;

    auto solution = falling_body(v0, y0, dt, T);
    return 0;
}
```

---

## Mål for dagens forelesning

Vite
- hvordan man larger klasser (`class`) og strukturer (`struct`)
- forkjellen på  `class`, `struct`
- forskjellen på `public` og `private` variabler
- hva funksjons overlasting (function overloading) er for noe
- hva medlemsinitialiseringslister er for noe
