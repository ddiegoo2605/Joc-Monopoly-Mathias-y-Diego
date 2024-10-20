def crear_fila_horizontal(casillas, inicio, fin):
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")
     for j  in range(inicio, fin + 1):
          espacios = " " * (8-len(casillas[j])) 
          casilla = casillas[j] + espacios
          print(f"|{casilla}|", end = " ")
     print() 
     for i in range(7):
          print("|"+" "* 8+"|", end = " ")#Aqui van los jugadores
     print()
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")
     
def crear_laterales(casillas):
     contador1 = 12
     contador2 = 20
     for i in range(5):
      print("+--------+" + " "* 56 + "+--------+")
      espacios = " " * (8-len(casillas[contador1])) 
      casillas_izq = casillas[contador1] + espacios
      espacios = " " * (8-len(casillas[contador2])) 
      casillas_der = casillas[contador2] + espacios
      print(f"|{casillas_izq}|"+ " "* 56 + f"|{casillas_der}|")
      print(f"|"+" "* 8+"|"+ " "* 56 + "|"+" "* 8+"|")#Iran los jugadores
      print("+--------+" + " "* 56 + "+--------+")
      contador1 = contador1 - 1
      contador2 = contador2 + 1

def crear_fila_horizontal2(casillas, inicio, fin):
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")
     for j  in range(inicio, fin -1, -1):
          espacios = " " * (8-len(casillas[j])) 
          casilla = casillas[j] + espacios
          print(f"|{casilla}|", end = " ") 
     print(" ")
     for i in range(7):
          print("|"+" "* 8+"|", end = " ")#Aqui van los jugadores
     print()
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")

def tablero_monopoly(casillas):
     crear_fila_horizontal(casillas, 13 , 19)
     crear_laterales(casillas)
     crear_fila_horizontal2(casillas, 6, 0)

casillas = ["Sortida", "Lauria", "Rosell", "Sort", "Marina", "Marina","Consell", "Presó",
            "Muntan", "Aribau", "Caixa", "S.Joan", "Aragó", "Parking", "Urquinoa", "Fontan",
            "Sort", "Rambles", "Pl.Cat","Anr pró", " Angel", "Augusta", "Caixa", "Balmes", "Gracia"]

tablero_monopoly(casillas)

