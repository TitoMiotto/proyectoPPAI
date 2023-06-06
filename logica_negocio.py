from auxiliar import *
import subprocess
from os import path
from tkinter import *
from tkinter import ttk
from reportlab.pdfgen import canvas

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


    def tomarseleccion(self, valor, duracion, cliente, estado, respuestas, encuesta):
        self.generarCSV(duracion, cliente, estado, respuestas, encuesta)
        if valor:
            self.imprimir()

    def generarCSV(self, duracion, cliente, estado, respuestas, encuesta):
        m = open("./archivo.cvs","w")
        #cabecera:
        duracion = str(duracion.total_seconds()/60)
        cabecera = cliente+","+estado+","+duracion+"\n"
        m.write(cabecera)
        preguntas = encuesta.getPreguntas()
        n = len(preguntas)
        for i in range(n):
            m.write(preguntas[i])
            m.write(",")
            m.write(respuestas[i])
            m.write("*\n")
        m.close()

    def imprimir(self):
        c = canvas.Canvas("./archivo.pdf")
    
        with open("./archivo.cvs", 'r') as archivo:
            contenido = archivo.read()
        lineas = contenido.splitlines()
        c.setFont("Helvetica", 12)
        y = 700
        for linea in lineas:
            c.drawString(100, y, linea)
            y -= 15
        c.save()
        subprocess.Popen(["cmd", "/C", "C:/Users/monti/OneDrive/Escritorio/gitppai/proyectoPPAI/archivo.pdf"])

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
        etiqueta1 = ttk.Label(self.marco, text="la llamada pertenece a: " + str(cliente))
        etiqueta1.pack(anchor="w")
        etiqueta2 = ttk.Label(self.marco, text="duro: " + str(duracion.total_seconds()/60) + " minutos")
        etiqueta2.pack(anchor="w")
        etiqueta3 = ttk.Label(self.marco, text="se encuentra: " + str(estado))
        etiqueta3.pack(anchor="w")
        etiqueta4 = ttk.Label(self.marco, text="sus respuestas fueron: " + str(respuestas))
        etiqueta4.pack(anchor="w")
        variable = StringVar()
        if encuesta != None: 
            etiqueta5 = ttk.Label(self.marco, text="pertenecen a la " + str(encuesta.getDescripcionEncuesta()))
        else: 
            etiqueta5 = ttk.Label(self.marco, text="No se encontro encuesta para estas respuestas")
        etiqueta5.pack(anchor="w")
        marco2 = ttk.Frame(self.pantalla)
        marco2.pack(fill="x", expand=True)
        ttk.Button(marco2, text="cvs", command=lambda:(variable.set(0),self.stop())).pack(side="right", anchor="se")
        ttk.Button(marco2, text="imprimir", command=lambda:(variable.set(1),self.stop())).pack(side="left", anchor="sw")
        mainloop()
        self.tomarseleccion(int(variable.get()), duracion, cliente, estado, respuestas, encuesta)

    def tomarseleccion(self, valor, duracion, cliente, estado, respuestas, encuesta):
        self.gestorConsultasEncuestas.tomarseleccion(valor, duracion, cliente, estado, respuestas, encuesta)

#las primeras funciones de esta son prerequisitos para iniciar el caso de uso
def iniciarCasoDeUso():
    pant = Pantalla()
    gestor = Controlador(pant)
    precarga(gestor)
    pant.consultarEncuestas(gestor)
    
iniciarCasoDeUso()
