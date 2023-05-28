from clases import *
import random
from datetime import datetime, timedelta

#metodo auxiliar para cargar un vector con respuestas posibles
def cargarRespuestas():
    vector = []
    for i in range(3):
        vector.append(RespuestaPosible("respuesta "+str(random.randrange(20)), i))
    return vector
    

#metodo auxiliar para cargar un vector con preguntas
def cargarpreguntas():
    vector = []
    for i in range(3):
        vector.append(Pregunta("Pregunta "+str(random.randint(1, 15)), cargarRespuestas()))
    return vector

#metodo auxiliar para cargar un vector con encuestas
def cargarEncuestas(vector):
    #def __init__(self, fechaFinVigencia, descripcion, pregunta):
    for i in range(2):
        vector.append(Encuesta(datetime(2023,random.randint(1, 12),random.randint(1, 12)), ("encuesta "+str(i)), cargarpreguntas()))

#metodo para mostrar encuesta
def mostrarEncuesta(e):
    print(e.fechaFinVigencia)
    print(e.descripcion)
    for i in e.pregunta:
        print(i.getDescripcion())
        print(i.listarRespuestasPosibles())



#metodo auxiliar para cargar un vector con llamadas
def cargarllamadas(vector):
    estados = ["inicial","finalizada","enProceso"]
    for i in range(5):
        duracion = random.randrange(110)
        encuestaEnviada = random.choice([True])
        cliente = Cliente(random.randrange(42100), "martin", random.randint(351000, 351999))
        fecha = datetime(2023, random.randint(1, 12),random.randint(1,28), random.randrange(20))
        estado = Estado(random.choice(estados))
        cambioEstado = [CambioEstado(fecha, estado), CambioEstado(fecha + timedelta(hours=2) , estado), CambioEstado(fecha + timedelta(hours=3), estado)]
        if encuestaEnviada:
            resEncuesta = []
            print("ingrese las respuestas que tendra la llamada N° ",int(i)+1)
            for i in range(3):
                resEncuesta.append(RespuestaDeCliente(fecha,RespuestaPosible("respuesta "+str(random.randint(0, 14)),i)))
        else:
            resEncuesta = None

        vector.append(Llamada("haland", "una Accion", duracion, encuestaEnviada, "ta bien", cliente, cambioEstado, resEncuesta))


def mostrarRespuestasDeLlamada(llamada):
    vector = llamada.getRespuestas()
    for i in vector:
        print(i)

    #este metodo creo que deberia ser de la pantalla (lo pongo aca para probar lo demas)
def mostrarLlamadas(llamadas):
    for i in llamadas:
        print("en que fecha se hizo",i.esDePeriodo())
        print("tiene encuesta? ",i.encuestaEnviada)
        print("cliente: ",i.cliente.nombreCompleto)
        print()

def prin():
    print("hola")

