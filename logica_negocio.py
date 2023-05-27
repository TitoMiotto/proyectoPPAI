from clases import *
from auxiliar import *
from datetime import datetime, timedelta

class Controlador:
    def __init__(self):
        self.llamadas = []
        self.fechaInicio = None
        self.fechaFin = None
        self.llamadaSeleccionada = None
        self.encuestas = []
        

    def buscarLlamadas(self):
        llamadasauxiliar = []
        for i in self.llamadas:
            if (self.fechaInicio < i.esDePeriodo() < self.fechaFin) and i.tieneRespuestas():
                llamadasauxiliar.append(i)
        self.llamadas = llamadasauxiliar

    #metodo para setear las fechas
    def tomarFechas(self, fechaHoraInicio, fechaHoraFin):
        self.fechaInicio = fechaHoraInicio
        self.fechaFin = fechaHoraFin

    #metodo para setear la llamada seleccionada
    def tomarLlamada(self, posicionLlamada):
        if posicionLlamada < len(self.llamadas):
            self.llamadaSeleccionada = self.llamadas[posicionLlamada]

    def buscarDatosLlamada(self):
        return self.llamadaSeleccionada.getDuracion(),self.llamadaSeleccionada.getNombreClienteDeLlamada(),self.llamadaSeleccionada.getEstadoActual()

    #este metodo creo que deberia ser de la pantalla (lo pongo aca para probar lo demas)
    def mostrarLlamadas(self):
        for i in self.llamadas:
            print("en que fecha se hizo",i.esDePeriodo())
            print("tiene encuesta? ",i.encuestaEnviada)
            print("cliente: ",i.cliente.nombreCompleto)
            print()

    def buscarEncuestasLlamada(self):
        respuestasDelCliente = self.buscarRespuestasDeLlamada()
        n = len(respuestasDelCliente)
        for i in self.encuestas:
            if i.esEncuestaEnPeriodo() < self.llamadaSeleccionada.esDePeriodo():
                continue
            respuestasDeCadaEncuesta = i.getRespuestasPregunta()
            if len(respuestasDeCadaEncuesta) == n:
                for j in range(n):
                    print(respuestasDelCliente[j],respuestasDeCadaEncuesta[j])
                    if not (respuestasDelCliente[j] in respuestasDeCadaEncuesta[j]):
                        break
                else:
                    return i

    def buscarRespuestasDeLlamada(self):
        return self.llamadaSeleccionada.getRespuestas()

    def setEncuestas(self, encuestas):
        self.encuestas = encuestas

def test():


    controlador = Controlador()

    cargarEncuestas(controlador.encuestas)
    mostrarEncuesta(controlador.encuestas[1])

    cargarllamadas(controlador.llamadas)
    controlador.tomarFechas(datetime(2023,1,1), datetime(2023,12,29))
    controlador.buscarLlamadas()
    controlador.tomarLlamada(int(input("seleccione la llamada: "))-1)
    print(controlador.buscarDatosLlamada())
    mostrarRespuestasDeLlamada(controlador.llamadaSeleccionada)
    

    mostrarEncuesta(controlador.buscarEncuestasLlamada())



test()