# Este ejemplo toma una lista de números e imprime un diccionario con la cantidad 
# de repeticiones de cada número en la lista
numeros = input("Ingrese la lista de números separada por comas: ")

# Convierte la cadena números en una lista, y se instancia un nuevo diccionario donde se guardarán los números repetidos
lista_numeros = numeros.split(',')
numeros_repetidos_dict = dict()

# Se recorre la lista de números
for numero in lista_numeros:
  # Se obtiene en el diccionario el valor de repeticiones de un número,
  # en caso de no encontrarse devuelve 'None'
  valor_repetido = numeros_repetidos_dict.get(str(numero))

  # En caso de existir alguna coincidencia del número en el diccionario
  # se sube +1 la cantidad de repeticiones para el número encontrado
  if valor_repetido is not None:
    numeros_repetidos_dict.update({ str(numero): valor_repetido + 1 })
  
  # En caso de no encontrar ninguna coincidencia se coloca el número en el diccionario con su primer coincidencia
  else:
    numeros_repetidos_dict.update({ str(numero): 1 })

# Se imprime el diccionario
print(numeros_repetidos_dict)

