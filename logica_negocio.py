from auxiliar import *

def iniciarCasoDeUso():
    pant = Pantalla()
    gestor = Controlador(pant)
    cargarllamadas(gestor.llamadas)
    cargarEncuestas(gestor.encuestas)
    mostrarLlamadas(gestor.llamadas)


    pant.consultarEncuestas(gestor)

    gestor.tomarFechas(pant.fechaInicio, pant.fechaFin)
    gestor.buscarLlamadas()
    mostrarLlamadas(gestor.llamadas)

    pant.mostrarLlamadas(gestor.llamadas)



iniciarCasoDeUso()
