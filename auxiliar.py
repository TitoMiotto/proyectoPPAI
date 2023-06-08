from datetime import datetime
from clases import *

# Crear instancia de Cliente
cliente1 = Cliente("12345678", "Juan Pérez", "3001234567")

# Crear instancias de RespuestaPosible
respuesta_posible1 = RespuestaPosible("Sí", 1)
respuesta_posible2 = RespuestaPosible("No", 0)

# Crear instancia de Pregunta con RespuestasPosibles
pregunta1 = Pregunta("¿Está satisfecho con el servicio?", [respuesta_posible1, respuesta_posible2])

# Crear instancia de Encuesta con Preguntas
encuesta1 = Encuesta(datetime(2023, 12, 31), "Encuesta de satisfacción del cliente", [pregunta1])

# Crear instancia de RespuestaDeCliente
respuesta_cliente1 = RespuestaDeCliente(datetime(2023, 7, 6), respuesta_posible1)

# Crear instancias de Estado
estado_inicial = Estado("Iniciada")
estado_final = Estado("Finalizada")

# Crear instancias de CambioEstado
cambio_estado1 = CambioEstado(datetime(2023, 7, 6, 10, 0, 0), estado_inicial)
cambio_estado2 = CambioEstado(datetime(2023, 7, 6, 10, 15, 0), estado_final)

# Crear instancia de Llamada con Cliente y RespuestaDeCliente
llamada1 = Llamada(
    "Operador 1",
    "Desbloquear tarjeta",
    None,  # Se calculará con calcularDuracion()
    True,
    "Buen trato al cliente",
    cliente1,
    [cambio_estado1, cambio_estado2],
    [respuesta_cliente1],
)
