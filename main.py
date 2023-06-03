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

