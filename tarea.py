def automata(palabra):
  estado_actual = 'e0'
  estados_aceptacion = {'e2'}
  delta = {
      ('e0', 'a'): 'e1',
      ('e1', 'a'): 'e1',
      ('e1', 'c'): 'e2',
      ('e2', 'b'): 'e2'
  }
  for simbolo in palabra:
      if (estado_actual, simbolo) in delta:
          estado_actual = delta[(estado_actual, simbolo)]
      else:
          return False
  return estado_actual in estados_aceptacion


while True:
  palabra = input("Introduce la palabra (a, b, c) o escribe 'salir': ").strip()
  if palabra.lower() == "salir":
      print("Programa finalizado.")
      break

  if automata(palabra):
      print("Palabra aceptada")
  else:
      print("Palabra rechazada")