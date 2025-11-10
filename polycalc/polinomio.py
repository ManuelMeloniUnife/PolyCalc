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