class Pracownik:
    def __init__(self, nazwisko, wyplata_brutto):
        self.nazwisko = nazwisko
        self.wyplata_brutto = wyplata_brutto

    def __str__(self):
        return f"{self.nazwisko } {self.wyplata_brutto}"
    
    def oblicz_netto(self):
        skladki_pracownik = 0.0976*self.wyplata_brutto + 0.015*self.wyplata_brutto + 0.0245*self.wyplata_brutto
        skladka_zdrowotna = 0.09*(self.wyplata_brutto - skladki_pracownik)
        zaliczka_podatek = 0.12*(int(self.wyplata_brutto - skladki_pracownik-250)) - 300
        wyplata_netto = round(self.wyplata_brutto - skladki_pracownik - skladka_zdrowotna - zaliczka_podatek, 2)
        return wyplata_netto
    
    def oblicz_koszty_pracodawcy(self):
        skladki_pracodawca = 0.0976*self.wyplata_brutto + 0.065*self.wyplata_brutto + 0.0167*self.wyplata_brutto + 0.0245*self.wyplata_brutto + 0.001*self.wyplata_brutto
        koszt_pracowdawcy = round(self.wyplata_brutto + skladki_pracodawca, 2)
        return koszt_pracowdawcy

    def wygeneruj_raport(self):
        skladka_emeryt = 0.0976 * self.wyplata_brutto
        skladka_rentowa = 0.015 * self.wyplata_brutto
        skladka_chorobowa = 0.0245 * self.wyplata_brutto
        skladka_zdrowotna = 0.09 * (self.wyplata_brutto - skladka_emeryt - skladka_rentowa - skladka_chorobowa)
        skladka_rentowa_pracodawca = 0.065 ** self.wyplata_brutto
        skladka_ubezp_pracodawca = 0.0167 * self.wyplata_brutto
        skladka_funduszpracy = 0.0245 * self.wyplata_brutto
        skladka_funduszgsp = 0.001 * self.wyplata_brutto
        print("Wynagrodzenie brutto:", self.wyplata_brutto,
              "\n\nSkładki płatne przez pracownika:\nSkładka emerytalna:", skladka_emeryt,
              "\nSkładka rentowa:", skladka_rentowa,
              "\nSkładka chorobowa:", skladka_chorobowa,
              "\nSkładka zdrowotna:", skladka_zdrowotna,
              "\n\nSkładki płatne przez pracodawcę:\nSkładka emerytalna:", skladka_emeryt,
              "\nSkładka rentowa:", skladka_rentowa_pracodawca,
              "\nSkładka na ubezpieczenie wypadkowe:", skladka_ubezp_pracodawca,
              "\nSkładka na Fundusz Pracy:", skladka_funduszpracy,
              "\nSkładka na Fundusz Gwarantowanych Świadczeń Pracowniczych:", skladka_funduszgsp
              )



Pracownik1 = Pracownik("Popiol", 3500)
#Test funkcji oblicz_netto()
assert Pracownik1.oblicz_netto() == 2715.94, "Niepoprawna wypata"
#Test funkcji __str__()
assert str(Pracownik1) == "Popiol 3500", "Nieoczekiwany string"


#Test funkcji oblicz_koszty_pracodawcy()
assert Pracownik1.oblicz_koszty_pracodawcy() == 4216.8

#Test funkcji wygeneruj_raport()
Pracownik1.wygeneruj_raport()
#Błędnie zdefiniowana zmienna skladka_rentowa_pracodawca, zmiana na -> skladka_rentowa_pracodawca = 0.065 * self.wyplata_brutto

