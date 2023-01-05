from tkinter import Frame, Toplevel, Button, OptionMenu, StringVar, Label, Listbox
from tkinter.ttk import Treeview, Style
import datetime

from config import *
from repository import get_lista_pedidos, get_next_pedidos_index, add_pedido, get_pedido_by_id, update_pedido, get_max_height, get_lista_clientes, get_cliente_by_id, get_producto_by_id, get_lista_productos
from utils.entry_placeholder import EntryWithPlaceholder
from models.pedido import Pedido, Item

class ListaPedidosPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        
        self.create_widgets()
        self.pack_widgets()
        self.fill_table()
        self.style = Style()
        self.style.configure('Treeview', rowheight=get_max_height()) # repace 40 with whatever you need
    
    def create_widgets(self):
        self.new_pedido_window = None
        self.table = Treeview(self,columns=[f"#{x}" for x in range(1,4)])
        

        self.table.heading("#0",text="Id")
        self.table.column("#0",width=50,anchor="c")

        self.table.heading("#1",text="Cliente")
        self.table.column("#1",width=200,anchor="c")

        self.table.heading("#2",text="Descuento")
        self.table.column("#2",width=100,anchor="c")

        self.table.heading("#3",text="Productos")
        self.table.column("#3",width=400,anchor="c")

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
        for pedido in get_lista_pedidos().values():
            self.table.insert("","end",text=pedido.id,values=pedido.tolist())
    
    def select_item(self,e):
        self.edit_button.pack()
        self.delete_button.pack()
    
    def add_button_command(self):
        self.new_pedido_window = PopUpNewPedido(self.add_pedido)
    
    def delete_button_command(self):
        self.delete_button.pack_forget()
        self.edit_button.pack_forget()
        self.table.delete(self.table.selection())
    
    def edit_button_command(self):
        print(self.table.item(self.table.selection())["text"])
        self.new_pedido_window = PopUpNewPedido(self.edit_pedido,title="Editar",pedido=get_pedido_by_id(self.table.item(self.table.selection())["text"]))
    
    def edit_pedido(self,pedido):
        print(pedido)
        self.table.item(self.table.selection()[0],values=pedido.tolist())
        update_pedido(pedido)
    
    def add_pedido(self,pedido):
        print(pedido)
        self.table.insert("","end",text=pedido.id,values=pedido.tolist())
        add_pedido(pedido)

class PopUpNewPedido(Toplevel):
    def __init__(self,add_function,title="Nuevo pedido",pedido=None):
        super().__init__()
        self.pedido = pedido
        self.clientes = [f"({cliente.id}) {cliente.nombre} {cliente.apellidos}" for cliente in get_lista_clientes().values()]
        self.cliente_value = StringVar(self)
        self.cliente_value.set(f"({pedido.cliente.id}) {pedido.cliente.nombre} {pedido.cliente.apellidos}" if pedido is not None else "cliente")
        self.productos = [f"({producto.id}) {producto.nombre}" for producto in get_lista_productos().values()]
        self.producto_value = StringVar(self)
        self.producto_value.set("producto")
        self.config(bg=bg_color)
        self.geometry("700x400")
        self.title(title)
        self.add_function = add_function

        self.cliente_entry = OptionMenu(self,self.cliente_value,*self.clientes)
        self.cliente_entry.place(rely=0.5, relx=0.0)

        self.descuento_entry = EntryWithPlaceholder(self,placeholder="descuento")
        if pedido is not None:
            self.descuento_entry.delete(0,"end")
            self.descuento_entry.insert(0,pedido.descuento)
            self.descuento_entry["fg"] = self.descuento_entry.default_fg_color
        self.descuento_entry.place(rely=0.5, relx=0.3)

        self.producto_entry = OptionMenu(self,self.producto_value,*self.productos)
        self.producto_entry.place(rely=0.5,relx=0.6)

        self.cantidad_entry = EntryWithPlaceholder(self,placeholder="cantidad")
        self.cantidad_entry.place(rely=0.6,relx=0.6)

        self.add_item = Button(self,text="+",command=self.add_item_command)
        self.add_item.place(rely=0.7,relx=0.6)

        self.items_listbox = Listbox(self)
        if pedido is not None:
            for item in pedido.items:
                self.items_listbox.insert("end",f"({item.producto.id}) {item.producto.nombre} x{item.cantidad}")
        self.items_listbox.place(rely=0.3,relx=0.8)

        self.add_button = Button(self,text="Aceptar",command=self.add)
        self.add_button.pack()

        self.message = Label(self,text="No has introducido los datos correctamente",foreground=error_color,background=bg_color)
    
    def add_item_command(self):
        self.items_listbox.insert("end",f"{self.producto_value.get()} x{self.cantidad_entry.get()}")

    def add(self):
        try:
            print(self.items_listbox.get(0,"end"))
            self.add_function(Pedido(
                get_next_pedidos_index() if self.pedido is None else self.pedido.id,
                get_cliente_by_id(int(self.cliente_value.get()[1:].split(")")[0])),
                self.descuento_entry.get(),
                [Item(get_producto_by_id(int(string[1:].split(")")[0])),int(string.split("x")[-1])) for string in self.items_listbox.get(0,"end")]
            ))
        except Exception as e:
            print(e)
            self.message.pack()
            return
        self.destroy()