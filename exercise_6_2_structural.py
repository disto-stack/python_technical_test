# En este ejemplo voy a explicar e implementar un patrón de diseño estructural, el elegido es Decorator

'''
  Es un patrón que permite añadir nuevos comportamientos a los objetos, colocando estos dentro
  de objetos contenedores especiales(llamados decoradores) que contienen estos comportamientos.

  Más en https://refactoring.guru/design-patterns/decorator
'''


'''
  En el patrón Decorator se implementa una clase abstracta que será extendida por una clase
  decorador y las diferentes clases de objetos que serán decorados.

  Contexto de ejemplo: El siguiente ejemplo se trata de unas figuras, que serán extendidas por 
  la clase Figura, estas en su estado base imprimen o 'dibujan' el tipo de figura que son.
  Lo que se va a hacer en este ejemplo es añadir un comportamiento por medio de un decorador, este
  va a agregarles a las figuras mencionadas un color de borde que será 'dibujado', extendiendo a su vez el 
  comportamiento base
'''

# Se define una clase abstracta, que será la abstracción de todas las figuras
from abc import ABCMeta, abstractmethod

class Figura(metaclass=ABCMeta):

  # Se define una clase abstracta para poder dibujar en cada una de las figuras
  @abstractmethod
  def dibujar(self):
    pass

# Se define una clase que extiende de la clase Figura, este sería un decorador genérico y será la
# abstracción de todos los decoradores
class FiguraDecorador(Figura, metaclass=ABCMeta):

  # En el contructor se define una propiedad, que será la figura que queremos decorar
  def __init__(self, figuraDecorada):
    self.figuraDecorada = figuraDecorada
  
  def dibujar(self):
    self.figuraDecorada.dibujar()

# Ahora se define una clase que hereda del decorador genérico 'FiguraDecorador',
# este va a añadir un nuevo comportamiento a la figura básica que queremos decorar
class FiguraRojaDecorador(FiguraDecorador):

  # En el contructor se define una propiedad, que será la figura que queremos decorar, esta será
  # pasada al padre
  def __init__(self, figuraDecorada):
    super().__init__(figuraDecorada)

  # Se crea un método que modifica el comportamiento de dibujar, añadiendo nuevas características
  # como lo es, agregar un borde rojo al dibujado
  def dibujar(self):
    self.figuraDecorada.dibujar() # Se llama al dibujar 'básico'
    self.setBordeRojo(self.figuraDecorada) # Se añade el dibujar un borde rojo a la figura decorada

  # Se define un método que agrega un borde rojo a la figura a decorar
  def setBordeRojo(self, figuraDecorada):
    print("Borde figura: Roja")


# Se definen las clases Rectangulo y Triangulo, que heredan de Figura.
class Rectangulo(Figura):
  def dibujar(self):
    print('Figura: Rectangulo')

class Triangulo(Figura):
  def dibujar(self):
    print('Figura: Triangulo')

# Se definen las Figuras básicas, estos objetos serán decorados
rectangulo = Rectangulo()
triangulo = Triangulo()

'''
  Como se puede notar, las figuras u objetos a decorar se pasan por el constructor
  de la clases FiguraRojaDecorador. Esta es la manera en que una figura se 'decora' y 
  da como resultado la instancia de un objeto ya decorado
'''
rectanguloRojo = FiguraRojaDecorador(rectangulo)
trianguloRojo = FiguraRojaDecorador(triangulo)


# Se imprimen las figuras sin decorar
print("\n======= Figuras sin decorar =============")
rectangulo.dibujar()
triangulo.dibujar()

# Se imprime el objeto rectangulo decorado
print("\n======= Rectangulo decorado =============")
rectanguloRojo.dibujar()

# Se imprime el objeto triangulo decorado
print("\n======= Triangulo decorado =============")
trianguloRojo.dibujar()
