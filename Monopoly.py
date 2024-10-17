import turtle
pantalla = turtle.Screen()
pantalla_titulo = pantalla.title("Monopoly")
pantalla.setup(width=1024, height=768)


dibujador = turtle.Turtle()
velocidad_tablero = dibujador.speed(0)


def dibujar_casilla(tamaño):
    for _ in range(4):
        dibujador.forward(tamaño)
        dibujador.right(90)

def dibujar_tablero(tamaño_casilla, num_casillas):
        for x in range (4):
            for y in range(num_casillas):
                dibujar_casilla(tamaño_casilla)
                dibujador.forward(tamaño_casilla)
            dibujador.right(90)

def escribir_dentro_casilla(num_casilla, texto):
     lado = (num_casilla -1) // num_casilla
     posicion = (num_casilla -1) % num_casilla
     horizontal = -num_casilla * 100 / 2 + posicion * 100
     vertical = 300 if lado ==  0 else -300 if lado == 2 else 300 - (posicion * 100)
     dibujador.penup()
     dibujador.goto(horizontal + 100 / 2, vertical- 100/2 )
     dibujador.pendown()
     dibujador.write(texto, align ="center", font=("Arial", 12, "normal"))


dibujador.penup()
dibujador.goto(-350,350)
dibujador.pendown()

dibujar_tablero(100,7)





turtle.done()