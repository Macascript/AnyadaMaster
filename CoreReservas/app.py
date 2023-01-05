from tkinter import Tk, Button
from functools import partial

from screens.lista_productos_page import ListaProductosPage
from screens.lista_clientes_page import ListaClientesPage
from screens.lista_pedidos_page import ListaPedidosPage
from config import *

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1500x700")
        self.actual_page_name = productos_page_name
        self.pages = {
            productos_page_name: ListaProductosPage,
            clientes_page_name: ListaClientesPage,
            pedidos_page_name: ListaPedidosPage
        }
        self.actual_page = self.pages[self.actual_page_name](self)

        self.buttons = {
            productos_page_name: Button(self,text=productos_page_name,command=partial(self.change_page,productos_page_name)),
            clientes_page_name: Button(self,text=clientes_page_name,command=partial(self.change_page,clientes_page_name)),
            pedidos_page_name: Button(self,text=pedidos_page_name,command=partial(self.change_page,pedidos_page_name))
        }

        self.buttons[productos_page_name].place(rely=0.3,relx=0.0)
        self.buttons[clientes_page_name].place(rely=0.5,relx=0.0)
        self.buttons[pedidos_page_name].place(rely=0.7,relx=0.0)

    def change_page(self,id):
        if self.actual_page_name == id: return

        self.actual_page.destroy()
        self.actual_page = self.pages[id](self)
        self.actual_page_name = id

if __name__ == "__main__":
    Window().mainloop()