#Imports

import random
import pandas as pd

#Bucle del juego

def Tirar_dados():
    #Valores del dado entre 1 y 6 (Tirar dado)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    #Total
    total = dado1 + dado2
 
    return total

casillas = pd.read_csv('Casillas.csv')
print(casillas)
