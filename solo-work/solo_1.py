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