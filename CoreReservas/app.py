from tkinter import Tk

from screens.lista_productos_page import ListaProductosPage

window = Tk()
window.geometry("1500x700")
actual_page = ListaProductosPage(window)


if __name__ == "__main__":
    window.mainloop()