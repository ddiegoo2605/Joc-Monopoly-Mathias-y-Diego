def crear_fila_horizontal(casillas, inicio, fin):
     for i in range(0, 7):
          print("+--------+", end= " ")
     print(" ")
     for i  in range(2):
          for j  in range(0, 7):
               print("|" + " " * 8 + "|", end = " ")
          print(" ")
     for i in range(0, 7):
          print("+--------+", end= " ")
     print(" ")
     
def crear_laterales(casillas):
     for i in range(7):
      print("+--------+" + " "* 56 + "+--------+")
      casillas_izq = casillas[i] if len(casillas) > i else " " * 8
      casillas_der = casillas[-(i + 1)] if len(casillas) > (-(i +1)) else " " * 8
      print("|" + " " * 8 + "|"+ " "* 56 + "|" + " " * 8 + "|")
      print("|" + " " * 8 + "|"+ " "* 56 + "|" + " " * 8 + "|")
      print("+--------+" + " "* 56 + "+--------+")

def tablero_monopoly(casillas):
     crear_fila_horizontal(casillas, 0 , 7)
     crear_laterales(casillas)
     crear_fila_horizontal(casillas, 7, 14)

casillas = [ "Sortida", "Lauria", "Rosell", "Sort", "Marina", "Marina","Consell", "Presó",
            "Muntan", "Aribau", "Caixa", "S.Joan", "Aragó", "Parking", "Urquinoa", "Fontan",
            "Sort", "Rambles", "Pl.Cat","Anr pró", " Angel", "Augusta", "Caixa", "Balmes", "Gracia"]

tablero_monopoly(casillas)

