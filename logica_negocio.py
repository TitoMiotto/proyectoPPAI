from clases import *

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