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
    # qui ho desiso di usare "isclose" poiche spesso mi vengono restituite 
    # le radici con qualche decimale sgarrato molto dopo la virgola
    assert math.isclose(roots[0], -1.0)
    assert math.isclose(roots[1], 1.0)

    # -- TEST FUNZIONI DI UTILITY E PARSER --
    # per quello che riguarda la conversione fa polinomio a stringa e viceversa,
    # ho preferito implementare diversi scenari per essere sicuro che qualsiasi fosse
    #la dimensione e il grado del polinomio, la funzione di conversione e il parser
    # funzionassero.... ho quindi testato tutte le casistiche.

def test_to_string_and_str_repr():
    p = Polinomio([5, 0, -2, 1])
    s = p.to_string_human()
    assert s.startswith("1x^3")
    assert "- 2x^2" in s
    assert s.endswith("+ 5") or s.endswith("+5")
    assert str(p) == p.to_string_human()
    assert "Polinomio([" in repr(p)

def test_from_string_roundtrip_simple():
    s = "x^2 - x + 1"
    p = Polinomio.from_string(s)
    
    # primo test: Il parsing è corretto
    assert p == Polinomio([1, -1, 1])
    
    # Test 2: Il "ritorno a stringa" è corretto (normalizzando entrambi)
    s_normalizzata = "1x^2 - x + 1" 
    output_normalizzato = p.to_string_human().replace(" ", "").replace("+", " + ").replace("-", " - ")
    # questo assert confronta le normalizzazioni e controlla che siano uguali, giusto per essere sicuri
    assert output_normalizzato == s_normalizzata

def test_to_string_polinomio_nullo():
    p_vuoto = Polinomio([])
    assert p_vuoto.to_string_human() == "0"
    p_zero = Polinomio([0, 0, 0]) 
    assert p_zero.to_string_human() == "0"

def test_to_string_costante():
    p_pos = Polinomio([5])
    assert p_pos.to_string_human() == "5" 

    p_neg = Polinomio([-5])
    assert p_neg.to_string_human() == "- 5" 

def test_to_string_potenza_uno():
    p_x = Polinomio([0, 1]) 
    assert p_x.to_string_human() == "x"
    
    p_meno_x = Polinomio([0, -1])
    assert p_meno_x.to_string_human() == "- x"
    
    p_3x = Polinomio([0, 3])
    assert p_3x.to_string_human() == "3x"

def test_to_string_potenza_superiore():
    
    p_x2 = Polinomio([0, 0, 1])
    assert p_x2.to_string_human() == "1x^2" 
    p_meno_x2 = Polinomio([0, 0, -1])
    assert p_meno_x2.to_string_human() == "- 1x^2"
    
    p_3x2 = Polinomio([0, 0, 3])
    assert p_3x2.to_string_human() == "3x^2"

def test_to_string_polinomio_completo_con_buchi():
    p = Polinomio([1, -2, 0, 5])
    
    assert p.to_string_human() == "5x^3 - 2x + 1"
    
    p2 = Polinomio([-1, 0, 1])
    assert p2.to_string_human() == "1x^2 - 1"

# DOPO OI TEST SOPRA LA COPERTURA DEL CODICE TESTATO ERA CIRCA DELL'92%
# IL RESTANTE 8% SONO TUTTI ERRORE GESTIONI DEGLI ERRORI E CASI SPECIALI 
# (es. in trova_radici 'if self.get_grado() !=2 : return []')
# la sezione sottostante testa anche queste casistiche 8il più possibile per provare
# add avvicinarsi al 100% del codice coperto.

# righe scoperte -> 57, 73, 75, 83, 118, 138, 143, 146, 148, 157, 161, 206, 225, 237 

def test_copertura_get_grado_polinomio_vuoto():
    # copre il caso if not self.coefficienti in get_grado.
    p = Polinomio([])
    assert p.get_grado() == -1

def test_copertura_divisione_per_zero():
    # copre il caso divisione d divisone di un polinomio per zero.
    p1 = Polinomio([1, 2, 3])
    p_zero = Polinomio([])
    
    with pytest.raises(ZeroDivisionError, match="Divisione per polinomio zero"):
        p1.divisione(p_zero)

def test_copertura_divisione_grado_inferiore():
    # copre il caso di divisione con polin. di grado inferiore
    p_num = Polinomio([1, 2]) 
    p_den = Polinomio([1, 2, 3]) 
    
    quoz, resto = p_num.divisione(p_den)
    
    assert quoz == Polinomio([])
    assert resto == p_num

def test_copertura_trova_radici_grado_non_2():
    # Copre l'eeorre di trova_radici su un polinomio di grado diverso da 2.
    p_grado_3 = Polinomio([1, 2, 3, 4])
    assert p_grado_3.trova_radici() == []
    
    p_grado_1 = Polinomio([1, 2])
    assert p_grado_1.trova_radici() == []