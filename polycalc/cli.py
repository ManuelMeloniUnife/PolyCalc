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

    args = parser.parse_args()


    # ---- IMPLEMENTAZIONE LOGICA DELLA CLI -----

    # prima di tutto devo controllare quale comando 
    # è stato chiamato, questo lo gestisco con diversi if.

    if args.command == "solve":
        p = Polinomio.from_string(args.polinomio)
        risultato = p.valuta(args.xvalue)
        print(f"Solve P for (x={args.xvalue}): {risultato}")

    if args.command == "sum":
        p1 = Polinomio.from_string(args.p1)
        p2 = Polinomio.from_string(args.p2)
        risultato = p1.somma(p2)
        print(f"Sum [P1 + P2]: {risultato}")

    if args.command == "sub":
        p1 = Polinomio.from_string(args.p1)
        p2 = Polinomio.from_string(args.p2)
        risultato = p1.sottrazione(p2)
        print(f"Sub [P1 - P2]: {risultato}")