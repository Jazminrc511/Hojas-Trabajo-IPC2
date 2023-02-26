from nodo import nodo
class lista_doble:
  def __init__(self):
    self.primero = None

  def insertar(self,receta):
    if self.primero is None:
      self.primero = nodo(receta=receta)
    else:
      actual = nodo(receta=receta, siguiente=self.primero)
      self.primero.anterior = actual 
      self.primero = actual #me faltaba esta linea

  def recorrer(self):
    if self.primero is None:
      return
    actual = self.primero 
    print("Paciente:", actual.receta.paciente, 
            "| Fecha de Nacimiento: ", actual.receta.fecha_nac, 
            "| Doctor: ", actual.receta.doctor,
            "| Colegiado: ", actual.receta.colegiado,
            "| Fecha cita: ", actual.receta.fecha_cita,
            "| Hora cita: ", actual.receta.hora_cita,
            "| Consulta: ", actual.receta.tipo_consulta,
            "| Tratamiento: ", actual.receta.tratamiento)
    
    while actual.siguiente:
      actual = actual.siguiente
      print("Paciente:", actual.receta.paciente, 
            "| Fecha de Nacimiento: ", actual.receta.fecha_nac, 
            "| Doctor: ", actual.receta.doctor,
            "| Colegiado: ", actual.receta.colegiado,
            "| Fecha cita: ", actual.receta.fecha_cita,
            "| Hora cita: ", actual.receta.hora_cita,
            "| Consulta: ", actual.receta.tipo_consulta,
            "| Tratamiento: ", actual.receta.tratamiento)
      
  def eliminar(self, colegiado, fecha_cita, hora_cita):
      actual = self.primero
      while actual:
          if actual.receta.colegiado == colegiado and actual.receta.fecha_cita == fecha_cita and actual.receta.hora_cita == hora_cita:
              if actual.anterior:
                  if actual.siguiente:
                      actual.anterior.siguiente = actual.siguiente
                      actual.siguiente.anterior = actual.anterior
                  else:
                      actual.anterior.siguiente = None
              else:
                  if actual.siguiente:
                      self.primero = actual.siguiente
                      actual.siguiente.anterior = None
                  else:
                      self.primero = None
              return True
          else:
              actual = actual.siguiente
      return False

  #Hoja de trabajo 5
  #Modificar

  def buscar(self, Name):
    actual = self.primero
    while actual:
      if actual.receta.paciente == Name:
        print("Encontrado en la lista de pacientes")
        return actual
      actual = actual.siguiente
    print("No se encontro al paciente en la lista")
    return None

  def modificar(self, paciente, fecha_cita, hora_cita):
    nodo_modificar = self.buscar(paciente)
    if nodo_modificar is not None:
      nodo_modificar.receta.fecha_cita = fecha_cita
      nodo_modificar.receta.hora_cita = hora_cita
      print("La información del paciente ha sido actualizada.")
    else:
      print("No se encontró al paciente en la lista.")
  
