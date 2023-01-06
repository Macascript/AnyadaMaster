from tkinter import Frame, Toplevel, Button, OptionMenu, StringVar, Label
from tkinter.ttk import Treeview
import datetime
from functools import partial

from config import *
from utils.popup import PopUp
from repository import get_lista_personal, get_next_personal_index, add_personal, get_personal_by_id, update_personal
from utils.entry_placeholder import EntryWithPlaceholder
from models.categoria_laboral import CategoriaLaboral
from models.estado_civil import EstadoCivil
from models.personal import Personal

class ListaPersonalPage(Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.config(bg=bg_color)
        self.create_widgets()
        self.pack_widgets()
        self.fill_table()
    
    def create_widgets(self):
        self.new_personal_window = None
        self.table = Treeview(self,columns=[f"#{x}" for x in range(1,12)])

        self.table.heading("#0",text="Id")
        self.table.column("#0",width=50,anchor="c")

        self.table.heading("#1",text="Nombre")
        self.table.column("#1",width=100,anchor="c")

        self.table.heading("#2",text="Apellidos")
        self.table.column("#2",width=150,anchor="c")

        self.table.heading("#3",text="NIF")
        self.table.column("#3",width=50,anchor="c")

        self.table.heading("#4",text="Seguridad social")
        self.table.column("#4",width=100,anchor="c")

        self.table.heading("#5",text="Fecha nacimiento")
        self.table.column("#5",width=110,anchor="c")

        self.table.heading("#6",text="Domicilio")
        self.table.column("#6",width=100,anchor="c")

        self.table.heading("#7",text="Teléfono")
        self.table.column("#7",width=80,anchor="c")

        self.table.heading("#8",text="Contacto emergencia")
        self.table.column("#8",width=150,anchor="c")

        self.table.heading("#9",text="Categoría laboral")
        self.table.column("#9",width=100,anchor="c")

        self.table.heading("#10",text="Fecha ingreso")
        self.table.column("#10",width=100,anchor="c")

        self.table.heading("#11",text="Estado civil")
        self.table.column("#11",width=100,anchor="c")


        self.table.bind('<ButtonRelease-1>',self.select_item)

        self.add_button = Button(self,text="+",command=self.add_button_command)

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
    
    def pack_widgets(self):
        self.place(rely=0,relx=0.2,relheight=1,relwidth=0.8)
        self.table.pack()
        self.add_button.pack()
    
    # def unpack_widgets(self):
    #     self.add_button.pack_forget()
    #     self.table.pack_forget()
    #     self.place_forget()

    def fill_table(self):
        for personal in get_lista_personal().values():
            self.table.insert("","end",text=personal.id,values=personal.tolist())
    
    def select_item(self,e):
        self.edit_button.pack()
        self.delete_button.pack()
    
    def add_button_command(self):
        self.new_personal_window = PopUpNewPersonal(self.add_personal)
    
    def edit_button_command(self):
        print(self.table.item(self.table.selection())["text"])
        self.new_personal_window = PopUpNewPersonal(self.edit_personal,title="Editar",personal=get_personal_by_id(self.table.item(self.table.selection())["text"]))
    
    def delete_button_command(self):
        personal = self.table.selection()
        self.popup_estas_seguro = PopUp(message="¿Estás seguro de que quieres eliminar al personal?",accept_func=partial(self.delete_personal,personal))
    
    def add_personal(self,personal):
        print(personal)
        self.table.insert("","end",text=personal.id,values=personal.tolist())
        add_personal(personal)
    
    def edit_personal(self,personal):
        print(personal)
        self.table.item(self.table.selection()[0],values=personal.tolist())
        update_personal(personal)
    
    def delete_personal(self,personal):
        self.delete_button.pack_forget()
        self.edit_button.pack_forget()
        self.table.delete(personal)

class PopUpNewPersonal(Toplevel):
    def __init__(self,add_function,title="Nuevo personal",personal=None):
        super().__init__()
        self.personal = personal
        self.categorias = CategoriaLaboral.tolist()
        self.categoria_value = StringVar(self)
        self.categoria_value.set(personal.categoria_laboral.name if personal is not None else "categoría laboral")
        self.estados = EstadoCivil.tolist()
        self.estado_value = StringVar(self)
        self.estado_value.set(personal.estado_civil.name if personal is not None else "estado civil")
        self.config(bg=bg_color)
        self.geometry("1200x100")
        self.title(title)
        self.add_function = add_function

        self.nombre_entry = EntryWithPlaceholder(self,placeholder="nombre")
        if personal is not None:
            self.nombre_entry.delete(0,"end")
            self.nombre_entry.insert(0,personal.nombre)
            self.nombre_entry["fg"] = self.nombre_entry.default_fg_color
        self.nombre_entry.place(rely=0.5, relx=0.0)

        self.apellidos_entry = EntryWithPlaceholder(self,placeholder="apellidos")
        if personal is not None:
            self.apellidos_entry.delete(0,"end")
            self.apellidos_entry.insert(0,personal.apellidos)
            self.apellidos_entry["fg"] = self.apellidos_entry.default_fg_color
        self.apellidos_entry.place(rely=0.5, relx=0.09)

        self.nif_entry = EntryWithPlaceholder(self,placeholder="nif")
        if personal is not None:
            self.nif_entry.delete(0,"end")
            self.nif_entry.insert(0,personal.nif)
            self.nif_entry["fg"] = self.nif_entry.default_fg_color
        self.nif_entry.place(rely=0.5, relx=0.18)

        self.seguridad_social_entry = EntryWithPlaceholder(self,placeholder="seguridad social")
        if personal is not None:
            self.seguridad_social_entry.delete(0,"end")
            self.seguridad_social_entry.insert(0,personal.seguridad_social)
            self.seguridad_social_entry["fg"] = self.seguridad_social_entry.default_fg_color
        self.seguridad_social_entry.place(rely=0.5, relx=0.27)

        self.fecha_nacimiento_entry = EntryWithPlaceholder(self,placeholder="fecha nacimiento")
        if personal is not None:
            self.fecha_nacimiento_entry.delete(0,"end")
            self.fecha_nacimiento_entry.insert(0,personal.fecha_nacimiento.strftime("%d/%m/%Y"))
            self.fecha_nacimiento_entry["fg"] = self.fecha_nacimiento_entry.default_fg_color
        self.fecha_nacimiento_entry.place(rely=0.5, relx=0.36)

        self.domicilio_entry = EntryWithPlaceholder(self,placeholder="domicilio")
        if personal is not None:
            self.domicilio_entry.delete(0,"end")
            self.domicilio_entry.insert(0,personal.domicilio)
            self.domicilio_entry["fg"] = self.domicilio_entry.default_fg_color
        self.domicilio_entry.place(rely=0.5, relx=0.45)

        self.telefono_entry = EntryWithPlaceholder(self,placeholder="teléfono")
        if personal is not None:
            self.telefono_entry.delete(0,"end")
            self.telefono_entry.insert(0,personal.telefono)
            self.telefono_entry["fg"] = self.telefono_entry.default_fg_color
        self.telefono_entry.place(rely=0.5, relx=0.54)

        self.contacto_emergencia_entry = EntryWithPlaceholder(self,placeholder="contacto emergencia")
        if personal is not None:
            self.contacto_emergencia_entry.delete(0,"end")
            self.contacto_emergencia_entry.insert(0,personal.contacto_emergencia)
            self.contacto_emergencia_entry["fg"] = self.contacto_emergencia_entry.default_fg_color
        self.contacto_emergencia_entry.place(rely=0.5, relx=0.63)

        self.categoria_entry = OptionMenu(self,self.categoria_value,*self.categorias)
        self.categoria_entry.place(rely=0.5, relx=0.72)

        self.fecha_ingreso_entry = EntryWithPlaceholder(self,placeholder="fecha ingreso")
        if personal is not None:
            self.fecha_ingreso_entry.delete(0,"end")
            self.fecha_ingreso_entry.insert(0,personal.fecha_ingreso.strftime("%d/%m/%Y"))
            self.fecha_ingreso_entry["fg"] = self.fecha_ingreso_entry.default_fg_color
        self.fecha_ingreso_entry.place(rely=0.5, relx=0.81)

        self.estado_entry = OptionMenu(self,self.estado_value,*self.estados)
        self.estado_entry.place(rely=0.5, relx=0.9)
        

        self.add_button = Button(self,text="Aceptar",command=self.add_button_command)
        self.add_button.pack()

        self.message = Label(self,text="No has introducido los datos correctamente",foreground=error_color,background=bg_color)
    
    def add_button_command(self):
        string = "añadir" if self.personal is None else "editar"
        self.popup_estas_seguro = PopUp(message=f"¿Estás seguro de que quieres {string} al personal?",accept_func=self.add)

    def add(self):
        try:
            nacimiento = self.fecha_nacimiento_entry.get().split("/")
            ingreso = self.fecha_ingreso_entry.get().split("/")
            self.add_function(Personal(
                get_next_personal_index() if self.personal is None else self.personal.id,
                self.nombre_entry.get(),
                self.apellidos_entry.get(),
                self.nif_entry.get(),
                self.seguridad_social_entry.get(),
                datetime.date(
                    int(nacimiento[2]),
                    int(nacimiento[1]),
                    int(nacimiento[0])
                ),
                self.domicilio_entry.get(),
                self.telefono_entry.get(),
                self.contacto_emergencia_entry.get(),
                CategoriaLaboral.strtoenum(self.categoria_value.get()),
                datetime.date(
                    int(ingreso[2]),
                    int(ingreso[1]),
                    int(ingreso[0])
                ),
                EstadoCivil.strtoenum(self.estado_value.get())
            ))
        except Exception as e:
            print(e)
            self.message.pack()
            return
        self.destroy()
