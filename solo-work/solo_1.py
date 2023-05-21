# zadanie 1.1

hello = "Hello"
student = "Ola"

print("{} {}".format(hello, student))

# zadanie 1.2

student = input("Wpisz swoje imie")

print("{} {}".format(hello, student))

# zadanie 1.3

studenci = ["Ania", "Kuba", "Piotr", "Marcin"]
liczba_studentow = len(studenci)

print("{} {}".format("Liczba studentow wynosi: ", liczba_studentow))

# zadanie 1.4

studenci = ["Ania", "Kasia", "Piotr", "Tomek"]

for s in studenci:
    print(hello, s)

# zadanie 1.5

liczba = 3

potega = 4

wynik = liczba**potega

print("Wynik wynosi: ", wynik)

# zadanie 1.6

ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = 0

for znak in ciag_znakow:
    if znak == '(':
        liczba_nawiasow_otwierajacych += 1

print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

# zadanie 1.7

# posortuj alfabetycznie (od imienia) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()

print("Alfabetyczna lista studentow wynosi: ")
for student in studenci:
    print(student)

# zadanie 1.8

# posortuj alfabetycznie (od nazwiska) studentow
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
sorted_studenci = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentow wynosi: ")
for student in sorted_studenci:
    print(student)

# zadanie 1.9

# policz wszystkich studentow z tablicy, ktorych nazwisko zaczyna sie na N
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1].startswith("N"):
        liczba_n += 1
print("Liczba studentow na N wynosi: ", liczba_n)

# zadanie 1.10

def czy_funkcja_liniowa(punkty):
    x = [punkt[0] for punkt in punkty]
    y = [punkt[1] for punkt in punkty]

    if len(set(x)) == 1:
        return True

    for i in range(len(x) - 2):
        if (y[i + 1] - y[i]) / (x[i + 1] - x[i]) != (y[i + 2] - y[i + 1]) / (x[i + 2] - x[i + 1]):
            return False

    return True
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]

wykres_1_funkcja_liniowa = czy_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
