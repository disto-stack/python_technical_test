# Este ejemplo toma una lista de numero e imprime la sumatoria de los cuadrados de ellos
numeros = input("Ingrese la lista de números separada por comas: ")

# Convierte la cadena numeros en una lista, y se inicializa una variable sumatoria en cero
lista_numeros = numeros.split(',')
sumatoria = 0

# Se recorre la lista de numeros
for numero in lista_numeros:
  numero = int(numero) # Se hace el parseo para evitar errores
  sumatoria += numero * numero # Se suman los cuadrados de cada numero

# Se imprime la sumatoria
print(sumatoria)
  


