import argparse
from .polinomio import Polinomio # imprta la classe polinomio.

def start_bash_app():
    parser = argparse.ArgumentParser(description="PolyCalc CLI")

    # qui dico ad argparse che voglio usare sub-commands
    # dest=".." salva quale sub commands sto chiamando quindi la seguente
    # è una riga generale dove viene "appoggiato" il sub commands chiamato

    subparsers = parser.add_subparsers(dest="command", required = True, help="Azione principale da eseguire.")

# --- SUBPARSER VALUTA ---
    parser_valuta = subparsers.add_parser('solve', help="Valuta un polinomio per un valore di x inserito.")
    parser_valuta.add_argument(
        '--polinomio', #argomento polinomio necessario per il parser "valuta"
        type = str,
        required = True,
        help = "Polinomio da valutare, scritto in stringa, con o senza spazi. (es. '3x^2+1' o '3x^2 + 1')"
    )
    parser_valuta.add_argument(
        '--xvalue', # argomento valore x necessario per il parser "valuta"
        type = float,
        required = True,
        help = "Valore di x per cui valutare il polinomio."
    )

# --- SUBPARSER SOMMA ---
    parser_somma = subparsers.add_parser('sum', help="somma due polinomi P1 e P2.")
    parser_somma.add_argument(
        '--p1', # argomento polinomio 1 necessario per il parser "somma"
        type = str,
        required = True,
        help = "Polinomio P1 da sommare, scritto in stringa, con o senza spazi. (es. '3x^2+1' o '3x^2 + 1')"
    )
    parser_somma.add_argument(
        '--p2', # argomento polinomio 2 necessario per il parser "somma"
        type = str,
        required = True,
        help = "Polinomio P2 da sommare, scritto in stringa, con o senza spazi. (es. '3x^2+1' o '3x^2 + 1')"
    )


# --- SUBPARSER SOTTRAZIONE ---
    parser_sottrazione = subparsers.add_parser('sub', help="somma due polinomi P1 e P2.")

    parser_sottrazione.add_argument(
        '--p1', # argomento polinomio 1 necessario per il parser "sub"
        type = str,
        required = True,
        help = "Polinomio P1 da cui verrà sottratto p2, scritto in stringa, con o senza spazi. (es. '3x^2+1' o '3x^2 + 1')"
    )
    parser_sottrazione.add_argument(
        '--p2', # argomento polinomio 2 necessario per il parser "sub"
        type = str,
        required = True,
        help = "Polinomio P2 che verrà sottratto da p1, scritto in stringa, con o senza spazi. (es. '3x^2+1' o '3x^2 + 1')"
    )


    # --- SUBPARSER MUL (moltiplicazione) ---
    parser_mul = subparsers.add_parser('mul', help="Moltiplica P1 e P2.")
    parser_mul.add_argument(
        '--p1',
        type = str,
        required = True,
        help = "Polinomio P1 (es. '3x+1')."
    )
    parser_mul.add_argument(
        '--p2',
        type = str,
        required = True,
        help = "Polinomio P2 (es. 'x-1')."
    )

    # --- SUBPARSER MUL_SCALAR ---
    parser_mul_scalar = subparsers.add_parser('mul_scalar', help="Moltiplica un polinomio per uno scalare.")
    parser_mul_scalar.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio P (es. '3x+1')."
    )
    parser_mul_scalar.add_argument(
        '--s',
        type = float,
        required = True,
        help = "Scalare (numero) per cui moltiplicare."
    )

    # --- SUBPARSER DIV (divisione) ---
    parser_div = subparsers.add_parser('div', help="Divide P1 per P2 (Quoziente e Resto).")
    parser_div.add_argument(
        '--p1',
        type = str,
        required = True,
        help = "Dividendo P1 (es. 'x^2-1')."
    )
    parser_div.add_argument(
        '--p2',
        type = str,
        required = True,
        help = "Divisore P2 (es. 'x-1')."
    )

    # --- SUBPARSER DERIV (derivata) ---
    parser_deriv = subparsers.add_parser('deriv', help="Calcola la derivata di un polinomio.")
    parser_deriv.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio da derivare (es. '3x^2+1')."
    )

    # --- SUBPARSER INTEG (integrale) ---
    parser_integ = subparsers.add_parser('integ', help="Calcola l'integrale indefinito di un polinomio.")
    parser_integ.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio da integrare (es. '2x')."
    )
    parser_integ.add_argument(
        '--c',
        type = float,
        default = 0.0,
        required = False,
        help = "Costante di integrazione (default: 0.0)."
    )

    # --- SUBPARSER INTEG_DEF (integrale definito) ---
    parser_integ_def = subparsers.add_parser('integ_def', help="Calcola l'integrale definito (area).")
    parser_integ_def.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio da integrare (es. '2x')."
    )
    parser_integ_def.add_argument(
        '--x1',
        type = float,
        required = True,
        help = "Estremo inferiore di integrazione."
    )
    parser_integ_def.add_argument(
        '--x2',
        type = float,
        required = True,
        help = "Estremo superiore di integrazione."
    )

    # --- SUBPARSER ROOTS (trova radici) ---
    parser_roots = subparsers.add_parser('roots', help="Trova le radici (solo per grado 2).")
    parser_roots.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio di grado 2 (es. 'x^2-1')."
    )

    # --- SUBPARSER GRADE (get_grado) ---
    parser_grade = subparsers.add_parser('grade', help="Mostra il grado del polinomio.")
    parser_grade.add_argument(
        '--p',
        type = str,
        required = True,
        help = "Polinomio (es. '3x^2+1')."
    )

    args = parser.parse_args()


    # ---- IMPLEMENTAZIONE LOGICA DELLA CLI -----

    # prima di tutto devo controllare quale comando 
    # è stato chiamato, questo lo gestisco con diversi if.
    try:
        if args.command == "solve":
            p = Polinomio.from_string(args.polinomio)
            risultato = p.valuta(args.xvalue)
            print(f"Solve P for (x={args.xvalue}): {risultato}")

        elif args.command == "sum":
            p1 = Polinomio.from_string(args.p1)
            p2 = Polinomio.from_string(args.p2)
            risultato = p1.somma(p2)
            print(f"Sum [P1 + P2]: {risultato}")

        elif args.command == "sub":
            p1 = Polinomio.from_string(args.p1)
            p2 = Polinomio.from_string(args.p2)
            risultato = p1.sottrazione(p2)
            print(f"Sub [P1 - P2]: {risultato}")

        elif args.command == "mul":
            p1 = Polinomio.from_string(args.p1)
            p2 = Polinomio.from_string(args.p2)
            risultato = p1.moltiplicazione(p2)
            print(f"[P1 * P2]: {risultato}")

        elif args.command == "mul_scalar":
            p = Polinomio.from_string(args.p)
            risultato = p.moltiplicazione_per_scalare(args.s)
            print(f"[P * {args.s}]: {risultato}")

        elif args.command == "div":
            p1 = Polinomio.from_string(args.p1)
            p2 = Polinomio.from_string(args.p2)
            quoz, resto = p1.divisione(p2)
            print(f"[P1 / P2]: Q={quoz}, R={resto}")

        elif args.command == "deriv":
            p = Polinomio.from_string(args.p)
            risultato = p.derivata()
            print(f"Derivata: {risultato}")    
    
        elif args.command == "integ":
            p = Polinomio.from_string(args.p)
            risultato = p.integrale(args.c)
            print(f"Integrale: {risultato}")

        elif args.command == "integ_def":
            p = Polinomio.from_string(args.p)
            risultato = p.integrale_definito(args.x1, args.x2)
            print(f"Area da {args.x1} a {args.x2}: {risultato}")

        elif args.command == "roots":
            p = Polinomio.from_string(args.p)
            risultato = p.trova_radici()
            if not risultato:
                print("Nessuna radice reale trovata.")
            else:
                print(f"Radici: {risultato}")

        elif args.command == "grade":
            p = Polinomio.from_string(args.p)
            risultato = p.get_grado()
            print(f"Grado: {risultato}")

    except Exception as e:
        print(f"Errore: {e}")