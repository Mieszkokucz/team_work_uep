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


Pracownik1 = Pracownik("Popiol", 3500)
#Test funkcji oblicz_netto()
#assert Pracownik1.oblicz_netto() == 2715.94, "Niepoprawna wypata"
#Test funkcji __str__()
#assert str(Pracownik1) == "Popiol 3500", "Nieoczekiwany string"

#poppozycja poprawki funkcji str:
# return f"{self.nazwisko } {self.wyplata_brutto}"