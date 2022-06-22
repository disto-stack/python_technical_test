# Este ejemplo toma una lista de numero e imprime un diccionario con el numero 
# de repeticiones de cada numero en la lista
numeros = input("Ingrese la lista de números separada por comas: ")

# Convierte la cadena numeros en una lista, y se instancia un nuevo diccionario donde se guardaran los numeros repetidos
lista_numeros = numeros.split(',')
numeros_repetidos_dict = dict({
  "1": 0
})

# Se recorre la lista de numeros
for numero in lista_numeros:
  # Se obtiene en el diccionario el valor de repeticones de un numero,
  # en caso de no encontrarse devuelve None
  valor_repetido = numeros_repetidos_dict.get(str(numero))

  # En caso de existir alguna coincidencia del numero en el diccionario
  # se sube +1 el numero de repeticiones para el numero encontrado
  if valor_repetido is not None:
    numeros_repetidos_dict.update({ str(numero): valor_repetido + 1 })
  
  # En caso de no encontrar ninguna coincidencia se coloca el numero en el diccionario con su primer coincidencia
  else:
    numeros_repetidos_dict.update({ str(numero): 1 })

# Se imprime el diccionario
print(numeros_repetidos_dict)

