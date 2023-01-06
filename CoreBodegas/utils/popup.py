import tkinter as tk

from config import bg_color

class PopUp(tk.Toplevel):
    def __init__(self,resolution="300x200", title="¿Estás seguro?",message="",accept_func=None):
        super().__init__()
        self.config(bg=bg_color)
        self.geometry(resolution)
        self.title(title)
        self.accept_func = accept_func
        self.message_label = tk.Label(self,text=message,background=bg_color)
        self.accept_button = tk.Button(self,text="Aceptar",command=self.accept)
        self.cancel_button = tk.Button(self,text="Volver",command=self.destroy)

        self.message_label.pack(pady=40)
        self.accept_button.place(rely=0.6,relx=0.6)
        self.cancel_button.place(rely=0.6,relx=0.3)

    def accept(self):
        self.accept_func()
        self.destroy()