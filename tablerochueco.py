def crear_fila_horizontal():
     for i in range(7):
          print("+---------------+", end= " ")
     print(" ")
     for i  in range(2):
          for i  in range(7):
               print("|" + " " * 15 + "|", end = " ")
          print(" ")
     for i in range(7):
          print("+---------------+", end= " ")
     print(" ")
     
def crear_laterales():
     for i in range(7):
      print("+---------------+" + " "* 91 + "+---------------+")
      print("|" + " " * 15 + "|"+ " "* 91 + "|" + " " * 15 + "|")
      print("|" + " " * 15 + "|"+ " "* 91 + "|" + " " * 15 + "|")
      print("+---------------+"+ " "* 91 + "+---------------+")



          
def tablero_monopolyprueba():
     crear_fila_horizontal()
     crear_laterales()
     crear_fila_horizontal()

tablero_monopolyprueba()