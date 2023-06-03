import math

def oblicz_objetosc_kuli(promien):
    if promien < 0:
        return "Promień nie może być mniejszy od zera!"

    objetosc = round((4/3) * math.pi * (promien ** 3),2)
    return objetosc

# Przykładowe użycie
#promien = 5
#objetosc = oblicz_objetosc_kuli(promien)
#print(f"Objętość kuli o promieniu {promien} wynosi: {objetosc}")


assert oblicz_objetosc_kuli(3) == 113.1
assert oblicz_objetosc_kuli(5) == 523.6


def szescian(bok):
    pole_powierzchni=6*bok*bok
    objetosc=bok**3
    return pole_powierzchni, objetosc

assert szescian(1) == (6, 1)
assert szescian(2) == (24, 8)
assert szescian(3) == (54, 27)


