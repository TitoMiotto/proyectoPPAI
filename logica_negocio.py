from auxiliar import *
import pickle 
from os import path
from tkinter import *
from tkinter import ttk

class Controlador:
    def __init__(self, pantalla):
        self.llamadas = []
        self.fechaInicio = None
        self.fechaFin = None
        self.llamadaSeleccionada = None
        self.encuestas = []
        self.pantalla = pantalla

        

    def buscarLlamadas(self):
        llamadasauxiliar = []
        for i in self.llamadas:
            if (self.fechaInicio <= i.esDePeriodo() <= self.fechaFin) and i.tieneRespuestas():
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
        duracion = self.llamadaSeleccionada.getDuracion()
        cliente = self.llamadaSeleccionada.getNombreClienteDeLlamada()
        estado = self.llamadaSeleccionada.getEstadoActual()
        respuestas = self.buscarRespuestasDeLlamada()
        encuesta = self.buscarEncuestasLlamada()
        self.pantalla.mostrarLlamada(duracion, cliente, estado, respuestas, encuesta)


    def buscarEncuestasLlamada(self):
        respuestasDelCliente = self.buscarRespuestasDeLlamada()
        n = len(respuestasDelCliente)
        for i in self.encuestas:
            if i.esEncuestaEnPeriodo() < self.llamadaSeleccionada.esDePeriodo():
                continue
            respuestasDeCadaEncuesta = i.getRespuestasPregunta()
            if len(respuestasDeCadaEncuesta) == n:
                for j in range(n):
                    if not (respuestasDelCliente[j] in respuestasDeCadaEncuesta[j]):
                        break
                else:
                    return i

    def buscarRespuestasDeLlamada(self):
        return self.llamadaSeleccionada.getRespuestas()

    def setEncuestas(self, encuestas):
        self.encuestas = encuestas

    def consultarEncuestas(self):
        self.pantalla.solicitarFechasFiltro()
        self.buscarLlamadas()
        self.pantalla.mostrarLlamadas()
        self.buscarDatosLlamada()


    '''def tomarseleccion(self, valor):
        duracion = self.llamadaSeleccionada.getDuracion()
        cliente = self.llamadaSeleccionada.getNombreClienteDeLlamada()
        estado = self.llamadaSeleccionada.getEstadoActual()
        respuestas = self.buscarRespuestasDeLlamada()
        encuesta = self.buscarEncuestasLlamada()
        m.open("archivo.cvs","wt")
        pickle.dump(obj, file)'''



class Pantalla:
    def __init__(self):
        self.pantalla = None
        self.marco = None
        self.gestorConsultasEncuestas = None
        self.fechaInicio = None
        self.fechaFin = None
        
    def consultarEncuestas(self, gestor):
        self.gestorConsultasEncuestas = gestor
        gestor.consultarEncuestas()
        

    
    def generarPantalla(self):
        self.pantalla = Tk()
        self.pantalla.geometry("390x200")
        marco = ttk.Frame(self.pantalla, padding=15)
        marco.grid()
        self.marco = marco
    
    def solicitarFechasFiltro(self):
        self.tomarFechaInicio()
        self.tomarFechaFin()
        self.gestorConsultasEncuestas.tomarFechas(self.fechaInicio, self.fechaFin)

    def aux(self):
        dia = StringVar()
        mes = StringVar()
        año = StringVar()
        ttk.Label(self.marco,text="Dia").grid(column=0,row=1)
        ttk.Label(self.marco,text="Mes").grid(column=0,row=2)
        ttk.Label(self.marco,text="Año").grid(column=0,row=3)
        ttk.Entry(self.marco, textvariable=dia).grid(column=1,row=1)
        ttk.Entry(self.marco, textvariable=mes).grid(column=1,row=2)
        ttk.Entry(self.marco, textvariable=año).grid(column=1,row=3)
        enter = ttk.Button(self.marco, text="Enter", command=self.stop).grid(column=1,row=4)
        mainloop()
        return int(año.get()),int(mes.get()),int(dia.get())
    #cambiar en la secuencia, tomar fecha inicio y despues generar pantalla.
    def tomarFechaInicio(self):
        self.generarPantalla()
        ttk.Label(self.marco, text="Ingrese la fecha de inicio de busqueda").grid()
        año,mes,dia= self.aux()
        self.fechaInicio = datetime(año, mes, dia)

    def tomarFechaFin(self):
        self.generarPantalla()
        ttk.Label(self.marco, text="Ingrese la fecha de fin de busqueda").grid()
        año,mes,dia= self.aux()
        self.fechaFin = datetime(año, mes, dia)
        
    def mostrarLlamadas(self):
        posLlamada = self.tomarLlamada() - 1
        self.gestorConsultasEncuestas.tomarLlamada(posLlamada)

    def stop(self):
        self.pantalla.destroy()

        
    
    def tomarLlamada(self):
        self.generarPantalla()
        #canvas = Canvas(self.pantalla, bg= "red", height= 240)
        #scroll = ttk.Scrollbar(self.pantalla,orient= "vertical", command = canvas.yview)
        #scroll.grid(row=0, column=2, sticky="ns")
        #self.marco = Frame(canvas)
        j = 0
        var = StringVar()
        for i in self.gestorConsultasEncuestas.llamadas:
            j+=1
            llamada = ttk.Radiobutton(self.marco, text="Llamada del "+str(i.esDePeriodo()), variable=var, value=j).grid(row=j)
        boton = ttk.Button(self.marco, text="seleccionar llamada", command=self.stop).grid(column=1)
        mainloop()
        return int(var.get())

    def mostrarLlamada(self, duracion, cliente, estado, respuestas, encuesta):
        self.generarPantalla()
        self.marco.pack()
        etiqueta1 = ttk.Label(self.marco, text="la llamada pertenece a " + str(cliente))
        etiqueta1.pack()
        etiqueta2 = ttk.Label(self.marco, text="duro " + str(duracion.total_seconds()/60) + " minutos")
        etiqueta2.pack()
        etiqueta3 = ttk.Label(self.marco, text="se encuentra " + str(estado))
        etiqueta3.pack()
        etiqueta4 = ttk.Label(self.marco, text="sus respuestas fueron: " + str(respuestas))
        etiqueta4.pack()
        etiqueta5 = ttk.Label(self.marco, text="pertenecen a la " + str(encuesta.getDescripcionEncuesta()))
        etiqueta5.pack()
        marco2 = ttk.Frame(self.marco)
        marco2.pack()
        ttk.Button(marco2, text="cvs", command=lambda:(self.tomarseleccion(0),self.stop())).pack()
        ttk.Button(marco2, text="valores de la encuesta", command=lambda:(self.tomarseleccion(1),self.stop())).pack()
        mainloop()

    def tomarseleccion(self, valor):
        self.gestorConsultasEncuestas.tomarseleccion(valor)

def iniciarCasoDeUso():
    pant = Pantalla()
    gestor = Controlador(pant)
    precarga(gestor)
    pant.consultarEncuestas(gestor)
    



iniciarCasoDeUso()
