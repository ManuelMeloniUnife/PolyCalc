from dataclasses import dataclass
from math import isclose, sqrt
from typing import List, Tuple

TOL = 1e-9

def _normalize(coeffs: List[float]) -> List[float]:
    # Rimuove gli zeri finali dalla lista in input, in modo da non mostrare in interfaccia termini con lo 0.
    i = len(coeffs) - 1
    
    while i >= 0 and isclose(coeffs[i], 0.0, abs_tol=TOL):
        i -= 1
        
    return coeffs[:i+1]

