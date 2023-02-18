#DEFINICIÓN DE LA CLASE LISTA CIRCULAR
from nodo import nodo

class lista_circular:
    def __init__(self):
        self.primero = None

    def insertar (self, receta):
        if self.primero is None:
            self.primero = nodo(receta=receta)
            self.primero.siguiente=self.primero
        else:
            actual = nodo(receta = receta, siguiente=self.primero.siguiente)
            self.primero.siguiente = actual
    
    def recorrer(self):
        if self.primero is None:
            return
        actual = self.primero
        print("Paciente: ", actual.receta.paciente, "| Fecha de nacimiento: ", actual.receta.fecha_nac, " | Doctor: ", actual.receta.doctor,  "| Colegiado: ", actual.receta.colegiado, "| Fecha de cita: ", actual.receta.fecha_cita, "| Hora de cita: ", actual.receta.hora_cita, "| Tipo de consulta: ", actual.receta.tipo_consulta, "| Tratamiento: ", actual.receta.tratamiento)
            
        while actual.siguiente != self.primero:
            actual=actual.siguiente
            #print("hola mundo")
            print("Paciente: ", actual.receta.paciente, "| Fecha de nacimiento: ", actual.receta.fecha_nac, " | Doctor: ", actual.receta.doctor,  "| Colegiado: ", actual.receta.colegiado, "| Fecha de cita: ", actual.receta.fecha_cita, "| Hora de cita: ", actual.receta.hora_cita, "| Tipo de consulta: ", actual.receta.tipo_consulta, "| Tratamiento: ", actual.receta.tratamiento)
            #print("Paciente: ", actual.receta.paciente)
            #actual =actual.siguiente

    def eliminar(self, colegiado, fecha_cita, hora_cita):
        actual = self.primero
        anterior = None
        no_encontrado = False
        
        while actual and actual.receta.colegiado != colegiado and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            anterior = actual
            actual = actual.siguiente
            
            if actual == self.primero:
                no_encontrado = True
                print("No encontrado")
                break

        if not no_encontrado:
            if anterior is not None:
                anterior.siguiente = actual.siguiente
                actual.siguiente = None
            else:
                while actual.siguiente != self.primero:
                    actual = actual.siguiente
                actual.siguiente = self.primero.siguiente
                self.primero = self.primero.siguiente

    def modificar(self, paciente, fecha_cita, hora_cita):
        actual = self.primero
        encontrado = False
        
        while actual and actual.receta.paciente != paciente and actual.receta.fecha_cita != fecha_cita and actual.receta.hora_cita != hora_cita:
            actual = actual.siguiente
            
        if actual is not None:
            actual.receta.fecha_cita = fecha_cita
            actual.receta.hora_cita = hora_cita
            encontrado = True

        if not encontrado:
            print("No se encuentra en la lista el dato que busca")