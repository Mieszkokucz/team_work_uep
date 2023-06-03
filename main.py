import math

def oblicz_objetosc_stozka(promien, wysokosc):
    if promien < 0 or wysokosc < 0:
        return "Promień i wysokosc nie może być mniejszy od zera!"

    objetosc = round( (1/3) * math.pi * (promien ** 2) * wysokosc, 2)
    return objetosc

# Przykładowe użycie
#promien = 5
#objetosc = oblicz_objetosc_kuli(promien)
#print(f"Objętość kuli o promieniu {promien} wynosi: {objetosc}")


oblicz_objetosc_stozka(3,5)
assert oblicz_objetosc_stozka(3,5) == 47.12
assert oblicz_objetosc_stozka(5,7) == 183.26


def szescian(bok):
    pole_powierzchni=6*bok*bok
    objetosc=bok**3
    return pole_powierzchni, objetosc

assert szescian(1) == (6, 1)
assert szescian(2) == (24, 8)
assert szescian(3) == (54, 27)


