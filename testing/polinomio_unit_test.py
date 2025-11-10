import math
import pytest
from hypothesis import given, strategies as st
from polycalc.polinomio import Polinomio

# --- Test per get_grado() ---

def test_get_grado_standard():
    """Testa un polinomio di grado 2."""
    # 3x^2 + 2x + 1
    p = Polinomio([1, 2, 3])
    assert p.get_grado() == 2

def test_get_grado_costante():
    """Testa un polinomio di grado 0 (una costante)."""
    p = Polinomio([10])
    assert p.get_grado() == 0

def test_get_grado_zero():
    """Testa un polinomio nullo definito come [0]."""
    p = Polinomio([0])
    assert p.get_grado() == 0

def test_get_grado_vuoto():
    """
    Testa il caso limite di una lista coefficienti vuota.
    """
    p = Polinomio([])
    assert p.get_grado() == -1

# --- Test per valuta() ---

def test_valuta_con_x_zero():
    """Testa valuta(x=0), che restituisce il termine noto."""
    # 3x^2 + 2x + 1
    p = Polinomio([1, 2, 3])
    # 3(0)^2 + 2(0) + 1 = 1
    assert p.valuta(0) == 1.0

def test_valuta_con_x_positivo():
    """Testa valuta() con un intero positivo."""
    # 3x^2 + 2x + 1
    p = Polinomio([1, 2, 3])
    # 3(2)^2 + 2(2) + 1 = 12 + 4 + 1 = 17
    assert p.valuta(2) == 17.0

def test_valuta_con_x_negativo():
    """Testa la valutazione con un intero negativo."""
    # p = x^2 - 4x + 4
    p = Polinomio([4, -4, 1])
    # (-3)^2 - 4(-3) + 4 = 9 + 12 + 4 = 25
    assert p.valuta(-3) == 25.0

def test_valuta_con_decimali():
    """Testa la valutazione con input ed output decimali (float)."""
    # p = 0.5x + 7
    p = Polinomio([7, 0.5])
    # 0.5(10) + 7 = 12
    assert p.valuta(10) == pytest.approx(12.0)

def test_valuta_polinomio_vuoto():
    """Testa la valutazione di un polinomio vuoto."""
    p = Polinomio([])
    # acc = 0.0, il ciclo non parte, return 0.0
    assert p.valuta(5) == 0.0

# --- Test per derivata() ---

def test_derivata_standard():
    """Testa la derivata di un polinomio di grado > 1."""
    # p = 3x^2 + 2x + 1
    p = Polinomio([1, 2, 3])
    p_derivata = p.derivata()
    # Derivata = 6x + 2 -> [2, 6]
    assert p_derivata.coefficienti == [2.0, 6.0]

def test_derivata_di_una_retta():
    """Testa la derivata di un polinomio di grado 1."""
    # p = -5x + 10
    p = Polinomio([10, -5])
    p_derivata = p.derivata()
    # Derivata = -5 -> [-5]
    assert p_derivata.coefficienti == [-5.0]

def test_derivata_di_una_costante():
    """
    Testa la derivata di una costante (grado 0),
    che dovrebbe attivare il caso 'len(self.coefficienti) <= 1'.
    """
    p = Polinomio([10])
    p_derivata = p.derivata()
    # Derivata = 0 -> []
    assert p_derivata.coefficienti == []

def test_derivata_di_polinomio_vuoto():
    """
    Testa la derivata di un polinomio vuoto,
    che dovrebbe attivare il caso 'len(self.coefficienti) <= 1'.
    """
    p = Polinomio([])
    p_derivata = p.derivata()
    # Derivata = 0 -> []
    assert p_derivata.coefficienti == []