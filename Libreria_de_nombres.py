def crear_fila_horizontal():
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")
     for i  in range(2):
          for i  in range(7):
               print("|" + " " * 8 + "|", end = " ")
          print(" ")
     for i in range(7):
          print("+--------+", end= " ")
     print(" ")
     
def crear_laterales():
     for i in range(7):
      print("+--------+" + " "* 56 + "+--------+")
      print("|" + " " * 8 + "|"+ " "* 56 + "|" + " " * 8 + "|")
      print("|" + " " * 8 + "|"+ " "* 56 + "|" + " " * 8 + "|")
      print("+--------+" + " "* 56 + "+--------+")

def tablero_monopoly():
     crear_fila_horizontal()
     crear_laterales()
     crear_fila_horizontal()

tablero_monopoly()


casillas = [ "Sortida", "Lauria", 
     
]