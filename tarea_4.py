def automata(palabra):
  estado_actual = 'e0'
  estados_aceptacion = {'e3'}  # Estado de aceptación
  delta = {
      ('e0', 'a'): 'e1',
      ('e1', 'a'): 'e2',
      ('e2', 'b'): 'e3',
      ('e3', 'b'): 'e4',
      ('e3', 'c'): 'e3',
      ('e4', 'b'): 'e3',
      ('e4', 'c'): 'e4'
  }

  contador_b = 0  # contar b consecutivas

  for simbolo in palabra:
      if simbolo == 'b':
          contador_b += 1
      elif simbolo == 'c':
          # al encontrar 'c', verificar el grupo anterior de b's
          if contador_b % 2 == 0 and contador_b != 0:
              return False
          contador_b = 0  # reiniciar el conteo
      else:
          contador_b = 0  # si es 'a', resetea grupo de b’s

      if (estado_actual, simbolo) in delta:
          estado_actual = delta[(estado_actual, simbolo)]
      else:
          return False

  # al final también verificamos el último grupo de b's
  if contador_b % 2 == 0 and contador_b != 0:
      return False

  return estado_actual in estados_aceptacion


while True:
  palabra = input("Introduce la palabra (a, b, c) o escribe 'x': ").strip()
  if palabra.lower() == "x":
      print("fin del programa")
      break

  if automata(palabra):
      print("bien")
  else:
      print("mal")