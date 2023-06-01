from clases import *
import random


#metodo auxiliar para cargar un vector con respuestas posibles
def cargarRespuestas():
    vector = []
    for i in range(3):
        vector.append(RespuestaPosible("Respuesta "+str(random.randrange(20)), i))
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
    for i in range(3):
        vector.append(Encuesta(datetime(2023,random.randint(1, 12),random.randint(1, 12)), ("encuesta "+str(i)), cargarpreguntas()))

#metodo para mostrar encuesta
def mostrarEncuesta(vector):
    for e in vector:
        print(e.fechaFinVigencia)
        print(e.descripcion)
        for i in e.pregunta:
            print(i.getDescripcion())
            print(i.listarRespuestasPosibles())



#metodo auxiliar para cargar un vector con llamadas
def cargarllamadas(vector):
    estados = ["inicial","finalizada","enProceso"]
    nombres = ("Martin", "Tito", "Franco", "Tomas", "Ignacio", "Eugenia", "Leonardo")
    apellidos = ("Sosa", "Montivero", "Malamud", "Venturini", "Boris")
    for i in range(5):
        duracion = random.randrange(110)
        encuestaEnviada = random.choice([True, False])
        cliente = Cliente(random.randrange(42100), random.choice(nombres) + " " +random.choice(apellidos), random.randint(351000, 351999))
        fecha = datetime(2023, random.randint(1, 12),random.randint(1,28), random.randrange(20))
        estado = Estado(random.choice(estados))
        cambioEstado = [CambioEstado(fecha, estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)) , estado), CambioEstado(fecha + timedelta(minutes=random.randint(1,15)), estado)]
        if encuestaEnviada:
            resEncuesta = []
            for i in range(3):
                resEncuesta.append(RespuestaDeCliente(fecha,RespuestaPosible("Respuesta "+str(random.randint(0, 14)),i)))
        else:
            resEncuesta = None

        vector.append(Llamada("", "", duracion, encuestaEnviada, "", cliente, cambioEstado, resEncuesta))


def cargarLlamadaManual():
    duracion = 1
    encuestaEnviada = True
    cliente = Cliente(random.randrange(42100), input("Ingrese un nombre: "), random.randint(351000, 351999))
    fecha = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")))
    estado = Estado("Finalizado")
    cambioEstado = [CambioEstado(fecha, estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)) , estado), CambioEstado(fecha + timedelta(minutes=random.randint(1,15)), estado)]
    if encuestaEnviada:
        resEncuesta = []
        print("Ingrese las respuestas que tendra una llamada de ejemplo ", 1)
        for i in range(3):
            resEncuesta.append(RespuestaDeCliente(fecha,RespuestaPosible("Respuesta "+ input("Ingrese numero de respuesta: "),i)))
    else:
        resEncuesta = None

    return Llamada("", "", duracion, encuestaEnviada, "", cliente, cambioEstado, resEncuesta)


def mostrarRespuestasDeLlamada(llamada):
    vector = llamada.getRespuestas()
    for i in vector:
        print(i)

    #este metodo creo que deberia ser de la pantalla (lo pongo aca para probar lo demas)
def mostrarLlamadas(llamadas):
    for i in llamadas:
        print("En que fecha se hizo",i.esDePeriodo())
        print("¿Tiene encuesta? ",i.encuestaEnviada)
        print("Cliente: ",i.cliente.nombreCompleto)
        print()
