from statistics import mean

class Student:
    def __init__(self, imie, nazwisko, nr_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_indeksu = nr_indeksu
        self.indeks = []
    def __str__(self):
        return self.imie + " " + self.nazwisko + " " + str(self.nr_indeksu)

    def dodaj_ocene(self, ocena):
        self.indeks.append(ocena)

    def oblicz_srednia(self):
        if len(self.indeks) == 0:
            return 0
        else:
            return mean(self.indeks)

class Samochod:
    def __init__(self, marka, model, rok_prod, moc, poj, kolor, segment, daty_przegladu):
        self.marka = marka
        self.model = model
        self.rok_prod = rok_prod
        self.moc = moc
        self.poj = poj
        self.kolor = kolor
        self.segment = segment
        self.daty_przegladu = daty_przegladu

    def __str__(self):
        return self.marka + " " + self.model + " " + str(self.rok_prod) + " " + str(self.moc) + " " + str(self.poj)\
            + " " + self.kolor + " " + self.segment + " " + str(self.daty_przegladu)
    def ostatnia_data(self):
        return max(self.daty_przegladu)


autko = Samochod("BMW", "5 Series", 2023, 340, 3.0, "White", "Limousine", ['01-01-2022', '01-01-2023'])
print(autko)
print(autko.ostatnia_data())

#student_marcin = Student("Marcin", "Kostka", 120060)
#student_marcin.dodaj_ocene(5.0)
#student_marcin.dodaj_ocene(4.5)
#student_marcin.dodaj_ocene(4.0)
#student_marcin.dodaj_ocene(3.0)
#print(student_marcin.indeks)
#print(student_marcin.oblicz_srednia())
