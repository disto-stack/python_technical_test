# Este ejemplo toma una lista de numero e imprime el menor entre todos ellos
numeros = input("Ingrese la lista de números separada por comas: ")

# Convierte la cadena numeros en una lista
lista_numeros = numeros.split(',')

# Se recorre la lista de numeros
for index in range(len(lista_numeros)):
  # En la primera iteración, el numero menor sera el primero de la lista
  if index == 0:
    numero_menor = lista_numeros[0]
    continue

  # Se compara el número menor hasta el momento, con el numero de la iteracion actual
  if int(lista_numeros[index]) < int(numero_menor):
    numero_menor = lista_numeros[index] # En caso de ser menor, el numero en la posicion 'index' de la lista pasa a ser el menor
  
# Se imprime el numero
print(numero_menor)

  

  
