def crear_fila_horizontal(nombres, inicio, fin):
    for i in range(inicio, fin):
        print("+--------+", end=" ")
    print(" ")
    
    for i in range(2):  # Imprimir dos líneas para espacio en las casillas
        for j in range(inicio, fin):
            nombre = nombres[j] if len(nombres) > j else " " * 8
            print(f"|{nombre.center(8)}|", end=" ")
        print(" ")
        
    for i in range(inicio, fin):
        print("+--------+", end=" ")
    print(" ")

def crear_laterales(nombres):
    for i in range(7):
        print("+--------+" + " " * 56 + "+--------+")
        nombre_izq = nombres[i] if len(nombres) > i else " " * 8
        nombre_der = nombres[-(i + 1)] if len(nombres) > (-(i + 1)) else " " * 8
        print(f"|{nombre_izq.center(8)}|" + " " * 56 + f"|{nombre_der.center(8)}|")
        print(f"|{' ' * 8}|" + " " * 56 + f"|{' ' * 8}|")
        print("+--------+" + " " * 56 + "+--------+")

def tablero_monopoly(nombres):
    crear_fila_horizontal(nombres, 0, 7)  # Fila superior
    crear_laterales(nombres)  # Lados izquierdo y derecho
    crear_fila_horizontal(nombres, 7, 14)  # Fila inferior

# Lista de nombres de ejemplo
nombres = ["Inicio", "Avenida", "Ferrocarril", "Suerte", "Electricidad", "Impuesto", "Cárcel", 
           "Visita", "Agua", "Parque", "Hotel", "Estación", "Suerte", "Final"]

# Crear tablero con los nombres
tablero_monopoly(nombres)
