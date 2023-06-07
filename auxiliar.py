from clases import *
from datetime import datetime, timedelta
import random


def cargarRespuestas():
    return [RespuestaPosible(f"Respuesta {random.randrange(20)}", i) for i in range(3)]

def cargarPreguntas():
    return [Pregunta(f"Pregunta {i}", cargarRespuestas()) for i in range(3)]

def cargarEncuestas(vector):
    for i in range(3):
        vector.append(Encuesta(datetime(2023, random.randint(1, 12), random.randint(1, 12)), f"encuesta {i}", cargarPreguntas()))

def mostrarEncuesta(vector):
    division = "-" * 40
    print(division)
    print("Encuestas generadas automáticamente...")
    for e in vector:
        print(division)
        print(e.descripcion)
        print(division)
        for i in e.pregunta:
            print(f"la {i.getDescripcion()} tiene las siguientes respuestas:")
            print(i.listarRespuestasPosibles())

def cargarllamadas(vector):
    print("Llamadas generadas de forma aleatoria...")
    estados = ["inicial", "finalizada", "enProceso"]
    nombres = ("Martin", "Tito", "Franco", "Tomas", "Ignacio", "Eugenia", "Leonardo")
    apellidos = ("Sosa", "Montivero", "Malamud", "Venturini", "Boris")
    for i in range(5):
        duracion = random.randrange(110)
        encuestaEnviada = random.choice([True])
        cliente = Cliente(random.randrange(42100), f"{random.choice(nombres)} {random.choice(apellidos)}", random.randint(351000, 351999))
        fecha = datetime(2023, random.randint(1, 12), random.randint(1, 28), random.randrange(20))
        estado = Estado(random.choice(estados))
        cambioEstado = [CambioEstado(fecha, estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)), estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)), estado)]
        if encuestaEnviada:
            resEncuesta = [RespuestaDeCliente(fecha, RespuestaPosible(f"Respuesta {random.randint(0, 14)}", i)) for i in range(3)]
        else:
            resEncuesta = None

        vector.append(Llamada("", "", duracion, encuestaEnviada, "", cliente, cambioEstado, resEncuesta))

def cargarLlamadaManual():
    duracion = 1
    encuestaEnviada = True
    print("\nGenerando llamada manualmente...")
    cliente = Cliente(random.randrange(42100), input("Ingrese un nombre: "), random.randint(351000, 351999))
    fecha = datetime(int(input("Año: ")), int(input("Mes: ")), int(input("Dia: ")))
    estado = Estado("Finalizada")
    cambioEstado = [CambioEstado(fecha, estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)), estado), CambioEstado(fecha + timedelta(minutes=random.randint(1, 15)), estado)]
    resEncuesta = [RespuestaDeCliente(fecha, RespuestaPosible(f"Respuesta {input(f'Ingrese el número de una respuesta perteneciente a la pregunta N°{i}: ')}", i)) for i in range(3)]
    return Llamada("", "", duracion, encuestaEnviada, "", cliente, cambioEstado, resEncuesta)

def mostrarRespuestasDeLlamada(llamada):
    vector = llamada.getRespuestas()
    for i in vector:
        print(i)

def mostrarLlamadas(llamadas):
    for i in llamadas:
        print(f"En que fecha se hizo {i.esDePeriodo()}")
        print(f"¿Tiene encuesta? {i.encuestaEnviada}")
        print(f"Cliente: {i.cliente.nombreCompleto}")
        print()

def precarga(gestor):
    cargarEncuestas(gestor.encuestas)
    mostrarEncuesta(gestor.encuestas)
    cargarllamadas(gestor.llamadas)
    gestor.llamadas.append(cargarLlamadaManual())
