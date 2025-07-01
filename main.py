from documento import Documento
from musica import Musica
from interface import Interface
from nota_musica import NotaMusica
import tkinter as tk
from conversor import Conversor


def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()


if __name__ == "__main__":
    main()
