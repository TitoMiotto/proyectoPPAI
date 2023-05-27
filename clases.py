from datetime import timedelta, time
class RespuestaDeCliente:
    def __init__(self, fechaEncuesta, respuestaSeleccionada):
        self.fechaEncuesta = fechaEncuesta
        self.respuestaSeleccionada = respuestaSeleccionada

    def getDescripcionRta(self):
        return self.respuestaSeleccionada.getDescripcionRta()

class Llamada:
    def __init__(
        self,
        descripcionOperador,
        detalleAccionRequerida,
        duracion,
        encuestaEnviada,
        observacionAuditor,
        cliente,
        cambioEstado,
        respuestasDeEncuesta,
    ):
        self.descripcionOperador = descripcionOperador
        self.detalleAccionRequerida = detalleAccionRequerida
        self.duracion = duracion
        self.encuestaEnviada = encuestaEnviada
        self.observacionAuditor = observacionAuditor
        self.cambioEstado = cambioEstado
        self.respuestasDeEncuesta = respuestasDeEncuesta
        self.cliente = cliente

    # este metodo solo funciona si los cambios de estados estan ordenados por fecha 
    def calcularDuracion(self):
        suma = timedelta()
        n = len(self.cambioEstado)
        for i in range(n-1):
            suma += self.cambioEstado[i+1].getFechaHoraInicio() - self.cambioEstado[i].getFechaHoraInicio()
        return suma

        

    def determinarEstadoInicial(self):
        return self.cambioEstado.estadoInicial

    def determinarUltimoEstado(self):
        return self.cambioEstado.estadoFinal

    def esDePeriodo(self):
        fechaMenor = self.cambioEstado[0].getFechaHoraInicio()
        for i in self.cambioEstado:
            if i.getFechaHoraInicio() < fechaMenor:
                fechaMenor = i.getFechaHoraInicio()
        return fechaMenor

    def getDuracion(self):
        self.duracion = self.calcularDuracion()
        return self.duracion

    def getNombreClienteDeLlamada(self):
        return self.cliente.getNombre()

    def getRespuestas(self):
        vector = []
        for i in self.respuestasDeEncuesta:
            vector.append(i.getDescripcionRta())
        return vector

    def new():
        pass

    def setDescripcionOperador(self, descripcionOperador):
        self.descripcionOperador = descripcionOperador

    def setDuracion(self, duracion):
        self.duracion = duracion

    def getEstadoActual(self):
        i = self.buscarUltimoEstado()
        return i.getNombreEstado()

    def buscarUltimoEstado(self):
        ultimo = self.cambioEstado[0]
        for i in self.cambioEstado:
            if ultimo.getFechaHoraInicio() < i.getFechaHoraInicio():
                ultimo = i
        return ultimo

    def tieneRespuestas(self):
        return self.encuestaEnviada

class Cliente:
    def __init__(self, dni, nombreCompleto, nroCelular):
        self.dni = dni
        self.nombreCompleto = nombreCompleto
        self.nroCelular = nroCelular

    def esCliente(self, dni):
        return self.dni == dni

    def getNombre(self):
        return self.nombreCompleto

class Estado:
    def __init__(self, nombre):
        self.nombre = nombre

    def esFinalizada(self):
        return self.nombre == "Finalizada"

    def esIniciada(self):
        return self.nombre == "Iniciada"

    def getNombre(self):
        return self.nombre

class CambioEstado:
    def __init__(self, fechaHoraInicio, estado):
        self.fechaHoraInicio = fechaHoraInicio
        self.estado = estado

    def getFechaHoraInicio(self):
        return self.fechaHoraInicio

    def getNombreEstado(self):
        return self.estado.getNombre()

    def new():
        pass

    def esFechaMenor(self, fecha):
        return self.fechaHoraInicio < fecha

class RespuestaPosible:
    def __init__(self, descripcion, valor):
        self.descripcion = descripcion
        self.valor = valor

    def getDescripcionRta(self):
        return self.descripcion

class Pregunta:
    def __init__(self, pregunta, respuesta):
        self.pregunta = pregunta
        self.respuesta = respuesta

    def getDescripcion(self):
        return self.pregunta

    def listarRespuestasPosibles(self):
        lista = []
        for i in self.respuesta:
            lista.append(i.getDescripcionRta())
        return lista

class Encuesta:
    def __init__(self, fechaFinVigencia, descripcion, pregunta):
        self.fechaFinVigencia = fechaFinVigencia
        self.descripcion = descripcion
        self.pregunta = pregunta

    def armarEncuesta(self):
        pass

    def esEncuestaEnPeriodo(self):
        return self.fechaFinVigencia

    def esVigente():
        pass

    def getDescripcionEncuesta(self):
        return self.descripcion

    def getRespuestasPregunta(self):
        vector = []
        for i in self.pregunta:
            vector.append(i.listarRespuestasPosibles())
        return vector
        


# Assuming you have the necessary data for object initialization
descripcion_operador = "Operator description"
detalle_accion_requerida = "Action required details"
duracion = 120
encuesta_enviada = True
observacion_auditor = "Auditor observation"
cliente = Cliente("123456789", "John Doe", "987654321")
cambio_estado = [CambioEstado("2023-05-25 10:00:00", Estado("Iniciada")), CambioEstado("2023-05-25 11:00:00", Estado("Finalizada"))]
respuestas_encuesta = [RespuestaDeCliente("2023-05-25", RespuestaPosible("Yes", 1))]

# Instantiate the object of the Llamada class
llamada = Llamada(
    descripcion_operador,
    detalle_accion_requerida,
    duracion,
    encuesta_enviada,
    observacion_auditor,
    cliente,
    cambio_estado,
    respuestas_encuesta
)

# You can now use the created object as per your requirements
# For example, you can access its attributes or call its methods


