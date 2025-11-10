from dataclasses import dataclass
from math import isclose, sqrt
from typing import List, Tuple


# utilizzo questa costante (0.0000000001) perchè so che in python molti valori float non sono precisi,
# ad esempio se ho 0.001 + 0.001 posso ottenere valori come : 0.0020000002...
# quindi con questa cosatante e la funzione isclose posso accettare un piccolo margine di errore.
TOL = 1e-9

def _normalize(coeffs: List[float]) -> List[float]:
    # Rimuove gli zeri finali dalla lista in input, in modo da non mostrare in interfaccia termini con lo 0.
    i = len(coeffs) - 1
    
    while i >= 0 and isclose(coeffs[i], 0.0, abs_tol=TOL):
        i -= 1
        
    return coeffs[:i+1]


@dataclass(frozen=True)
class Polinomio:
    coefficienti: Tuple[float,...]
    # ---- DEFINIZIONE ED ATTRIBUTI ------

    # sovrascrivo l'__init__ standard del dataclass.
    def __init__(self, coefficienti: List[float] | Tuple[float, ...]):
        coeff_list = list(coefficienti)
        coeff_list = _normalize(coeff_list)
        object.__setattr__(self, "coefficienti", tuple(float(c) for c in coeff_list))
    
    # ---- OPERATORI ALGEBRICI ------

    # somma algebrica di due polinomio (risultato è polinomio di lunghezza = alla maggiore dei due addendi).
    def somma(self, altro: "Polinomio") -> "Polinomio":
        max_len = max(len(self.coefficienti), len(altro.coefficienti))
        result = [0.0]*max_len
        for i in range(max_len):
            a = self.coefficienti[i] if i < len(self.coefficienti) else 0.0
            b = altro.coefficienti[i] if i < len(altro.coefficienti) else 0.0
            result[i] = a + b
        return Polinomio(result)
    
    def sottrazione(self, altro: "Polinomio") -> "Polinomio":
        max_len = max(len(self.coefficienti), len(altro.coefficienti))
        result = [0.0]*max_len
        for i in range(max_len):
            a = self.coefficienti[i] if i < len(self.coefficienti) else 0.0
            b = altro.coefficienti[i] if i < len(altro.coefficienti) else 0.0
            result[i] = a - b
        return Polinomio(result)

    def moltiplicazione(self, altro: "Polinomio") -> "Polinomio":
        if not self.coefficienti or not altro.coefficienti:
            # TODO controllare eventuale errore di moltiplicazione per polinomi vuoti.
            # cosi non credo vada bene per una questione di variabili non inizializzate.
            return Polinomio([])
        result = [0.0] * (len(self.coefficienti) + len(altro.coefficienti) - 1)
        for i, a in enumerate(self.coefficienti):
            for j, b in enumerate(altro.coefficienti):
               result[i + j] += a * b
        return Polinomio(result)

    def moltiplicazione_per_scalare(self, scalare: float) -> "Polinomio":
        if isclose(scalare, 0.0, abs_tol=TOL):
            return Polinomio([])
        return Polinomio([c * scalare for c in self.coefficienti])
    
    def divisione(self, altro: "Polinomio") -> Tuple["Polinomio", "Polinomio"]:
        # TODO sia questo il metodo di divisione A/B, ricordarsi di implementare anche il metodo B/A, 
        # in modo da poter inserire il doppio button nell'interfaccia grafica del calcolatore.
        if not altro.coefficienti:
            raise ZeroDivisionError("Divisione per polinomio zero")
        if not self.coefficienti:
            return Polinomio([]), Polinomio([])


        dividend = list(self.coefficienti)
        divisor = list(altro.coefficienti)
        deg_n = len(dividend) - 1
        deg_d = len(divisor) - 1
        if deg_n < deg_d:
            return Polinomio([]), Polinomio(dividend)


        quotient = [0.0] * (deg_n - deg_d + 1)
        remainder = dividend[:]
        lead_d = divisor[-1]


        for k in range(deg_n - deg_d, -1, -1):
        # Calcola il coefficiente del quoziente per il termine k
            coeff = remainder[deg_d + k] / lead_d
            quotient[k] = coeff
            # Sottrae (coeff * divisore) dal resto
            for j in range(deg_d + 1):
                remainder[j + k] -= coeff * divisor[j]
        return Polinomio(quotient), Polinomio(_normalize(remainder))


        # ---- ANALISI ----

    def get_grado(self) -> int:
        if not self.coefficienti:
            return -1
        return len(self.coefficienti) - 1


    def valuta(self, x: float) -> float:
        acc = 0.0
        for c in reversed(self.coefficienti):
            acc = acc * x + c
        return acc


    def derivata(self) -> "Polinomio":
        if len(self.coefficienti) <= 1:
            return Polinomio([])
        result = [self.coefficienti[i] * i for i in range(1, len(self.coefficienti))]
        return Polinomio(result)


    def integrale(self, costante_di_integrazione: float = 0.0) -> "Polinomio":
        result = [0.0] * (len(self.coefficienti) + 1)
        result[0] = costante_di_integrazione
        for i, c in enumerate(self.coefficienti, start=1):
            result[i] = self.coefficienti[i - 1] / i
        return Polinomio(result)

    def integrale_definito(self, x1: float, x2: float) -> float:
        F = self.integrale(0.0)
        return F.valuta(x2) - F.valuta(x1)

    # --- AVANZATE ---

    def trova_radici(self) -> List[float]:
        if self.get_grado() != 2:
            return []
        c0 = self.coefficienti[0] if len(self.coefficienti) > 0 else 0.0
        c1 = self.coefficienti[1] if len(self.coefficienti) > 1 else 0.0
        c2 = self.coefficienti[2]
        if isclose(c2, 0.0, abs_tol=TOL):
            return []
        delta = c1 * c1 - 4.0 * c2 * c0
        if delta < -TOL:
            return []
        if isclose(delta, 0.0, abs_tol=TOL):
           return [(-c1) / (2.0 * c2)]
        sqrt_delta = sqrt(delta)
        return [(-c1 - sqrt_delta) / (2.0 * c2), (-c1 + sqrt_delta) / (2.0 * c2)]
    

    # --- UTILITY ---

    def __eq__(self, altro: object) -> bool:  
        if not isinstance(altro, Polinomio):
            return False
        a = _normalize(list(self.coefficienti))
        b = _normalize(list(altro.coefficienti))
        if len(a) != len(b):
            return False
        return all(isclose(x, y, abs_tol=TOL) for x, y in zip(a, b))


    def to_string_human(self) -> str:
        if not self.coefficienti:
            return "0"
        terms: List[str] = []
        for power in range(len(self.coefficienti) - 1, -1, -1):
            coeff = self.coefficienti[power]
            if isclose(coeff, 0.0, abs_tol=TOL):
                continue
            sign = "-" if coeff < 0 else "+"
            abs_c = abs(coeff)
            # Build term without sign
            if power == 0:
                core = f"{abs_c:g}"
            elif power == 1:
                if isclose(abs_c, 1.0, abs_tol=TOL):
                    core = "x"
                else:
                    core = f"{abs_c:g}x"
            else:
                if isclose(abs_c, 1.0, abs_tol=TOL):
                    core = f"1x^{power}"
                else:
                    core = f"{abs_c:g}x^{power}"


            if not terms:
                # il primo termine mantiene il segno solo se è negativoo
                if sign == "-":
                    terms.append(f"- {core}")
                else:
                    terms.append(core)
            else:
                terms.append(f"{sign} {core}")
        # unisce e normalizza gli spazi
        s = " ".join(terms)
        return s.replace("+ -", "-").strip()
