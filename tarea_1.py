def automata(palabra):
  estado_actual = 'e0'
  estados_aceptacion = {'e4'}
  delta = {
      ('e0', '1'): 'e1',
      ('e1', '1'): 'e2',
      ('e2', '0'): 'e3',
      ('e3', '0'): 'e3',
      ('e3', '1'): 'e4'
  }
  for simbolo in palabra:
      if (estado_actual, simbolo) in delta:
          estado_actual = delta[(estado_actual, simbolo)]
      else:
          return False
  return estado_actual in estados_aceptacion


while True:
  palabra = input("Introduce la palabra (0, 1) o escribe 'salir': ").strip()
  if palabra.lower() == "salir":
      print("Programa finalizado.")
      break

  if automata(palabra):
      print("Palabra aceptada")
  else:
      print("Palabra rechazada")