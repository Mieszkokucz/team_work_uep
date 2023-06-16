import csv
import generator
from salary import Pracownik

#wczytanie danych z csv i wrzucenie ich do klasy pracownik


with open('data/pracownicy.csv', mode='r', newline='') as file:
    csvreader = csv.reader(file)

    #pomin header
    next(csvreader)

    for row in csvreader:
        # print(row)
        imie, nazwisko, pensja = row
        Pracownik1 = Pracownik(nazwisko, int(pensja))
        Pracownik1.oblicz_netto()
        Pracownik1.oblicz_koszty_pracodawcy()
        Pracownik1.wygeneruj_raport()

