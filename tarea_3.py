#ejercicio  4

#como primer acto de amor definimos el autómata
def automata(palabra):
    estado_actual = 'e0'# Estado inicial
    estados_aceptacion = {'e4'}  # Estado final de aceptación
#OJITO el delta se refiere a la función de transición
    delta = {
        ('e0', '0'): 'e1',
        ('e1', '1'): 'e2',
        ('e2', '1'): 'e3',  
        ('e3', '0'): 'e4',
        ('e3', '1'): 'e2',
        ('e4', '0'): 'e4'
    }
# Recorremos la palabra y aplicamos la función de transición
    for simbolo in palabra:
        if (estado_actual, simbolo) in delta:
            estado_actual = delta[(estado_actual, simbolo)]      
        else:
            return False
# Verificamos si el estado actual es un estado de aceptación
    return estado_actual in estados_aceptacion


# Bucle principal para preguntar la palabra al usuario
while True:
    palabra = input("Introduce la palabra (0 y 1) o escribe 'salir': ").strip()
    if palabra.lower() == "salir":
        print("Programa finalizado.")
        break
# Verificamos si la palabra es aceptada por el autómata
    if automata(palabra):
        print("Palabra aceptada")
    else:
        print("Palabra rechazada")