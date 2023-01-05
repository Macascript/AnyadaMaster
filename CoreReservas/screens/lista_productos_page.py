from tkinter import Frame, Toplevel, Button, OptionMenu, StringVar, Label
from tkinter.ttk import Treeview
import datetime

from config import *
from repository import get_lista_productos, get_next_productos_index, add_producto, get_producto_by_id, update_producto
from utils.entry_placeholder import EntryWithPlaceholder
from models.formato_botella import FormatoBotella
from models.tipo_corcho import TipoCorcho
from models.producto import Producto

class ListaProductosPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.place(rely=0,relx=0,relheight=1,relwidth=1)
        self.create_widgets()
        self.fill_table()
    
    def create_widgets(self):
        self.new_producto_window = None
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

        self.table.bind('<ButtonRelease-1>',self.select_item)

        self.add_button = Button(self,text="+",command=self.add_button_command)
        self.add_button.pack()

        self.delete_button = Button(self,text="x",command=self.delete_button_command)
        self.edit_button = Button(self,text="e",command=self.edit_button_command)

        # self.formatos = FormatoBotella.tolist()
        # self.formato_botella_value = StringVar(self)
        # self.formato_botella_value.set("formato botella")
        # self.formato_botella_entry = OptionMenu(self,self.formato_botella_value,*self.formatos)
        # self.formato_botella_entry.place(rely=0.5, relx=0.51)
        # self.table.column("#0",width=50)
        # for column in self.table["columns"]:
        #     self.table.column(column,width=200)
    
    def fill_table(self):
        for producto in get_lista_productos().values():
            self.table.insert("","end",text=producto.id,values=producto.tolist())
    
    def select_item(self,e):
        self.edit_button.pack()
        self.delete_button.pack()
    
    def add_button_command(self):
        self.new_producto_window = PopUpNewProducto(self.add_producto)
    
    def delete_button_command(self):
        self.delete_button.pack_forget()
        self.edit_button.pack_forget()
        self.table.delete(self.table.selection())
    
    def edit_button_command(self):
        print(self.table.item(self.table.selection())["text"])
        self.new_producto_window = PopUpNewProducto(self.edit_producto,title="Editar",producto=get_producto_by_id(self.table.item(self.table.selection())["text"]))
    
    def edit_producto(self,producto):
        print(producto)
        self.table.item(self.table.selection()[0],values=producto.tolist())
        update_producto(producto)
    
    def add_producto(self,producto):
        print(producto)
        self.table.insert("","end",text=producto.id,values=producto.tolist())
        add_producto(producto)

class PopUpNewProducto(Toplevel):
    def __init__(self,add_function,title="Nuevo producto",producto=None):
        super().__init__()
        self.producto = producto
        self.formatos = FormatoBotella.tolist()
        self.formato_botella_value = StringVar(self)
        self.formato_botella_value.set(f"{producto.formato_botella.value} ({producto.formato_botella.name})" if producto is not None else "formato botella")
        self.corchos = TipoCorcho.tolist()
        self.tipo_corcho_value = StringVar(self)
        self.tipo_corcho_value.set(producto.tipo_corcho.name if producto is not None else "tipo corcho")
        self.config(bg=bg_color)
        self.geometry("700x100")
        self.title(title)
        self.add_function = add_function

        self.nombre_entry = EntryWithPlaceholder(self,placeholder="nombre")
        if producto is not None:
            self.nombre_entry.delete(0,"end")
            self.nombre_entry.insert(0,producto.nombre)
            self.nombre_entry["fg"] = self.nombre_entry.default_fg_color
        self.nombre_entry.place(rely=0.5, relx=0.0)

        self.descripcion_entry = EntryWithPlaceholder(self,placeholder="descripcion")
        if producto is not None:
            self.descripcion_entry.delete(0,"end")
            self.descripcion_entry.insert(0,producto.descripcion)
            self.descripcion_entry["fg"] = self.descripcion_entry.default_fg_color
        self.descripcion_entry.place(rely=0.5, relx=0.17)

        self.precio_entry = EntryWithPlaceholder(self,placeholder="precio")
        if producto is not None:
            self.precio_entry.delete(0,"end")
            self.precio_entry.insert(0,producto.precio)
            self.precio_entry["fg"] = self.precio_entry.default_fg_color
        self.precio_entry.place(rely=0.5, relx=0.34)

        self.formato_botella_entry = OptionMenu(self,self.formato_botella_value,*self.formatos)
        self.formato_botella_entry.place(rely=0.5, relx=0.51)

        self.tipo_corcho_entry = OptionMenu(self,self.tipo_corcho_value,*self.corchos)
        self.tipo_corcho_entry.place(rely=0.5, relx=0.68)

        self.cosecha_entry = EntryWithPlaceholder(self,placeholder="cosecha")
        if producto is not None:
            self.cosecha_entry.delete(0,"end")
            self.cosecha_entry.insert(0,producto.cosecha.strftime("%m/%Y"))
            self.cosecha_entry["fg"] = self.cosecha_entry.default_fg_color
        self.cosecha_entry.place(rely=0.5, relx=0.85)

        self.add_button = Button(self,text="Aceptar",command=self.add)
        self.add_button.pack()

        self.message = Label(self,text="No has introducido los datos correctamente",foreground=error_color,background=bg_color)
    
    def add(self):
        try:
            cosecha = self.cosecha_entry.get().split("/")
            self.add_function(Producto(
                get_next_productos_index() if self.producto is None else self.producto.id,
                self.nombre_entry.get(),
                self.descripcion_entry.get(),
                float(self.precio_entry.get()),
                FormatoBotella.strtoenum(self.formato_botella_value.get()),
                TipoCorcho.strtoenum(self.tipo_corcho_value.get()),
                datetime.date(
                    int(cosecha[2] if len(cosecha) == 3 else cosecha[1]),
                    int(cosecha[1] if len(cosecha) == 3 else cosecha[0]),
                    int(cosecha[0]) if len(cosecha) == 3 else 1
                )
            ))
        except Exception as e:
            print(e)
            self.message.pack()
            return
        self.destroy()
