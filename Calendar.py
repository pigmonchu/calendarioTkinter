from tkinter import *
from tkinter import ttk
from datetime import datetime
from datetime import date
import calendar

dt = datetime.now()

HEIGHTBTN = 50
WIDTHBTN = 50

#FRAMEWORK PARA LOS BOTONES.

class CalButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '14', 'bold'))
        
        self.__btn = ttk.Button(self, text= text, command=command, style='my.TButton')
        self.__btn.pack(side=TOP, expand=True,fill=BOTH)

# FRAMEWORK PARA LAS ETIQUETAS.

class Days(ttk.Frame):    

    def __init__(self, parent, text, foreground, wlabel= 1 ,hlabel=1):
        ttk.Frame.__init__(self, parent, width=WIDTHBTN*wlabel, height=HEIGHTBTN*hlabel)

        self.pack_propagate(0)         
        
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 8')

        self.__lbl = ttk.Label(self, text = text, style='my.TLabel', background='white', foreground= foreground, anchor = CENTER, borderwidth=2, relief="groove")
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)

    
# Clase donde creo todos los botones, etiquetas y métodos de funcionabilidad.
        
class Calendar(ttk.Frame):
    
    mesAnterior = None
    indiceMeses = 0
    indiceAños = 0
    listaMeses =['Enero',' Febrero', 'Marzo','Abril','Mayo','Junio','Julio', 'Agosto','Septiembre','Octubre', 'Noviembre','Diciembre']
    diasSemana = ['Lunes','Martes','Miercoles','Jueves', 'Viernes', 'Sabado', 'Domingo']
    __dates = []
    

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
    
        # CREACIÓN DE LA PRIMERA LÍNEA DEL CALENDARIO. BOTONES +  ETIQUETA QUE INDICA EL MES & AÑO

        self.btn_inicio = CalButton(self, text = '«', command = lambda: self.backFull('«'), hbtn=0.5)
        self.btn_inicio.grid(column = 0, row = 0)
        
        self.btn_volver = CalButton(self, text = '<', command = lambda: self.back('<'), hbtn=0.5)
        self.btn_volver.grid(column=1 ,row=0)

        self.lbl_mes = Days(self, text = str(self.listaMeses[dt.month-1]) + str(' ') + str(dt.year),wlabel= 3, hlabel= 0.5, foreground= 'black')
        self.lbl_mes.grid(column = 2 , row = 0, columnspan = 3)

        self.btn_moveOn = CalButton(self, text = '>', command = lambda: self.moveOn('>'), hbtn=0.5)
        self.btn_moveOn.grid(column = 5, row = 0)

        self.btn_final = CalButton(self, text = '»', command = lambda: self.moveOnFull('»'), hbtn=0.5)
        self.btn_final.grid(column=6, row=0)


        # Creación de los nombres de cada día. Son etiquetas fijas que no varían su texto. Lunes/Martes/X/Jueves/Viernes ...etc
        
        column = 0
        row = 1
        for i in self.diasSemana:            
            
            self.lbl_i = Days(self, text = i, hlabel= 0.5, foreground='black')
            self.lbl_i.grid(column = column, row = row)
                    
            column += 1
        
        #Creación inicial del los días del mes actual. INICIO

        month = dt.month
        year = dt.year
        self.createDays(month, year) # RMR: Reutilizo el código duplicado.

    def createDays(self,month,year):
        '''
        Crea instancias de Days para cada dia y las posiciona adecuadamente.
        Guarda referencias para destruirlas en el cambio de mes
        '''        
        self.deleteDays()
        column = date(year, month , 1).weekday()
        row = 2
        dia = calendar.monthrange(year,month)


        for i in range(1, dia[1]+1):

            if column == 5 or column == 6:
                self.lbl_i = Days(self, text = i, foreground = 'red')
            else:
                self.lbl_i = Days(self, text = i, foreground='black')
            self.lbl_i.grid(column = column, row = row)
            self.__dates.append(self.lbl_i)

            column += 1
            if column == 7:
                column = 0
                row += 1

    # Método para borrar los días y escribir los del nuevo mes.
         
    def deleteDays(self):

        for day in self.__dates:
            day.grid_forget()
            day.update()
            day.destroy()
        
        self.__dates = []

    # Método para ir al primer mes del año, es decir, a Enero.

    def backFull (self, simbolo):

        if simbolo == '«':
            
            self.indiceMeses = -(dt.month) 
            month = dt.month + self.indiceMeses
            year = dt.year + self.indiceAños
            print(month)
            print(self.listaMeses[month])            
            print(year)
            self.muestraMes(str(self.listaMeses[month]) + str(' ') + str(year))
            month = month + 1
            self.createDays(month, year)
                        
        return month

    # Método para ir al mes anterior.

    def back(self, simbolo):

        if simbolo == '<':
            month = dt.month + self.indiceMeses 

            if month  == 0 :
                self.indiceMeses = 12  - dt.month
                self.indiceAños -= 1
                month = dt.month + self.indiceMeses 
                year = dt.year + self.indiceAños
                print(month)
                print(self.listaMeses[month-1])                
                print(year)
                self.indiceMeses -= 1
                self.muestraMes(str(self.listaMeses[month-1]) + str(' ') + str(year))
                self.createDays(month, year)

                
            else: 

                self.indiceMeses -= 1
                month = dt.month + self.indiceMeses
                year = dt.year + self.indiceAños
                print(month)
                print(self.listaMeses[month])
                print(year)
                self.muestraMes(str(self.listaMeses[month]) + str(' ') + str(year))
                month = month + 1
                self.createDays(month, year)
        
        return month

    # Método para ir al último mes del año, es decir, Diciembre.

    def moveOnFull(self,simbolo):

        if simbolo == '»':
            
            self.indiceMeses = 12  - dt.month
            month = dt.month + self.indiceMeses
            year = dt.year + self.indiceAños
            print(month)
            print(self.listaMeses[month-1])
            print(year)
            self.muestraMes(str(self.listaMeses[month-1]) + str(' ') + str(year))
            month = month
            self.createDays(month, year)
        
        return month
    
    # Método para ir al siguiente mes.

    def moveOn(self, simbolo):
        
        if simbolo == '>':           
            
            month = dt.month + self.indiceMeses - 1

            if month  == len(self.listaMeses) - 1  :
                self.indiceMeses = -(dt.month) 
                self.indiceAños += 1
                month = dt.month + self.indiceMeses
                year = dt.year + self.indiceAños
                print(month)
                print(self.listaMeses[month])                
                print(year)
                self.muestraMes(str(self.listaMeses[month]) + str(' ') + str(year))
                month = month + 1
                self.createDays(month, year)
                
                
            else: 

                self.indiceMeses += 1
                month = dt.month + self.indiceMeses 
                year = dt.year + self.indiceAños 
                print(month)
                print(self.listaMeses[month])
                print(year)
                self.muestraMes(str(self.listaMeses[month]) + str(' ') + str(year))
                month = month + 1
                self.createDays(month, year)
               
        return month

    # Método para eliminar el mes anterior y que aparezca en pantalla el nuevo mes seleccionado.

    def muestraMes(self, cadena):

        self.lbl_mes.forget()
        self.lbl_mes = Days(self, text = str(cadena),wlabel= 3, hlabel= 0.5, foreground = 'black')
        self.lbl_mes.grid(column = 2 , row = 0, columnspan = 3)



            

        

        