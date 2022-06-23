# Este ejemplo toma una lista de números y los ordena de menor a mayor
numeros = input("Ingrese la lista de números separada por comas: ")

# Convierte la cadena números en una lista
lista_numeros = numeros.split(',')

# Se recorre la lista para ordenarla, en este caso se utilizará el ordenamiento burbuja (Bubble sort)
for i in range(len(lista_numeros)):

  # Se hace un segundo recorrido con j hasta la posicion len - i - 1
  # ya que en cada iteración i, no se debe recorrer todo el arreglo,
  # para evitar iteraciones demas y hacer ineficiente el algoritmo
  for j in range(0, len(lista_numeros) - 1):

    # Si el valor en la posicion j es mayor a la posición j + 1,
    # se hace un intercambio entre los valores anteriormente mencionados
    if int(lista_numeros[j]) > int(lista_numeros[j + 1]):
      lista_numeros[j], lista_numeros[j + 1] = lista_numeros[j + 1], lista_numeros[j]

# Se imprime la lista de números
print(lista_numeros)

    