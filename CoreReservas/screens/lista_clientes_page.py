from tkinter import Frame, Toplevel, Button, Label
from tkinter.ttk import Treeview, Style
import datetime
from functools import partial

from config import *
from utils.popup import PopUp
from repository import get_lista_clientes, get_next_clientes_index, add_cliente, get_cliente_by_id, update_cliente, delete_cliente
from utils.entry_placeholder import EntryWithPlaceholder
from models.cliente import Cliente

class ListaClientesPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.create_widgets()
        self.pack_widgets()
        self.fill_table()
        self.style = Style()
        self.style.configure('Treeview', rowheight=20)
    
    def create_widgets(self):
        self.new_cliente_window = None
        self.popup_estas_seguro = None
        self.table = Treeview(self,columns=[f"#{x}" for x in range(1,7)])

        self.table.heading("#0",text="Id")
        self.table.column("#0",width=50,anchor="c")

        self.table.heading("#1",text="Nombre")
        self.table.column("#1",width=200,anchor="c")

        self.table.heading("#2",text="Apellidos")
        self.table.column("#2",width=200,anchor="c")

        self.table.heading("#3",text="Nif")
        self.table.column("#3",width=50,anchor="c")

        self.table.heading("#4",text="Dirección")
        self.table.column("#4",width=150,anchor="c")

        self.table.heading("#5",text="Teléfono")
        self.table.column("#5",width=100,anchor="c")

        self.table.heading("#6",text="Fecha Nacimiento")
        self.table.column("#6",width=100,anchor="c")

        self.table.bind('<ButtonRelease-1>',self.select_item)

        self.add_button = Button(self,text="+",command=self.add_button_command)

        self.delete_button = Button(self,text="x",command=self.delete_button_command)
        self.edit_button = Button(self,text="e",command=self.edit_button_command)
    
    def pack_widgets(self):
        self.place(rely=0,relx=0.2,relheight=1,relwidth=0.8)
        self.table.pack()
        self.add_button.pack()
    
    # def unpack_widgets(self):
    #     self.add_button.pack_forget()
    #     self.table.pack_forget()
    #     self.place_forget()

    def fill_table(self):
        for cliente in get_lista_clientes().values():
            self.table.insert("","end",text=cliente.id,values=cliente.tolist())
    
    def select_item(self,e):
        self.edit_button.pack()
        self.delete_button.pack()
    
    def add_button_command(self):
        self.new_cliente_window = PopUpNewCliente(self.add_cliente)
    
    def edit_button_command(self):
        print(self.table.item(self.table.selection())["text"])
        self.new_cliente_window = PopUpNewCliente(self.edit_cliente,title="Editar",cliente=get_cliente_by_id(self.table.item(self.table.selection())["text"]))
    
    def delete_button_command(self):
        cliente = self.table.selection()
        self.popup_estas_seguro = PopUp(message="¿Estás seguro de que quieres eliminar el cliente?",accept_func=partial(self.delete_cliente,cliente))
    
    def add_cliente(self,cliente):
        print(cliente)
        self.table.insert("","end",text=cliente.id,values=cliente.tolist())
        add_cliente(cliente)
    
    def edit_cliente(self,cliente):
        print(cliente)
        self.table.item(self.table.selection()[0],values=cliente.tolist())
        update_cliente(cliente)

    def delete_cliente(self,cliente):
        self.delete_button.pack_forget()
        self.edit_button.pack_forget()
        delete_cliente(get_cliente_by_id(self.table.item(cliente)["text"]))
        self.table.delete(cliente)

class PopUpNewCliente(Toplevel):
    def __init__(self,add_function,title="Nuevo cliente",cliente=None):
        super().__init__()
        self.popup_estas_seguro = None
        self.cliente = cliente
        self.config(bg=bg_color)
        self.geometry("700x100")
        self.title(title)
        self.add_function = add_function

        self.nombre_entry = EntryWithPlaceholder(self,placeholder="nombre")
        if cliente is not None:
            self.nombre_entry.delete(0,"end")
            self.nombre_entry.insert(0,cliente.nombre)
            self.nombre_entry["fg"] = self.nombre_entry.default_fg_color
        self.nombre_entry.place(rely=0.5, relx=0.0)

        self.apellidos_entry = EntryWithPlaceholder(self,placeholder="apellidos")
        if cliente is not None:
            self.apellidos_entry.delete(0,"end")
            self.apellidos_entry.insert(0,cliente.apellidos)
            self.apellidos_entry["fg"] = self.apellidos_entry.default_fg_color
        self.apellidos_entry.place(rely=0.5, relx=0.17)

        self.nif_entry = EntryWithPlaceholder(self,placeholder="nif")
        if cliente is not None:
            self.nif_entry.delete(0,"end")
            self.nif_entry.insert(0,cliente.nif)
            self.nif_entry["fg"] = self.nif_entry.default_fg_color
        self.nif_entry.place(rely=0.5, relx=0.34)

        self.direccion_entry = EntryWithPlaceholder(self,placeholder="direccion")
        if cliente is not None:
            self.direccion_entry.delete(0,"end")
            self.direccion_entry.insert(0,cliente.direccion)
            self.direccion_entry["fg"] = self.direccion_entry.default_fg_color
        self.direccion_entry.place(rely=0.5, relx=0.51)

        self.telefono_entry = EntryWithPlaceholder(self,placeholder="telefono")
        if cliente is not None:
            self.telefono_entry.delete(0,"end")
            self.telefono_entry.insert(0,cliente.telefono)
            self.telefono_entry["fg"] = self.telefono_entry.default_fg_color
        self.telefono_entry.place(rely=0.5, relx=0.68)

        self.fecha_nacimiento_entry = EntryWithPlaceholder(self,placeholder="fecha_nacimiento")
        if cliente is not None:
            self.fecha_nacimiento_entry.delete(0,"end")
            self.fecha_nacimiento_entry.insert(0,cliente.fecha_nacimiento.strftime("%d/%m/%Y"))
            self.fecha_nacimiento_entry["fg"] = self.fecha_nacimiento_entry.default_fg_color
        self.fecha_nacimiento_entry.place(rely=0.5, relx=0.85)

        self.add_button = Button(self,text="Aceptar",command=self.add_button_command)
        self.add_button.pack()

        self.message = Label(self,text="No has introducido los datos correctamente",foreground=error_color,background=bg_color)
    
    def add_button_command(self):
        string = "añadir" if self.cliente is None else "editar"
        self.popup_estas_seguro = PopUp(message=f"¿Estás seguro de que quieres {string} el cliente?",accept_func=self.add)

    def add(self):
        try:
            fecha_nacimiento = self.fecha_nacimiento_entry.get().split("/")
            self.add_function(Cliente(
                get_next_clientes_index() if self.cliente is None else self.cliente.id,
                self.nombre_entry.get(),
                self.apellidos_entry.get(),
                self.nif_entry.get(),
                self.direccion_entry.get(),
                self.telefono_entry.get(),
                datetime.date(
                    int(fecha_nacimiento[2]),
                    int(fecha_nacimiento[1]),
                    int(fecha_nacimiento[0])
                )
            ))
        except Exception as e:
            print(e)
            self.message.pack()
            return
        self.destroy()
