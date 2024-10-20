import random
listacasillas=["Sortida", "Lauria", "Rosell", "Sort", "Marina", "Marina","Consell", "Presó",
            "Muntan", "Aribau", "Caixa", "S.Joan", "Aragó", "Parking", "Urquinoa", "Fontan",
            "Sort", "Rambles", "Pl.Cat","Anr pró", " Angel", "Augusta", "Caixa", "Balmes", "Gracia"]
listaduenos=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_casas=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_hoteles=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_preciocasa=["200","225","250","275","300","325","350","375","400","425","450","475","500","525","550","525"]
lista_preciohotel=["250","255","260","265","270","275","280","285","290","300","310","320","330","340","350","360"]
lista_multacasa=["10","10","15","15","20","20","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_multahotel=["N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N","N",]
lista_jugadores=["V","G","T","B"]
for x in range(24):
   listacasillas.append(x+1)
   listaduenos.append("N")
   lista_casas.append(0)
   lista_hoteles.append(0)
   lista_preciocasa.append(30)
   lista_preciohotel.append(100)
   lista_multacasa.append(20)
   lista_multahotel.append(60)
dineroxjugador=[2000,2000,2000,2000]
banca=500000
valorterreno=230
lista_posiciones=[0,0,0,0]


def puedocomprar(posicion):
   if (lista_hoteles[posicion] == 0 and lista_casas[posicion]<4) or (lista_hoteles[posicion] == 1 and lista_casas
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


print("INICIANDO EL JUEGO...")
jugadoractual=0  #jugadores van del 0 al 3
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


   print("Estas en la casilla nro",nuevaposicion,"y la casilla se llama",listacasillas[nuevaposicion-1])
   #INICIO SECCION EL LUGAR ES DE OTRO DUEÑO
   if listaduenos[nuevaposicion]!="N" and listaduenos[nuevaposicion]!=lista_jugadores[jugadoractual]:
       print("Es lugar del jugador",listaduenos[nuevaposicion])
       montoacobrar=cuantocobrar(nuevaposicion)
       dineroxjugador[jugadoractual]-=montoacobrar
       jugadordueno = convertiranumero(listaduenos[nuevaposicion])
       dineroxjugador[jugadordueno] += montoacobrar
   # FIN SECCION EL LUGAR ES DE OTRO DUEÑO
   else:
       #INICIO SECCION: -----NO ES DE NADIE O ES TUYO------
       marca="fallo"
       while marca=="fallo":
           rpta=input("Escoger una opcion: PA pasar, C comprar casa, T comprar terreno, H comprar hotel, PR precios")
           if rpta=="T":
               if listaduenos[nuevaposicion]=="N":
                   if dineroxjugador[jugadoractual]-valorterreno>=0:
                       dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]-valorterreno
                       banca=banca+valorterreno
                       print("Terreno comprado")
                       marca="ok"
                   else:
                       print("No te alcanza para comprar el terreno")
                       marca="fallo"
           if rpta=="C":
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
                           print("No te alcanza para comprar el casa")
                           marca = "fallo"
                   else:
                       print("NO ES POSIBLE COMPRAR.")
                       marca = "fallo"
               else:
                   print("No puedes comprar porque no es tu terreno")
                   marca="fallo"
           if rpta=="H":
               if listaduenos[nuevaposicion] == jugadoractual :
                   valorhotel = lista_preciohotel[nuevaposicion]
                   if puedocomprarhotel(nuevaposicion):
                       if dineroxjugador[jugadoractual]-valorhotel>=0:
                           dineroxjugador[jugadoractual]=dineroxjugador[jugadoractual]-valorhotel
                           banca=banca+valorhotel
                           print("Hotel comprado")
                           lista_casas[nuevaposicion]-=2
                           lista_hoteles[nuevaposicion]+=1
                           marca="ok"
                       else:
                           print("No te alcanza para comprar el hotel")
                           marca="fallo"
                   else:
                       print("NO ES POSIBLE COMPRAR.")
                       marca = "fallo"
               else:
                   print("No puedes comprar hotel porque no es tu terreno")
                   marca = "fallo"
           if rpta=="PR":
               print("MOSTRAR PRECIOS")
               marca = "ok"
           if rpta=="PA":
               print("Fin de jugada. Pasemos al siguiente jugador.")
               marca="ok"
           # FIN SECCION: -----NO ES DE NADIE O ES TUYO------
   muestrasaldos()
   if jugadoractual==3:
       jugadoractual=0
   else:
       jugadoractual+=1