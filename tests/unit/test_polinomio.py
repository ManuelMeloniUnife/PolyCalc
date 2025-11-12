import math
import pytest
from hypothesis import given, strategies as st
from polycalc import Polinomio

def test_get_grado():
    # primo test sia per la normalizzazione (dovrebbe rimuovere gli 0 e lasciare un polinomio vuoto)
    # quindi dare -1 con get_grado.
    assert Polinomio([0,0]).get_grado() == -1
    # qui testo la rimozione dei due 0s con la normalizzazione e rimane solo 1x^0 -> grado 0.
    assert Polinomio([1,0,0]).get_grado() == 0
    # rimozione del primo 0 a dx, rimane 1x^1+2x^0 -> grado 1
    assert Polinomio([1,2,0]).get_grado() == 1

# --- TEST OPERAZIONI ALGEBRICHE ---

def test_somma_sottrazione():
    p = Polinomio([4,-1,5])
    q = Polinomio([1,2])
    # provo i metodi di somma e sottrazione, anche invertendoli per essere sicuro che non ci siano 
    # strani errori, sempre meglio un test in più.
    assert p.somma(q) == Polinomio([5,1,5])
    assert q.somma(p) == Polinomio([5,1,5])
    assert p.sottrazione(q) == Polinomio([3,-3,5])
    assert q.sottrazione(p) == Polinomio([-3,3,-5])

def test_moltiplicazione():
    p = Polinomio([1,1]) #  (x+1)
    q = Polinomio([1,-1]) # (x-1) 
    assert p.moltiplicazione(q) == Polinomio([1,0,-1]) # x^2 -x +x -1 = x^2 -1
    k = Polinomio([1,2,3])
    assert p.moltiplicazione(k) == Polinomio([1,3,5,3]) #  x^3 + 2x^2 + 3x + x^2 + 2x + 3 -->  x^3 + 3x^2 + 5x +3
    # testo anche le funzioni inverse per evitare errori strani.
    assert q.moltiplicazione(p) == Polinomio([1,0,-1]) 
    assert k.moltiplicazione(p) == Polinomio([1,3,5,3])

def test_molt_scalare():
    p = Polinomio([2, -3])
    assert p.moltiplicazione_per_scalare(0) == Polinomio([0,0])
    assert p.moltiplicazione_per_scalare(1) == Polinomio([2,-3])
    assert p.moltiplicazione_per_scalare(2) == Polinomio([4,-6])
    assert p.moltiplicazione_per_scalare(-2) == Polinomio([-4,6])

def test_divisione_base():
    p = Polinomio([1,0,-1]) # (x^2 - 1)
    d = Polinomio([1,-1]) # (x - 1)
    q, r = p.divisione(d)
    assert q == Polinomio([1,1]) # x +1
    assert r == Polinomio([])

def test_valuta_horner():
    p = Polinomio([4,-1,5]) # quindi: 5x^2 - x + 4
    x = 3
    assert math.isclose(p.valuta(x), 5 * x * x - x + 4 )
    
def test_derivata_integrale():
    p = Polinomio([3,0,2]) #  2x^2 + 3
    dp = p.derivata() # 4x
    assert dp == Polinomio([0,4])
    F = p.integrale(7) # cioè (2/3)x^3 + 3x + 7
    assert F == Polinomio([7, 3, 0, 2/3])

def test_integrale_definito():
    p = Polinomio([0, 1])  # x
    area = p.integrale_definito(0, 2)
    assert math.isclose(area, 2.0)

def test_trova_radici_quadratica():
    p = Polinomio([-1, 0, 1])  # x^2 - 1
    roots = sorted(p.trova_radici())
    assert len(roots) == 2
    assert math.isclose(roots[0], -1.0)
    assert math.isclose(roots[1], 1.0)

def test_to_string_and_str_repr():
    p = Polinomio([5, 0, -2, 1])
    s = p.to_string_human()
    assert s.startswith("1x^3")
    assert "- 2x^2" in s
    assert s.endswith("+ 5") or s.endswith("+5")
    assert str(p) == p.to_string_human()
    assert "Polinomio([" in repr(p)
