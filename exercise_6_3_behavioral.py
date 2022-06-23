# En este ejemplo voy a explicar e implementar un patrón de diseño comportamental, el elegido es Observer

'''
  Es un patrón que permite definir un mecanismo de suscripción para notificar a uno o más
  objetos sobre cualquier evento que suceda en el ejemplo que están observando

  Más en https://refactoring.guru/es/design-patterns/observer
'''

'''
  De manera básica en el patrón observer existen dos tipos de objetos:
  
  -> subject: Será el objeto el cual queremos saber los eventos que pasen en el, este notificará
  a los otros objetos algun evento de importancia

  -> observer: Son los objetos que quieren conocer algun cambio o evento del 'subject', esté será notificado
  de algún evento de importancia.
'''

# Se define la clase Subject
class Subject():
  # En su contructor tendrá inicializado, una lista de observers, que serán notificados en 
  # caso de algún evento importante
  def __init__(self):
    self._observers = []

  # Este método agrega nuevos observers a la lista anteriormente inicializada
  def subcribir(self, observer):
    self._observers.append(observer)
  
  # Este método remueve observers de la lista anteriormente inicializada
  def desubscribir(self, observer):
    self._observers.remove(observer)
  
  # Este método notifica a cada uno de los observers de la lista, de algún evento de importancia
  def notificar(self):
    print('\nNotificando a los observers...')
    for observer in self._observers:
      observer.reaccionar_evento() # Cada observer tendrá un método reaccionar_evento(), donde se recibirá la notificación

  # Método para simular algún evento de importancia dentro del 'subject'
  def algun_evento_importante(self):
    print('\n¡Ha pasado algo...!')

    # Aquí se notifica a los observers del evento ocurrido
    self.notificar()
  
# Se define la clase Observer
class Observer():
  # Método donde se reaccionara a algún evento ocurrido en el subject al cual estén suscritos
  def reaccionar_evento(self):
    print('Observador a reaccionado a evento...')

# Se crea un objeto subject
subject = Subject()

# Se crea dos observers
observer_a = Observer()
observer_b = Observer()

# Aquí se suscriben al subject, los observers anteriormente instanciados
subject.subcribir(observer_a)
subject.subcribir(observer_b)

'''
  Finalmente, ocurre un evento importante en el subject y se nota, como cada uno de los
  observers que están suscritos, serán notificados y tendrán una reacción frente a él.
'''
subject.algun_evento_importante()


