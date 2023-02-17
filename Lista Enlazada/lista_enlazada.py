#Definición de la clase Lista Enlazada
from receta import receta
from nodo import nodo

class lista_enlazada:
    def __init__(self):
        self.primero = None

    def insertar(self, receta):
        if self.primero is None:
            self.primero =  nodo(receta = receta)
            return

        actual = self.primero
        while actual.siguiente:
            actual= actual.siguiente
        actual.siguiente = nodo(receta =receta)

    def recorrer(self):
        actual = self.primero

        while actual != None:
            #print("hola mundo")
            print("Paciente: ", actual.receta.paciente, "| Fecha de nacimiento: ", actual.receta.fecha_nac, " | Doctor: ", actual.receta.doctor,  "| Colegiado: ", actual.receta.colegiado, "| Fecha de cita: ", actual.receta.fecha_cita, "| Hora de cita: ", actual.receta.hora_cita, "| Tipo de consulta: ", actual.receta.tipo_consulta, "| Tratamiento: ", actual.receta.tratamiento)
            #print("Paciente: ", actual.receta.paciente)
            actual =actual.siguiente

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None

        while actual != None and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
        # O puede ser solo "while actual
            anterior = actual
            actual = actual.siguiente
            
        if anterior is None:
            self.primero = actual.siguiente
            actual.siguiente = None
        elif actual:
            anterior.siguiente = actual.siguiente
            actual.siguiente = None


    def modificar(self, paciente, fecha_cita, hora_cita):
        actual = self.primero
        while actual != None and actual.receta.paciente != paciente:
            actual = actual.siguiente

        if actual != None:    
            actual.receta.fecha_cita = fecha_cita
            actual.receta.hora_cita = hora_cita
            print("Se actualizó correctamente")
            # fecha y hora se van a actualizar