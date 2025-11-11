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