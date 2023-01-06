from tkinter import Frame, Toplevel, Button, OptionMenu, StringVar, Label
from tkinter.ttk import Treeview
import datetime

from config import *
from repository import get_lista_materias_primas, get_next_materias_primas_index, add_materia_prima, get_materia_prima_by_id, update_materia_prima
from utils.entry_placeholder import EntryWithPlaceholder
from models.materia_prima import MateriaPrima
from models.tipo_uva import TipoUva

class ListaMateriasPrimasPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.create_widgets()
        self.pack_widgets()
        self.fill_table()
    
    def create_widgets(self):
        self.new_materia_prima_window = None
        self.table = Treeview(self,columns=[f"#{x}" for x in range(1,9)])

        self.table.heading("#0",text="Id")
        self.table.column("#0",width=50,anchor="c")

        self.table.heading("#1",text="Nombre")
        self.table.column("#1",width=200,anchor="c")

        self.table.heading("#2",text="Descripción")
        self.table.column("#2",width=200,anchor="c")

        self.table.heading("#3",text="Código origen")
        self.table.column("#3",width=100,anchor="c")

        self.table.heading("#4",text="Cantidad")
        self.table.column("#4",width=70,anchor="c")

        self.table.heading("#5",text="Tipo uva")
        self.table.column("#5",width=100,anchor="c")

        self.table.heading("#6",text="Fecha")
        self.table.column("#6",width=100,anchor="c")

        self.table.heading("#7",text="Madurez")
        self.table.column("#7",width=100,anchor="c")

        self.table.heading("#8",text="Calidad")
        self.table.column("#8",width=100,anchor="c")

        self.table.bind('<ButtonRelease-1>',self.select_item)

        self.add_button = Button(self,text="+",command=self.add_button_command)

        self.delete_button = Button(self,text="x",command=self.delete_button_command)
        self.edit_button = Button(self,text="e",command=self.edit_button_command)
    
    def pack_widgets(self):
        self.place(rely=0,relx=0.2,relheight=1,relwidth=0.8)
        self.table.pack()
        self.add_button.pack()

    def fill_table(self):
        for materia_prima in get_lista_materias_primas().values():
            self.table.insert("","end",text=materia_prima.id,values=materia_prima.tolist())
    
    def select_item(self,e):
        self.edit_button.pack()
        self.delete_button.pack()
    
    def add_button_command(self):
        self.new_materia_prima_window = PopUpNewMateriaPrima(self.add_materia_prima)
    
    def delete_button_command(self):
        self.delete_button.pack_forget()
        self.edit_button.pack_forget()
        self.table.delete(self.table.selection())
    
    def edit_button_command(self):
        print(self.table.item(self.table.selection())["text"])
        self.new_materia_prima_window = PopUpNewMateriaPrima(self.edit_materia_prima,title="Editar",materia_prima=get_materia_prima_by_id(self.table.item(self.table.selection())["text"]))
    
    def edit_materia_prima(self,materia_prima):
        print(materia_prima)
        self.table.item(self.table.selection()[0],values=materia_prima.tolist())
        update_materia_prima(materia_prima)
    
    def add_materia_prima(self,materia_prima):
        print(materia_prima)
        self.table.insert("","end",text=materia_prima.id,values=materia_prima.tolist())
        add_materia_prima(materia_prima)

class PopUpNewMateriaPrima(Toplevel):
    def __init__(self,add_function,title="Nueva materia_prima",materia_prima=None):
        super().__init__()
        self.materia_prima = materia_prima
        self.uvas = TipoUva.tolist()
        self.tipo_uva_value = StringVar(self)
        self.tipo_uva_value.set(materia_prima.tipo_uva.name if materia_prima is not None else "tipo uva")
        self.config(bg=bg_color)
        self.geometry("800x100")
        self.title(title)
        self.add_function = add_function

        self.nombre_entry = EntryWithPlaceholder(self,placeholder="nombre")
        if materia_prima is not None:
            self.nombre_entry.delete(0,"end")
            self.nombre_entry.insert(0,materia_prima.nombre)
            self.nombre_entry["fg"] = self.nombre_entry.default_fg_color
        self.nombre_entry.place(rely=0.5, relx=0.0)

        self.descripcion_entry = EntryWithPlaceholder(self,placeholder="descripcion")
        if materia_prima is not None:
            self.descripcion_entry.delete(0,"end")
            self.descripcion_entry.insert(0,materia_prima.descripcion)
            self.descripcion_entry["fg"] = self.descripcion_entry.default_fg_color
        self.descripcion_entry.place(rely=0.5, relx=0.125)

        self.origen_entry = EntryWithPlaceholder(self,placeholder="código origen")
        if materia_prima is not None:
            self.origen_entry.delete(0,"end")
            self.origen_entry.insert(0,materia_prima.codigo_origen)
            self.origen_entry["fg"] = self.origen_entry.default_fg_color
        self.origen_entry.place(rely=0.5, relx=0.25)

        self.cantidad_entry = EntryWithPlaceholder(self,placeholder="cantidad")
        if materia_prima is not None:
            self.cantidad_entry.delete(0,"end")
            self.cantidad_entry.insert(0,materia_prima.cantidad)
            self.cantidad_entry["fg"] = self.cantidad_entry.default_fg_color
        self.cantidad_entry.place(rely=0.5, relx=0.375)

        self.tipo_uva_entry = OptionMenu(self,self.tipo_uva_value,*self.uvas)
        self.tipo_uva_entry.place(rely=0.5, relx=0.5)

        self.fecha_entry = EntryWithPlaceholder(self,placeholder="fecha")
        if materia_prima is not None:
            self.fecha_entry.delete(0,"end")
            self.fecha_entry.insert(0,materia_prima.fecha.strftime("%m/%Y"))
            self.fecha_entry["fg"] = self.fecha_entry.default_fg_color
        self.fecha_entry.place(rely=0.5, relx=0.625)

        self.madurez_entry = EntryWithPlaceholder(self,placeholder="madurez")
        if materia_prima is not None:
            self.madurez_entry.delete(0,"end")
            self.madurez_entry.insert(0,materia_prima.madurez)
            self.madurez_entry["fg"] = self.madurez_entry.default_fg_color
        self.madurez_entry.place(rely=0.5, relx=0.75)
        
        self.calidad_entry = EntryWithPlaceholder(self,placeholder="calidad")
        if materia_prima is not None:
            self.calidad_entry.delete(0,"end")
            self.calidad_entry.insert(0,materia_prima.calidad)
            self.calidad_entry["fg"] = self.calidad_entry.default_fg_color
        self.calidad_entry.place(rely=0.5, relx=0.875)

        self.add_button = Button(self,text="Aceptar",command=self.add)
        self.add_button.pack()

        self.message = Label(self,text="No has introducido los datos correctamente",foreground=error_color,background=bg_color)
    
    def add(self):
        try:
            calidad = int(self.calidad_entry.get())
            if calidad > 2:
                self.message.config(text="La calidad no puede ser peor que 2 (mayor que 2)")
                self.message.pack()
                return
            
            fecha = self.fecha_entry.get().split("/")
            self.add_function(MateriaPrima(
                get_next_materias_primas_index() if self.materia_prima is None else self.materia_prima.id,
                self.nombre_entry.get(),
                self.descripcion_entry.get(),
                int(self.origen_entry.get()),
                float(self.cantidad_entry.get()),
                TipoUva.strtoenum(self.tipo_uva_value.get()),
                datetime.date(
                    int(fecha[2] if len(fecha) == 3 else fecha[1]),
                    int(fecha[1] if len(fecha) == 3 else fecha[0]),
                    int(fecha[0]) if len(fecha) == 3 else 1
                ),
                int(self.madurez_entry.get()),
                calidad
            ))
        except Exception as e:
            print(e)
            self.message.config(text="No has introducido los datos correctamente")
            self.message.pack()
            return
        self.destroy()
