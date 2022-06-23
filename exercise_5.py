# En este ejercicio se ingresa una palabra y se imprime el conjunto de anagramas que 
# se forman con esa palabra
palabra = input("Ingrese la palabra a evaluar: ")

# Se instancia un set, ya que es mas eficiente que una lista, y no permite guardar elementos repetidos
anagramas_set = set()


# En este caso se utilizara un algoritmo recursivo para hallar permutaciones, 
# para esta declaramos una funcion que tendrá de parametro la palbra que queremos permutar
# y un i, que sirve para controlar los diferentes entornos generados en un algoritmo recursivo,
# así evitamos un ciclo infinito
def generar_permutaciones(palabra_a_permutar, i = 0):

  # Se guarda un anagrama en el set anteriormente instanciado, esto pasa cuando i alcanza la longitud de las palabras
  if i == len(palabra_a_permutar):

    # El join es porque por los difernetes entornos, las palabras pasan como un arreglo de letras
    anagramas_set.add("".join(palabra_a_permutar)) 


  # Se recorre un arreglo de letras, pero como por cada entorno solo se hara intercambios
  # no conviene hacer un recorrido completo desde j = 0
  for j in range(i, len(palabra_a_permutar)):
    letras = list(palabra_a_permutar) # se convierte la palabra en una lista de letras

    # Se intercambia los valores de la lista de letras en las posiciones i y j
    letras[i], letras[j] = letras[j], letras[i]

    # Se llama un nuevo entorno de manera recursiva
    generar_permutaciones(letras, i + 1)
  
# Se hace el llamado por primera vez a la función anteriormente definida
generar_permutaciones(palabra)

# Se imprime el set de anagramas
print(anagramas_set)
