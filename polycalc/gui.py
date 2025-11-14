import tkinter as tk
from tkinter import ttk, messagebox
from .polinomio import Polinomio

class PolyCalcApp(ttk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__(master, padding=10)
        self.grid(sticky="nsew")
        master.title("PolyCalc")
        master.geometry("900x700")
        master.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1)

        self._build_widgets()

    def _build_widgets(self) -> None:
        self.p1_var = tk.StringVar(value="4, -1, 5")
        self.p2_var = tk.StringVar(value="1, 2")
        self.x_var = tk.StringVar(value="2")
        self.y_var = tk.StringVar(value="3")


        # --- INPUT UTENTE ---


        frm_inputs = ttk.LabelFrame(self, text="Input")
        frm_inputs.grid(row=0, column=0, sticky="ew", padx=4, pady=4)
        frm_inputs.columnconfigure(1, weight=1)

        ttk.Label(frm_inputs, text="Polinomio A").grid(row=0, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.p1_var).grid(row=0, column=1, sticky="ew", padx=4, pady=4)
        ttk.Label(frm_inputs, text="Polinomio B").grid(row=1, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.p2_var).grid(row=1, column=1, sticky="ew", padx=4, pady=4)
        ttk.Label(frm_inputs, text="x").grid(row=2, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.x_var, width=12).grid(row=2, column=1, sticky="w", padx=2, pady=4)
        ttk.Label(frm_inputs, text="y").grid(row=3, column=0, sticky="w", padx=4, pady=4)
        ttk.Entry(frm_inputs, textvariable=self.y_var, width=12).grid(row=3, column=1, sticky="w", padx=2, pady=4)



        # --- RIGA DI BOTTONI COLLEGATI AI METODI ---


        frm_btn = ttk.Frame(self)
        frm_btn.grid(row=1, column=0, sticky="ew", padx=4, pady=4)
        for i in range(6):
            frm_btn.columnconfigure(i, weight=1)

        ttk.Button(frm_btn, text="SUM A+B", command=self._somma).grid(row=0, column=0, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="SUB A-B", command=self._sottrazioneAB).grid(row=0, column=1, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="SUB B-A", command=self._sottrazioneBA).grid(row=1, column=1, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="MULT A*B", command=self._moltiplicazione).grid(row=0, column=2, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="MULT A*x", command=self._moltiplicazione_scalareA).grid(row=1, column=2, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="MULT B*x", command=self._moltiplicazione_scalareB).grid(row=2, column=2, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DIV A/B", command=self._divisioneAB).grid(row=0, column=3, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DIV B/A", command=self._divisioneBA).grid(row=1, column=3, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DERIV A'", command=self._derivataA ).grid(row=0, column=4, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="DERIV B'", command=self._derivataB ).grid(row=1, column=4, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="SOLVE A(x)", command=self._valutaA).grid(row=0, column=5, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="SOLVE B(x)", command=self._valutaB).grid(row=1, column=5, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="INTEG A(x)", command=self._integraleA).grid(row=0, column=6, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="INTEG B(x)", command=self._integraleB).grid(row=1, column=6, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="INTEG A(x -> y)", command=self._integraleAxy).grid(row=0, column=7, sticky="ew", padx=2, pady=2)
        ttk.Button(frm_btn, text="INTEG B(x -> y)", command=self._integraleBxy).grid(row=1, column=7, sticky="ew", padx=2, pady=2)

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

    def _get_polinomi(self) -> tuple[Polinomio, Polinomio]:
        p1 = Polinomio(self._parse_list(self.p1_var.get()))
        p2 = Polinomio(self._parse_list(self.p2_var.get()))
        return p1, p2


    def _append(self, line: str) -> None:
        self.txt.insert("end", line + "\n")
        self.txt.see("end")


    def _somma(self) -> None:
        try:
            p, q = self._get_polinomi()
            r = p.somma(q)
            self._append(f"SUM [A+B] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _sottrazioneAB(self) -> None:
        try:
            p, q = self._get_polinomi()
            r = p.sottrazione(q)
            self._append(f"SUB [A-B] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _sottrazioneBA(self) -> None:
        try:
            p, q = self._get_polinomi()
            r = q.sottrazione(p)
            self._append(f"SUB [B-A] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))


    def _moltiplicazione(self) -> None:
        try:
            p, q = self._get_polinomi()
            r = p.moltiplicazione(q)
            self._append(f"MUL [A*B] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))
    
    def _moltiplicazione_scalareA(self) -> None:
        try:
            p, _ = self._get_polinomi()
            x = float(self.x_var.get())
            r = p.moltiplicazione_per_scalare(x)
            self._append(f"MUL [A*{x}] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _moltiplicazione_scalareB(self) -> None:
        try:
            _, p = self._get_polinomi()
            x = float(self.x_var.get())
            r = p.moltiplicazione_per_scalare(x)
            self._append(f"MUL [A*{x}] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))        

    def _divisioneAB(self) -> None:
        try:
            p, q = self._get_polinomi()
            quoz, resto = p.divisione(q)
            self._append(f"DIV [A/B]: Q={quoz}, R={resto}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))
    
    def _divisioneBA(self) -> None:
        try:
            p, q = self._get_polinomi()
            quoz, resto = q.divisione(p)
            self._append(f"DIV [B/A]: Q={quoz}, R={resto}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _derivataA(self) -> None:
        try:
            p, _ = self._get_polinomi()
            r = p.derivata()
            self._append(f"DERIV [A'(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _derivataB(self) -> None:
        try:
            _, q = self._get_polinomi()
            r = q.derivata()
            self._append(f"DERIV [B'(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _valutaA(self) -> None:
        try:
            p, _ = self._get_polinomi()
            x = float(self.x_var.get())
            v = p.valuta(x)
            self._append(f"A({x}) = {v:g}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _valutaB(self) -> None:
        try:
            _ , p = self._get_polinomi()
            x = float(self.x_var.get())
            v = p.valuta(x)
            self._append(f"A({x}) = {v:g}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))
    
    def _integraleA(self) -> None:
        try:
            p, _ = self._get_polinomi()
            r = p.integrale()
            self._append(f"INT [A(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _integraleB(self) -> None:
        try:
            _, p = self._get_polinomi()
            r = p.integrale()
            self._append(f"INT [A(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

    def _integraleAxy(self) -> None:
        try:
            p, _ = self._get_polinomi()
            x = float(self.x_var.get())
            y = float(self.y_var.get())
            r = p.integrale_definito(x,y)
            self._append(f"INT [A(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))
    
    def _integraleBxy(self) -> None:
        try:
            _, p = self._get_polinomi()
            x = float(self.x_var.get())
            y = float(self.y_var.get())
            r = p.integrale_definito(x,y)
            self._append(f"INT [A(x)] = {r}")
        except Exception as e:
            messagebox.showerror("Errore", str(e))

# --- FUNZIONE DI AVVIO INTERFACCIA ----

def main() -> None:
    root = tk.Tk()
    PolyCalcApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()