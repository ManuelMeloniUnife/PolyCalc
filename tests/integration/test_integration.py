import pytest
from polycalc.polinomio import Polinomio
from math import isclose

### --- TEST ALGEBRA --- ###

def test_integrazione_divisione_moltiplicazione_somma():
    """
    verifica che (quoziente * divisore) + resto == dividendo
    questo test combina: divisione(), moltiplicazione(), somma() e __eq__()
    """
    P_dividendo = Polinomio.from_string("5x^3 - 2x^2 + x - 7")
    P_divisore = Polinomio.from_string("x - 1")

    P_quoziente, P_resto = P_dividendo.divisione(P_divisore)

    P_risultato = P_quoziente.moltiplicazione(P_divisore).somma(P_resto)

    assert P_risultato == P_dividendo

def test_integrazione_sottrazione_e_somma():
    """
    verifica che (A + B) - B == A
    usa somma(), sottrazione() e __eq__()
    """
    A = Polinomio.from_string("x^2 + 2x")
    B = Polinomio.from_string("3x^3 - 5")
    
    risultato = A.somma(B).sottrazione(B)
    
    assert risultato == A

### --- TEST ANALISI --- ###

def test_integrazione_derivata_e_integrale():
    """
    Verifica che l'integrale della derivata di un polinomio
    sia uguale al polinomio originale meno la costante di integrazione.
    testa quindi: derivata(), integrale() e __eq__().
    """
    P_originale = Polinomio.from_string("2x^3 - 4x^2 + 5x - 10")
    
    costante_originale = P_originale.coefficienti[0]
    
    P_derivata = P_originale.derivata()
    P_roundtrip = P_derivata.integrale(costante_di_integrazione=costante_originale)
    
    assert P_roundtrip == P_originale

def test_integrazione_radici_e_valuta():
    """
    erifica che le radici trovate da trova_radici()
    restituiscano 0 se usate in valuta().
    combina: trova_radici() e valuta().
    """
    # p = x^2 - 4 -> [ -4, 0, 1 ]. Radici = 2, -2
    p = Polinomio.from_string("x^2 - 4")
    
    radici = p.trova_radici()
    
    assert len(radici) == 2
    
    assert isclose(p.valuta(radici[0]), 0.0, abs_tol=1e-9)
    assert isclose(p.valuta(radici[1]), 0.0, abs_tol=1e-9)

### --- TEST PARSER E UTILITY --- ###

def test_integrazione_from_string_e_to_string_human():
    """
    Verifica che un polinomio convertito in stringa e poi
    riconvertito in polinomio sia uguale all'originale.
    COPRE from_string() e to_string_human().
    """
    s_originale = "x^5 - 3x^3 + 2x - 1"
    
    p = Polinomio.from_string(s_originale)
    
    s_prodotta = p.to_string_human()
    
    p_roundtrip = Polinomio.from_string(s_prodotta)
    
    assert p == p_roundtrip