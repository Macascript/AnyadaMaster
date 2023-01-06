from tkinter import Tk, Button
from functools import partial

from screens.lista_materias_primas_page import ListaMateriasPrimasPage
from screens.lista_personal_page import ListaPersonalPage
from screens.historial_page import HistorialPage
from config import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x700")
        self.actual_page_name = materias_primas_page_name
        self.pages = {
            materias_primas_page_name: ListaMateriasPrimasPage,
            personal_page_name: ListaPersonalPage,
            historial_page_name: HistorialPage
        }
        self.actual_page = self.pages[self.actual_page_name](self)

        self.buttons = {
            materias_primas_page_name: Button(self,text=materias_primas_page_name,command=partial(self.change_page,materias_primas_page_name)),
            personal_page_name: Button(self,text=personal_page_name,command=partial(self.change_page,personal_page_name)),
            historial_page_name: Button(self,text=historial_page_name,command=partial(self.change_page,historial_page_name))
        }

        self.buttons[materias_primas_page_name].place(rely=0.3,relx=0.0)
        self.buttons[personal_page_name].place(rely=0.5,relx=0.0)
        self.buttons[historial_page_name].place(rely=0.7,relx=0.0)

    def change_page(self,id):
        if self.actual_page_name == id: return

        self.actual_page.destroy()
        self.actual_page = self.pages[id](self)
        self.actual_page_name = id

if __name__ == "__main__":
    Window().mainloop()