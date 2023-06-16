from io import StringIO
class Pracownik:
    def __init__(self, nazwisko, wyplata_brutto):
        self.nazwisko = nazwisko
        self.wyplata_brutto = wyplata_brutto

    def __str__(self):
        return f"{self.nazwisko } {self.wyplata_brutto}"

    def oblicz_netto(self):
        self.skladka_emeryt = round(0.0976 * self.wyplata_brutto, 2)
        self.skladka_rentowa = round(0.015 * self.wyplata_brutto, 2)
        self.skladka_chorobowa = round(0.0245 * self.wyplata_brutto, 2)
        self.skladka_zdrowotna = round(0.09 * (self.wyplata_brutto - self.skladka_emeryt - self.skladka_rentowa - self.skladka_chorobowa), 2)
        self.zaliczka_podatek_dochodowy = round(0.12 * round((self.wyplata_brutto - self.skladka_emeryt - self.skladka_rentowa - self.skladka_chorobowa - 250)) - 300, 2)
        self.wyplata_netto = self.wyplata_brutto - self.skladka_emeryt - self.skladka_rentowa - self.skladka_chorobowa - self.skladka_zdrowotna - self.zaliczka_podatek_dochodowy

        return self.wyplata_netto

    def oblicz_koszty_pracodawcy(self):
        self.skladki_pracodawca = 0.0976*self.wyplata_brutto + 0.065*self.wyplata_brutto + 0.0167*self.wyplata_brutto + 0.0245*self.wyplata_brutto + 0.001*self.wyplata_brutto
        self.koszt_pracowdawcy = round(self.wyplata_brutto + self.skladki_pracodawca, 2)
        return self.koszt_pracowdawcy

    def wygeneruj_raport(self):
        print(f"Wynagrodzenie brutto: {self.wyplata_brutto}" +\
        f"\n\nSkładki płatne przez pracownika:\nSkładka emerytalna: {self.skladka_emeryt}" +\
              f"\nSkładka rentowa: {self.skladka_rentowa}" +\
              f"\nSkładka chorobowa: {self.skladka_chorobowa}" +\
              f"\nSkładka zdrowotna: {self.skladka_zdrowotna}" +\
              f"\nZaliczka na podatek dochodowy: {self.zaliczka_podatek_dochodowy}" +\
              f"\nWynagrodzenie netto: {self.wyplata_netto}"
              )



Pracownik1 = Pracownik("Popiol", 3500)
#Test funkcji oblicz_netto()
assert Pracownik1.oblicz_netto() == 2715.94, "Niepoprawna wypata"
#Test funkcji __str__()
assert str(Pracownik1) == "Popiol 3500", "Nieoczekiwany string"


#Test funkcji oblicz_koszty_pracodawcy()
assert Pracownik1.oblicz_koszty_pracodawcy() == 4216.8

Pracownik1.wygeneruj_raport()

#Test funkcji wygeneruj_raport()
#te przechwytywanie z neta skopiowialem
captured_output = StringIO()
sys.stdout = captured_output

# Call the method
Pracownik1.wygeneruj_raport()

# Capture the printed output
printed_text = captured_output.getvalue().strip()

expected_output = f"Wynagrodzenie brutto: 3500" +\
        f"\n\nSkładki płatne przez pracownika:\nSkładka emerytalna: 341.6" +\
              f"\nSkładka rentowa: 52.5" +\
              f"\nSkładka chorobowa: 85.75" +\
              f"\nSkładka zdrowotna: 271.81" +\
              f"\nZaliczka na podatek dochodowy: 32.4" +\
              f"\nWynagrodzenie netto: 2715.94"

assert printed_text == expected_output, f"Expected '{expected_output}', but got '{printed_text}'"

sys.stdout = sys.__stdout__