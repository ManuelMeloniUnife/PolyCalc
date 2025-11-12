import tkinter as tk
from tkinter import ttk, messagebox
from .polinomio import Polinomio

class PolyCalcApp(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, padding=10)
        self.grid(sticky="nsew")
        master.title("PolyCalc")
        master.geometry("640x420")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

def main() -> None:
    root = tk.Tk()
    PolyCalcApp(root)
    root.mainloop()




if __name__ == "__main__":
    main()