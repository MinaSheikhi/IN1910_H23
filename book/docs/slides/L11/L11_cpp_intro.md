---
theme: default
paginate: true
header: "Lecture 11 - Introduksjon til C++"
footer: "Henrik Finsberg - 28.09.22"
marp: true
---

# Lecture 11 - Introduksjon til C++

Henrik Finsberg - 28.09.22

---

## Mål for dagens forelesning

- Bli kjent med basic C++ syntaks
  - Funksjoner
  - Typer (`int`, `double`)
  - Løkker (`for`, `while`)
  - Betingelser (`if`, `else`)
  - Navnerom (namespace)
- Vite hvordan man skriver, kompilerer og kjører ett C++ program
- Kjenne til C++ `vector`.
- Vite hvordan man printer til terminalen og skriver til en fil.
- Vite hovedforskjellene mellom python og C++

---

## Før vi kan bruke C++ må dere installere en C++ kompilator

https://pages.github.uio.no/IN1910/IN1910_H22/docs/setup/cpp_compiler.html

---

## Undervisningsmateriale i C++

- Forelesningsnotater: https://pages.github.uio.no/IN1910/IN1910_H22/docs/lectures/cpp/cpp.html
- Gratis tilgjengelig lærebok: https://pages.github.uio.no/IN1910/IN1910_H22/docs/info/curriculum.html#c

---

## Hvorfor C++?

- Det er nyttig å lære flere programmeringsspråk for å se ulike måter å løse samme problem på

- C++ er et lavnivå språk. Kortere vei fra kode til maskininstruksjoner

- Vi kan bruke C++ til å lære mer om hva som skjer i et program

  - Hva skjer når vi deklarerer en variabel?
  - Hvordan håndteres minne?

- C++ har høyere ytelse enn python

---

## Kort historie

- C++ ble utviklet av Bjarne Stroustrup i 1979

- Formålet med dette var å lage en objektorientert utgave av C (inspirert av Simula)

- `++` er en måte å inkrementere på, så C++ er på en måte utviklet versjon av C

- C++ har (i likehet med python) et stort standardbibliotek

- C++ kommer med ny standard hvert tredje år. Den nyeste er C++20 (neste er C++23)

- I dette kurset bruker vi C++14 standaren. Grunnen til dette er at vi ønsker kun å gi en kort innføring, og vil dermed ikke støte på noen konsepter som krever nyere standard.

---

## Mitt første C++ program

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## C++ filer ender med .cpp

- Denne filen heter for eksempel `hello.cpp`

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Istedet for `import` bruker vi `#include`

- `#include <iostream>` vil for eksempel inkludere et bibliotek som inneholder funksjoner for å printe til konsollen

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Alle C++ program må han en funksjon som heter `main`

- Hvis vi ikke har denne funksjonen vil vi få en feilmelding
- `main` funksjonen er funksjonen som blir kjørt
- Dette er likt i python med `if __name__ == "__main__"`, men det er ikke like strengt

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Alle funksjoner må spesifisere hva slags type de returnerer

- For eksempel denne `main` funksjonen returnerer en `int`.
- Typen som returneres kommer før navnet på funksjonen
- Grunne til at `main` returner en `int` er at det er vanlig å bruke _exit codes_, hvor code `0` betyr at programmet var velykket.
- Vi bruker `return` akkurat som i python

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## `main` tar ingen argumenter

- Hadde `main` tatt argumenter hadde de gått inn parantesen `()`.

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Vi bruker krølleparenteser `{}` istedenfor innrykk

- All innenfor krølleparentesene hører til funksjonen
- Innrykk (indentation) har ingenting å si

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Alle linjer ender med `;`

- Med noen få unntak slik som av slutten av krølleparenteser til funksjoner, og linjer med `#include`

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Vi kan printe ved å bruke `std::cout`

- `std` betyr bare at funksjonen `cout` hører til standardbibliotektet
- `::` er akkurat som `.` bruker i python. For eksempel `math.sin`, eller `np.linspace`.

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Hvis vi skriver `using namespace std` så slipper vi å skrive `std::`

- Dette blir på samme måte som å skrive `from std import *` i python
- Det er generelt en dårlig ide fordi du lett kan få navnekollisjoner

```c++
// hello.cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello world!\n";
    return 0;
}
```

---

## `<<` sender strengene i pilens retning

- Alt sendes til slutt til `cout` (console output)
- `<<` kan sammenkobles
- `\n` betyr ny linje (går også an å bruke `std::endl` fra `iostream`).

```c++
// hello.cpp
#include <iostream>

int main()
{
    // Alle disse printer det samme
    std::cout << "Hello world!\n";
    std::cout << "Hello "
              << "world!\n";
    std::cout << "Hello"
              << " "
              << "world!\n";
    return 0;
}
```

---

## Vi lager kommentarer med `//`

- Eventuelt kan vi bruke `/* */` dersom vi ønsker at kommentaren skal gå over flere linjer.

```c++
// hello.cpp
#include <iostream>

int main()
{
    /* Dette er
    en kommentar
    over flere
    linjer */

    // Dette er en kommentar på en linje
    std::cout << "Hello world!\n";
    return 0;
}
```

---

## Sammenligne med python

```c++
// hello.cpp
#include <iostream>

int main()
{
    std::cout << "Hello world!\n";
    return 0;
}
```

```python
# hello.py
if __name__ == "__main__":
    print("Hello world")
```

---

## For å kjøre et C++ program må det først kompileres

```
$ c++ hello.cpp
```

Dette produsere en ny kjørbar fil som heter `a.out` (kan være forskjellig på ulike operativsystem).

Man kan nå kjøre denne filen

```
$ ./a.out
Hello world!
```

---

## Man kan også spesifisere et navn på outputfilen

```
$ c++ hello.cpp -o hello
```

Dette produsere en fil heter `hello`. Man kan nå kjøre denne filen

```
$ ./hello
Hello world!
```

---

## Vi må også spesifisere hvilken C++ standard vi skal bruke

I dette kurset bruker vi C++14 standaren.

```
$ c++ hello.cpp -std=c++14
$ c++ hello.cpp -o hello -std=c++14
```

---

## Kjørbar fil med maskinstruksjoner

Denne nye filen inneholder maskininstruksjoner som er spesialisert for den maskinen det er kompilert på. Det betyr at dersom du kompilerer et program og gir den kompilerte fila videre så vil den kun fungere om dere har lik operativ system og lik arkitektur på maskinen.

---

## C++ bruker statisk typesjekking

- Statically typed
- C++ må vite hva slags typer alt er.
- Dette er fordi ulike typer krever ulik plass i minne

```c++
string city = "Oslo"; // må også bruke #include <string>
char a = 'a';         // Merk ' for char mens " for strenger
int year = 2018;
double temp = 42.3;
```

---

| C++ Type        | Description           | Size in memory |
| --------------- | --------------------- | -------------- |
| `bool`          | Boolean               | 1 byte         |
| `short`         | 16-bit integer        | 2 bytes        |
| `int`           | 32-bit integer        | 4 bytes        |
| `long long int` | 64-bit integer        | 8 bytes        |
| `float`         | 32-bit floating-point | 4 bytes        |
| `double`        | 64-bit floating-point | 8 bytes        |
| `char`          | single character      | 1 byte         |
| `string`        | character sequence    | 1 byte         |

---

## Bytes og bits

* 1 byte = 8 bits (1 bit er `0` eller `1`)
* Hva er dette binære tallet i titallsystemet for eksempel?
  ```
  101010
  ```
* Svar:
    $$ (101010)_2 = (1 \cdot 2^5 + 0 \cdot 2^4 + 1 \cdot 2^3 + 0 \cdot 2^2 + 1 \cdot 2^1 + 0 \cdot 2^0)_{10}$$
    $$ (101010)_2 = (32+8+2)_{10} = (42)_{10}$$

---

# Hvor mange tall kan vi representere med 8 bits?

* Med 1 byte kan vi representere 256 ($2^8$ tall). For eksempel 255 = $2^8 -1 = (2^7 + 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1 + 2^0)_{10} = (11111111)_2$


---

## Hva betyr det at `int` er 4 bytes?

- Med 4 byte kan vi representere $(2^8)^4 = 2^{32}$ tall

- Men hvis vi skal ha negative tall må vi nøye oss med halvparten.

- Derfor kan `int` holde tall mellom $[-2^{31}, 2^{31} - 1]$ (hvor $0$ også er inkludert)

---

## I Python er alt av typen `object` og tar mye større plass

For eksempel hos meg tar tallet `1` 28 bytes

```python
import sys
print(sys.getsizeof(1))
# prints 28
```

Det er noe av grunnen til hvorfor C++ har bedre ytelse.

---

## I C++ er det anbefalt å intialisere variabler ved å bruke `{}` i stedet for `=`

```c++
string city = "Oslo";
char a = 'a';
int year = 2018;
double temp = 42.3;
```

- Men det er helt OK dere bruker `=` (så lenge dere er klar over forskjellen)

```c++
string city{"Oslo"};
char a{'a'};
int year{2018};
double temp{42.3};
```

---

## Grunnen til at `{}` er anbefalt er fordi det gjøres noen ekstra sjekker

Følgende er lovlig

```c++
int pi = 3.14; // Her blir pi konvertert til 3
```

Følgende er ikke lovlig

```c++
int pi{3.14}; // Det gir en feilmelding
```

---

## Eksempel - funksjon som konverterer fra Fahrenheit til Celsius

Lag en funksjon `F2C` med signaturen

```c++
double F2C(double F);
```

som konverterer fra Fahrenheit til Celsius ved å bruke formelen

$$ C = 5*(F-32)/9$$

Test programmet ditt med $F = 100$.
Test programmet i https://godbolt.org

---

```c++
#include <iostream>

double F2C(double F)
{
    return 5 * (F - 32) / 9;
}

int main()
{
    double temp = 100.0;
    std::cout << temp << " F" << endl;
    std::cout << F2C(temp) << " C" << endl;
    return 0;
}
```

---

## Hvis du ikke ønsker å returnere noe kan du bruke `void`

`void` er en spesiell type uten verdier og bruker for funksjoner som ikke returnerer noe
Lag en funksjon `greet` med signaturen

```c++
void greet(std::string name);
```
some printer "Hello" etterfuglt av navnet some sendes inn.
Lag en program som spør om navnet diff og som tar input fra consollen og lager det i en `string` variabel.

_Hint_: For å ta input fra consollonen må man bruke `cin` (console input) fra `iostream` (og her skal pilene gå fra `cin` til den variablen som du vil skrive til).

---

```c++
#include <iostream>
#include <string>

void greet(std::string name)
{
    std::cout << "Hello there " << name << "!\n";
}

int main()
{
    std::string name;
    std::cout << "What is you name? ";
    std::cin >> name;
    greet(name);
    return 0;
}
```

---

## `for` løkker

```c++
#include <iostream>

int main()
{
    for (int i = 0; i < 10; i++)
    {
        std::cout << i << " ";
    }
    std::cout << "\n";
    return 0;
}
```

---

## `if`, `else if` og `else`

```c++
if (condition1)
{
    // Do something
}
else if (condition2)
{
    // Do something else
}
else
{
    // Do something else
}
```
---

# Fizz buzz:

For alle tallene fra 1 til 20 print
- `Fizz` hvis tallet er delelig med 3
- `Buzz` hvis det er delelig med 5
- `FizzBuzz` hvis det er delelig med både 5 og 3
- Ellers print tallet

---

```c++
#include <iostream>

int main()
{
    for (int i = 1; i < 20; i++)
    {
        if (((i % 3) == 0) && ((i % 5) == 0))
        {
            std::cout << "FizzBuzz\n";
        }
        else if ((i % 3) == 0)
        {
            std::cout << "Fizz\n";
        }
        else if ((i % 5) == 0)
        {
            std::cout << "Buzz\n";
        }
        else
        {
            std::cout << i << "\n";
        }
    }
    return 0;
}
```

---

## Boolske verdier

En verdi som er enten `true` eller `false` kalles for en bools verdi. Med andre ord typen `bool` har to verdier.

Vi kan bruke `!` til å negere en boolsk verdi (hva bruker vi i python?)

```c++
bool x = true;
if (x)
{
    std::cout << "x is true\n";
}
if (!x)
{
    std::cout << "x is false\n";
}
```
* Hva skjer om `x` er en `int`. Med verdi `0` eller `42`?


---

## Hva om vi ønsker at output skal skrives til en fil?

- Bytte ut `iostream` med `fstream`
- Åpner en fil, og bruker filinstansen på samme måte some `cout`.

```c++
#include <fstream>

int main()
{
    std::ofstream ofs{"output.txt"};
    for (int i = 0; i < 10; i++)
    {
        ofs << i << "\n";
    }

    return 0;
}
```

---

## Det er lurt å sjekke at åpning av filen gikk bra

```c++
#include <fstream>

int main()
{
    std::ofstream ofs{"fake_folder/output.txt"};
    if (!ofs)
    {
        throw std::runtime_error("Unable to open file");
    }
    for (int i = 0; i < 10; i++)
    {
        ofs << i << "\n";
    }

    return 0;
}
```

---

## Primtallssjekker

Lag en funksjon `is_prime` med signaturen

```c++
bool is_prime(int n);
```

som tar enn et heltall og returnerer `true` hvis tallet er et primtall og `false` hvis tallet ikke er et primtall.

---

```c++
bool is_prime(int n)
{
    if (n == 1)
    {
        return false;
    }

    for (int d = 2; d < n; d++)
    {
        if (n % d == 0)
        {
            return false;
        }
    }
    return true;
}
```

---

## Kjøre primtallsjekkeren

```c++
int main()
{
    bool quit = false;
    int x;
    while (!(quit))
    {
        std::cout << "Enter a number (0 to quit): ";
        std::cin >> x;
        if (x == 0)
        {
            quit = true;
            std::cout << "Goodbye\n";
            return 0;
        }
        bool p = is_prime(x);
        if (p)
        {
            std::cout << x << " is a prime\n";
        }
        else
        {
            std::cout << x << " is not a prime\n";
        }
    }
    return 0;
}
```

---

## Går også an å bruke `auto` hvis du ønsker at kompilatoren skal finne ut hvilken type en variabel er

```c++
auto p = is_prime(x);
```

- Nyttig hvis det er kompliserte typer eller at du ikke bryr deg om hvilken type det er
- Men det gjør ofte koden mindre lesbar

---

## Vector er som lister i python

- En an de meste brukte datastrukturene i C++ er `vector`
- Vi kommer til å bruke mye tid på å forstå hvordan `vector` egentlig fungerer
- `vector` tilsvarer `list` i python

---

## Når vi lager en vector må vi si hvilken type den skal inneholde

```c++
#include <vector>

int main()
{
    std::vector<int> primes;
    return 0;
}
```

---

## Vi kan legge til elementer ved å bruke `push_back`

```c++
#include <vector>

int main()
{
    std::vector<int> primes;
    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);

    return 0;
}
```

---

## Eller vi kan initialisere en vektor

```c++
#include <vector>

int main()
{
    std::vector<int> primes{2, 3, 5};

    return 0;
}
```

---

## For å loope over en vektor kan vi enten lage en standard `for` loop

- Da kan vi bruke `.size()` metoden til å finne lengden av vektoren

```c++
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> primes{2, 3, 5};
    for (int i = 0; i < primes.size(); i++)
    {
        std::cout << primes[i] << " ";
    }
    std::cout << "\n";

    return 0;
}
```

---

## Men her finnes det er bedre måte

- Dette blir som å skrive `for p in primes` i python

```c++
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> primes{2, 3, 5};
    for (int p : primes)
    {
        std::cout << p << " ";
    }
    std::cout << "\n";

    return 0;
}
```

---

## Dette er også et godt eksempel der `auto` er nyttig

- Da funker det også hvis vektoren vår er av en annen type

```c++
#include <iostream>
#include <vector>

int main()
{
    std::vector<int> primes{2, 3, 5};
    for (auto p : std::primes)
    {
        std::cout << p << " ";
    }
    std::cout << "\n";

    return 0;
}
```

---

## Hva skjer når vi kjører python?

- python er et program som er skrevet i `C` (det finnes også andre implementasjoner)
- python oversetter kildekoden til noe som heter bytecode. Filene som ligger i `__pycache__` mappen som ender med `.pyc` er bytecode.
- Prøv å velg `python` når du bruker https://godbolt.org så kan du se bytekoden

---

## Din egen python versjon i c++

- Vi kan prøve å lage vårt eget python program
- Dette er en ganske dårlig versjon, men det illustrerer hva som skjer

```c++
#include <iostream>

int main()
{
    // Heltall
    int x;
    while (true)
    {
        std::cout << ">>> ";
        std::cin >> x; // Les det som brukeren gir inn i x
        std::cout << "You wrote " << x << "\n";
    }
    return 0;
}
```

---

## Mål for dagens forelesning

- Bli kjent med basic C++ syntaks
  - Funksjoner
  - Typer (`int`, `double`)
  - Løkker (`for`, `while`)
  - Betingelser (`if`, `else`)
  - Navnerom (namespace)
- Vite hvordan man skriver, kompilerer og kjører ett C++ program
- Kjenne til C++ `vector`.
- Vite hvordan man printer til terminalen og skriver til en fil.
- Vite hovedforskjellene mellom python og C++
