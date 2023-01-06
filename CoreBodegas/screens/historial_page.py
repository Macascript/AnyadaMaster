from tkinter import Frame, Listbox

from config import *
from repository import get_historial

class HistorialPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.create_widgets()
        self.pack_widgets()
        self.fill_list()
    
    def create_widgets(self):
        self.listbox = Listbox(self)
    
    def pack_widgets(self):
        self.place(rely=0,relx=0.2,relheight=1,relwidth=0.8)
        self.listbox.place(rely=0.01,relx=0.01,relheight=0.8,relwidth=0.98)

    def fill_list(self):
        for log in get_historial():
            self.listbox.insert(0,log)