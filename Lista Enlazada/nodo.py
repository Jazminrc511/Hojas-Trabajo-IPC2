#Definición de la clase Noodo
from receta import receta
class nodo:
    def __init__(self, receta=None, siguiente=None):
        self.receta=receta
        self.siguiente=siguiente