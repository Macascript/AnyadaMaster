from tkinter import Tk

from screens.lista_productos_page import ListaProductosPage
from screens.lista_clientes_page import ListaClientesPage

window = Tk()
window.geometry("1500x700")
# actual_page = ListaProductosPage(window)
actual_page = ListaClientesPage(window)


if __name__ == "__main__":
    window.mainloop()