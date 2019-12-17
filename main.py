from tkinter import *
from tkinter import ttk

from Calendar import *
from Calendar import WIDTHBTN, HEIGHTBTN

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Calendario')
        self.geometry("{}x{}".format(WIDTHBTN*7, HEIGHTBTN*7))

        c = Calendar(self)
        c.pack()
        

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.start()
        