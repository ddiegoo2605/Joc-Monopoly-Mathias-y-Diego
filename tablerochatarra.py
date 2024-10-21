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
opcion = (input("Juga V, opcions: passar, comprar casa, comprar hotel, preus"))

import random
listacasillas=["Sortida", "Lauria", "Rosell", "Sort", "Marina", "Marina","Consell", "Presó",
            "Muntan", "Aribau", "Caixa", "S.Joan", "Aragó", "Parking", "Urquinoa", "Fontan",
            "Sort", "Rambles", "Pl.Cat","Anr pró", " Angel", "Augusta", "Caixa", "Balmes", "Gracia"]
listaduenos=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_casas=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_hoteles=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_preciocasa=["200","225","250","275","300","325","350","375","400","425","450","475","500","525","550","525"]
lista_preciohotel=["250","255","260","265","270","275","280","285","290","300","310","320","330","340","350","360"]
lista_multacasa=["10","10","15","15","20","20","25","25","30","30","35","35","40","40","50","50",]
lista_multahotel=["15","15","15","20","20","20","25","25","25","30","30","35","35","40","40","50","50",]
lista_terrenos=["50","50","50","50","60","60","60","60","70","70","70","70","80","80","80","80",]
lista_jugadores=["V","G","T","B"]
lista_suerte=["Sortir de Presó", "Anar a la presó", "Anar a la sortida", "Anar tres espais enderrere", "Fer reparacions a les propietats:El jugador paga 25$ per cada propietat i 100$ per cada hotel a la banca",
              "Ets escollit alcalde, cada jugador et paga 50$"]
lista_caja=["Sortir de la presó","Anar a la presó", "Error de banca al teu favor; guanyes 150$","Despeses mediques, pagues 50$","Despeses escolars, pagues 50$",
            " Reparacions al carrer, pagues 40$", "Concurs de belleza, guanyes 10$"]
lista_cartas_especiales=["N", "N", "N", "N"]

for x in range(24):
   lista_terrenos.append(0)
   listacasillas.append(x+1)
   listaduenos.append("N")
   lista_casas.append(0)
   lista_hoteles.append(0)
   lista_preciocasa.append(200)
   lista_preciohotel.append(250)
   lista_multacasa.append(10)
   lista_multahotel.append(15)
dineroxjugador=[2000,2000,2000,2000]
banca=500000
lista_posiciones=[0,0,0,0]


def puedocomprar(posicion):
   total = (lista_hoteles[posicion] == 0 and lista_casas[posicion]<4) or (lista_hoteles[posicion]) == 1 and lista_casas
   if (lista_hoteles[posicion] == 0 and lista_casas[posicion]<4) or (lista_hoteles[posicion]) == 1 and lista_casas:
    return total
   
def puedocomprarhotel(posicion):
    total = (lista_hoteles[posicion] < 2 and lista_casas[posicion] <= 2 ) 
    if (lista_hoteles[posicion] == 0 and lista_casas[posicion]<4) or (lista_hoteles[posicion]) == 1 and lista_casas:
     return total


def convertiranumero(cadena):
   if cadena=="V":
       return 0
   if cadena=="G":
       return 1
   if cadena=="T":
       return 2
   if cadena=="B":
       return 3


def muestrasaldos():
   print("Banca    :", banca)
   print("Jugador V:",dineroxjugador[0])
   print("Jugador G:",dineroxjugador[1])
   print("Jugador T:",dineroxjugador[2])
   print("Jugador B:",dineroxjugador[3])

def orden_jugadores():
    V=random.randint(1,12)
    G=random.randint(1,12)
    T=random.randint(1,12)
    B=random.randint(1,12)

    if G < V:
        temp = G
        V = G
        tmp = V
    if G < T:
        temp = G
        T = G
        tmp = G
    if G < B:
        temp = G
        B = G
        tmp = G


#INICIO DE JUEGO
jugadoractual = 0  #jugadores van del 0 al 3
eljuegosigue=True
marca=""
while eljuegosigue:
   print("Juega",lista_jugadores[jugadoractual])
   dado1=random.randint(1,6)
   dado2=random.randint(1,6)
   print("Dado1:",dado1,"-- Dado2:",dado2)
   nuevaposicion=lista_posiciones[jugadoractual]+dado1+dado2
   if nuevaposicion<=28:
       lista_posiciones[jugadoractual]=nuevaposicion
   else:
       #da la vuelta al tablero:
       nuevaposicion=nuevaposicion-28
       lista_posiciones[jugadoractual] = nuevaposicion
       dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]+200
       banca=banca-200


   print(f"Juga {jugadoractual}, ha sortit {dado1} i {dado2}")
   print(f"{jugadoractual} avanza a {listacasillas[nuevaposicion-1]}")
   #INICIO SECCION EL LUGAR ES DE OTRO DUEÑO
   if listaduenos[nuevaposicion]!="N" and listaduenos[nuevaposicion]!=lista_jugadores[jugadoractual]:
       print("Es lugar del jugador",listaduenos[nuevaposicion])
       montoacobrar=(nuevaposicion)
       dineroxjugador[jugadoractual]-=montoacobrar
       jugadordueno = convertiranumero(listaduenos[nuevaposicion])
       dineroxjugador[jugadordueno] += montoacobrar
   # FIN SECCION EL LUGAR ES DE OTRO DUEÑO
   else:
       #INICIO SECCION: -----NO ES DE NADIE O ES TUYO------
       marca="fallo"
       while marca=="fallo":
           rpta=input(f"Juga '{jugadoractual}': passar, comprar casa, comprar hotel, preus")
           if rpta=="comprar casa":
               if listaduenos[nuevaposicion]=="N":
                   if dineroxjugador[jugadoractual]-lista_terrenos>=0:
                       dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]-lista_terrenos
                       banca=banca+lista_terrenos
                       print(f"{jugadoractual} ha comprat {listacasillas[nuevaposicion-1]}")
                       marca="ok"
                   else:
                       print("No tens suficients calés")
                       marca="fallo"
           if rpta=="comprar casa":
               if listaduenos[nuevaposicion] == jugadoractual :
                   valorcasa = lista_preciocasa[nuevaposicion]
                   if puedocomprar(nuevaposicion):
                       if dineroxjugador[jugadoractual]-valorcasa>=0:
                           dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]-valorcasa
                           banca=banca+valorcasa
                           print("Casa comprada")
                           lista_casas[nuevaposicion] += 1
                           marca="ok"
                       else:
                           marca = "fallo"
                   else:
                       marca = "fallo"
               else:
                   marca="fallo"
           if rpta=="H":
               if listaduenos[nuevaposicion] == jugadoractual :
                   valorhotel = lista_preciohotel[nuevaposicion]
                   if puedocomprarhotel(nuevaposicion):
                       if dineroxjugador[jugadoractual]-valorhotel>=0:
                           dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]-valorhotel
                           banca=banca+valorhotel
                           print("Hotel comprat")
                           lista_casas[nuevaposicion]-=2
                           lista_hoteles[nuevaposicion]+=1
                           marca="ok"
                       else:
                           print("No tens suficients calés")
                           marca="fallo"
                   else:
                       print("No es posible comprar")
                       marca = "fallo"
               else:
                   print("No pots comprar el terreny")
                   marca = "fallo"
           if rpta=="preus":
               print(f"{listacasillas[nuevaposicion-1[lista_terrenos]]}")
               marca = "ok"
           if rpta=="passar":
               marca="ok"
           # FIN SECCION: -----NO ES DE NADIE O ES TUYO------
   muestrasaldos()
   if jugadoractual==3:
       jugadoractual=0
   else:
       jugadoractual+=1