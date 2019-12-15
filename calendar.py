from tkinter import *
from tkinter import ttk
from datetime import datetime

dt = datetime.now()
#print(dt.year)         # año
#print(dt.month)        # mes
#print(dt.day) 

HEIGHTBTN = 50
WIDTHBTN = 50

class CalButton(ttk.Frame):
    def __init__(self, parent, text, command, wbtn=1, hbtn=1):
        ttk.Frame.__init__(self, parent, width=wbtn*WIDTHBTN, height=hbtn*HEIGHTBTN)

        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TButton', font=('Helvetica', '14', 'bold'))
        
        self.__btn = ttk.Button(self, text= text, command=command, style='my.TButton')
        self.__btn.pack(side=TOP, expand=True,fill=BOTH)

    

class Days(ttk.Frame):
    
    

    def __init__(self, parent, text, wlabel= 1 ,hlabel=1):
        ttk.Frame.__init__(self, parent, width=WIDTHBTN*wlabel, height=HEIGHTBTN*hlabel)

        self.pack_propagate(0)         
        
        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font='Helvetica 8')

        self.__lbl = ttk.Label(self, text = text, style='my.TLabel', background='white', foreground='black', anchor = CENTER, borderwidth=2, relief="groove")
        self.__lbl.pack(side=TOP, fill=BOTH, expand=True)

    

        
class Calendar(ttk.Frame):

    indiceMeses = -1
    indiceAños = 0
    listaMeses =['Enero',' Febrero', 'Marzo','Abril','Mayo','Junio','Julio', 'Agosto','Septiembre','Octubre', 'Noviembre','Diciembre']
    diasSemana = ['Lunes','Martes','Miercoles','Jueves', 'Viernes', 'Sabado', 'Domingo']
    

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
    
        # CREACIÓN DE LA PRIMERA LÍNEA DEL CALENDARIO. BOTONES + MES & AÑO
        self.btn_inicio = CalButton(self, text = '«', command = None, hbtn=0.5)
        self.btn_inicio.grid(column = 0, row = 0)
        
        self.btn_volver = CalButton(self, text = '<', command = lambda: self.back('<'), hbtn=0.5)
        self.btn_volver.grid(column=1 ,row=0)
        self.lbl_mes = Days(self, text = str(self.listaMeses[dt.month-1]) + str(' ') + str(dt.year),wlabel= 3, hlabel= 0.5)
        self.lbl_mes.grid(column = 2 , row = 0, columnspan = 3)

        self.btn_avanzar = CalButton(self, text = '>', command = lambda: self.avanzar('>'), hbtn=0.5)
        self.btn_avanzar.grid(column = 5, row = 0)

        self.btn_final = CalButton(self, text = '»', command = None, hbtn=0.5)
        self.btn_final.grid(column=6, row=0)

        # CREACIÓN DE LOS NOMBRES DE LOS DÍAS DE LAS SEMANA
        column = 0
        row = 1
        for i in self.diasSemana:            
            
            self.lbl_i = Days(self, text = i, hlabel= 0.5)
            self.lbl_i.grid(column = column, row = row)
                    
            column += 1
            
    def back(self, simbolo):

        if simbolo == '<':
            month = dt.month + self.indiceMeses - 1

            if month  == 0 :
                self.indiceMeses = 12  - dt.month
                self.indiceAños -= 1
                month = dt.month + self.indiceMeses 
                print(month)
                print(self.listaMeses[month])
                year = dt.year + self.indiceAños
                print(year)
                self.indiceMeses += 1
                self.muestraMes(self.listaMeses[month])

                
            else: 

                self.indiceMeses -= 1
                month = dt.month + self.indiceMeses
                year = dt.year + self.indiceAños
                print(month)
                print(self.listaMeses[month])
                print(year)
                self.muestraMes(self.listaMeses[month])

    
    def avanzar(self, simbolo):
        
        if simbolo == '>':           
            
            month = dt.month + self.indiceMeses - 1

            if month  == len(self.listaMeses) - 1 :
                self.indiceMeses = -(dt.month) 
                self.indiceAños += 1
                month = dt.month + self.indiceMeses
                print(month)
                print(self.listaMeses[month])
                year = dt.year + self.indiceAños
                self.indiceMeses += 1
                print(year)
                self.muestraMes(self.listaMeses[month])

                
            else: 

                self.indiceMeses += 1
                month = dt.month + self.indiceMeses - 1
                year = dt.year + self.indiceAños 
                print(month)
                print(self.listaMeses[month])
                print(year)
                self.muestraMes(self.listaMeses[month])
               
                
    def muestraMes(self, cadena):
        self.cadena = cadena
        self.lbl_mes.config(text=self.cadena)



            

        

        