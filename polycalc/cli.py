import argparse
from .polinomio import Polinomio # imprta la classe polinomio.

def start_bash_app():
    parser = argparse.ArgumentParser(description="PolyCalc CLI")

    # qui dico ad argparse che voglio usare sub-commands
    # dest=".." salva quale sub commands sto chiamando quindi la seguente
    # è una riga generale dove viene "appoggiato" il sub commands chiamato

    subparsers = parser.add_subparsers(dest="command", required = True, help="Azione principale da eseguire.")

    parser_valuta = subparsers.add_parser('valuta', help="Valuta un polinomio per un valore di x inserito.")
    parser_valuta.add_argument(
        '--polinomio', #argomento polinomio necessario per il parser "valuta"
        type = str,
        required = True,
        help = "Polinomio da valutare, scritto in stringa senza spazi. (es. '3x^2+1')"
    )

    parser_valuta.add_argument(
        '--xvalue', # argomento valore x necessario per il parser "valuta"
        type = float,
        required = True,
        help = "Valore di x per cui valutare il polinomio."
    )




    args = parser.parse_args()


    # ---- IMPLEMENTAZIONE LOGICA DELLA CLI -----

    # prima di tutto devo controllare quale comando 
    # è stato chiamato, questo lo gestisco con diversi if.

    if args.command == "valuta":
        p = Polinomio.from_string(args.polinomio)
        risultato = p.valuta(args.xvalue)
        print(f"Valore di P(x={args.xvalue}): {risultato}")