from tkinter import Frame
from tkinter.ttk import Treeview

from config import bg_color
from repository import get_lista_productos

class ListaProductosPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.place(rely=0,relx=0,relheight=1,relwidth=1)
        self.create_widgets()
        self.fill_table()
    
    def create_widgets(self):
        self.table = Treeview(self,columns=tuple([f"#{x}" for x in range(1,7)]))
        self.table.pack()

        self.table.heading("#0",text="Id")
        self.table.column("#0",width=50,anchor="c")

        self.table.heading("#1",text="Nombre")
        self.table.column("#1",width=200,anchor="c")

        self.table.heading("#2",text="Descripción")
        self.table.column("#2",width=200,anchor="c")

        self.table.heading("#3",text="Precio")
        self.table.column("#3",width=50,anchor="c")

        self.table.heading("#4",text="Formato botella")
        self.table.column("#4",width=150,anchor="c")

        self.table.heading("#5",text="Tipo corcho")
        self.table.column("#5",width=100,anchor="c")

        self.table.heading("#6",text="Cosecha")
        self.table.column("#6",width=100,anchor="c")


        # self.table.column("#0",width=50)
        # for column in self.table["columns"]:
        #     self.table.column(column,width=200)
    
    def fill_table(self):
        for producto in get_lista_productos():
            self.table.insert("",0,text=producto.id,values=producto.tolist())