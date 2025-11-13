import tkinter as tk
from tkinter import ttk, messagebox
from .polinomio import Polinomio

class PolyCalcApp(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, padding=10)
        self.grid(sticky="nsew")
        master.title("PolyCalc")
        master.geometry("720x500")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self._build_widgets()

    def _build_widgets(self) -> None:
        self.p1_var = tk.StringVar(value="4, -1, 5")
        self.p2_var = tk.StringVar(value="1, 2")
        self.x_var = tk.StringVar(value="2")


        # --- INPUT UTENTE ---


        frm_inputs = ttk.LabelFrame(self, text="Input")
        frm_inputs.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        frm_inputs.columnconfigure(1, weight=1)

        ttk.Label(frm_inputs, text="Polinomio A").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.p1_var).grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        ttk.Label(frm_inputs, text="Polinomio B").grid(row=1, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.p2_var).grid(row=1, column=1, sticky="ew", padx=4, pady=4)
        ttk.Label(frm_inputs, text="x").grid(row=2, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.x_var, width=12).grid(row=2, column=1, sticky="w", padx=4, pady=4)


        # --- RIGA DI BOTTONI COLLEGATI AI METODI ---


        frm_btn = ttk.Frame(self)
        frm_btn.grid(row=1, column=0, sticky="ew", padx=4, pady=4)
        for i in range(6):
            frm_btn.columnconfigure(i, weight=1)

        ttk.Button(frm_btn, text="SUM A+B").grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="SUB A-B").grid(row=0, column=1, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="MULT A*B").grid(row=0, column=2, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DIV A/B").grid(row=0, column=3, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DERIV A'").grid(row=0, column=4, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="VALUE A(x)").grid(row=0, column=5, sticky="ew", padx=2, pady=2)


        # --- CELLA TESTO DI OUTPUT ---


        frm_out = ttk.LabelFrame(self, text="Output")
        frm_out.grid(row=2, column=0, sticky="nsew", padx=4, pady=4)
        self.rowconfigure(2, weight=1)
        frm_out.rowconfigure(0, weight=1)
        frm_out.columnconfigure(0, weight=1)
        self.txt = tk.Text(frm_out, wrap="word")
        self.txt.grid(row=0, column=0, sticky="nsew")

# --- SEZIONE DI IMPLEMENTAZIONE DELLA LOGICA ---
    @staticmethod
    def _parse_list(text: str) -> list[float]:
        try:
            if "," in text:
                parts = [p.strip() for p in text.split(",") if p.strip()]
            else:
                parts = [p.strip() for p in text.split() if p.strip()]
            return [float(p) for p in parts]
        except Exception as exc:
            raise ValueError("Formato coefficienti non valido") from exc



# --- FUNZIONE DI AVVIO INTERFACCIA ----

def main() -> None:
    root = tk.Tk()
    PolyCalcApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()