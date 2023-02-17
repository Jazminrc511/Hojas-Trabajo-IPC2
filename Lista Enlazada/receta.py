#Definición de la clase receta
class receta:
    def __init__(self, paciente, fecha_nac, doctor, colegiado, fecha_cita, hora_cita, tipo_consulta, tratamiento) :
        self.paciente= paciente
        self.fecha_nac=fecha_nac
        self.doctor=doctor
        self.colegiado=colegiado
        self.fecha_cita=fecha_cita
        self.hora_cita=hora_cita
        self.tipo_consulta=tipo_consulta
        self.tratamiento = tratamiento