#Imports
from random import randomint

#Variables

dado1 = -1
dado2 = -1
total = 0

#Bucle del juego

while juego:
    #Valores del dado entre 1 y 6 (Tirar dado)
    dado1 = randomint(1, 6)
    dado2 = randomint(1, 6)

    #Total
    total = dado1 + dado2 
    #Mostrar el total
    print(f"Dados: {total}, El primer dado fue {dado1} y el segundo fue {dado2}")
