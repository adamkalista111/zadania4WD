import sys as system
import random

#Zad. 1
#Wygeneruj liczby z przedziału <0,30>, następnie pomnóż je przez 2 i zapisz do pliku

print("Zadanie 1:\n")

lista = []
for i in range(10):
    lista.append(random.randrange(0,30))

plik = open("Zad1_2.txt", "w")
for i in lista:
    plik.write(str(i*2) + " ")
plik.close()
#Zad. 2
#Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
print("Zadanie 2:\n")
plik = open("Zad1_2.txt", "r")
print(plik.readlines())
#Zad. 3
#Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

print("Zadanie 3:\n")
with open("Zad3.txt", "r+") as plik:
    for i in range(3):
        plik.write("Kilka linijek tekstu\n")
    for i in plik:
        print(i)

#Zad.4

class NaZakupy:
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    def wyswietl_produkt(self):
        print(self.nazwa_produktu, self.ilosc, self.jednostka_miary, self.cena_jed)
    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)
    def ile_kosztuje(self):
        print(self.ilosc * self.cena_jed)
zakupy = NaZakupy("ziemiank", 5, "kg", 2.49)
zakupy.wyswietl_produkt()
zakupy.ile_produktu()
zakupy.ile_kosztuje()
#Zad.5



#Zad.6
