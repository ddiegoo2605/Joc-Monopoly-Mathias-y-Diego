import random

jugador1 = "Vermell"
jugador2 = "Groc"
jugador3 = "Taronja"
jugador4 = "Blau"


def orden_tirada():
    tirada_jugador1 = random.randint(0,4)
    tirada_jugador2 = random.randint(0,4)
    tirada_jugador3 = random.randint(0,4)
    tirada_jugador4 = random.randint(0,4)

    if tirada_jugador2 > tirada_jugador1:
        tmp = tirada_jugador1
        tirada_jugador1 = tirada_jugador2
        tmp = tirada_jugador2
        
    if tirada_jugador3 > tirada_jugador4:
        tmp = tirada_jugador4
        tirada_jugador3 = tirada_jugador4
        tmp = tirada_jugador3
        
    if tirada_jugador2 > tirada_jugador1:
        tmp = tirada_jugador1
        tirada_jugador1 = tirada_jugador2
        tmp = tirada_jugador2