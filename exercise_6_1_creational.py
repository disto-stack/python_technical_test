# En este ejemplo voy a explicar e implementar un patrón de diseño creacional, el elegido es Singleton

'''
  Es un patron que garantiza la creación de una sola instancia de una clase a lo largo del ciclo 
  de vida de una aplicación. Mas en https://www.geeksforgeeks.org/singleton-pattern-in-python-a-complete-guide
'''

# Creamos la clase, en este caso la clase verificará si hay una instancia de la misma, en caso de haberla
# se retornara la instancia ya creada.
class ClaseSingleton():
  '''
    El método __new__ es un metodo estático perteneciente a la clase de un objeto, 
    __new__ se ejecuta antes de __init__, siempre lo hace, lo que significa que si no lo declaramos, 
    este se ejecuta de manera explícita. El primer argumento (cls) se refiere a la clase del objeto
  '''
  def __new__(cls):
    if not hasattr(cls, 'instance'): # Verificamos si existe una instancia de la clase
      cls.instance = super().__new__(cls) # En caso de no haber una instancia, se crea una nueva

    return cls.instance # Se retorna la instancia, ya sea una nueva o una definida anteriormente (Depende del condicional anterior)


# Para demostrar que son las mismas instancias, crearemos dos objetos
singleton = ClaseSingleton()
nuevo_singleton = ClaseSingleton()


# Se verifica las instancias, si está correcta la implementación del patrón, debe dar la salida:
# 'Las dos clases tienen la misma instancia'
if (singleton is nuevo_singleton):
  print('Las dos clases tienen la misma instancia')
else:
  print('Las dos clases no tienen la misma instancia')
  


