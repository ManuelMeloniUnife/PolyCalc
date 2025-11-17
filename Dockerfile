# nella documentaizone ho letto che python ha una versione 'lite' per linux... usaimo quella
FROM python:3.10-slim

# questo versione non ha di base però tkinter quindi andiamo ad installarlo noi..
# questo è ecessario perché l'immagine 'slim' è molto minimale
RUN apt-get update && apt-get install -y \
    tk \
    tcl \
    && rm -rf /var/lib/apt/lists/*

# imposto la cartella di lavoro, qui docker si chieed se esiste nella macchina virtuale, e se non esiste (quello che succede) la crea.
WORKDIR /app

# copia la mia cartella di lavoro fisica (il primo punto ) nella sua cartella app appena creata (seconod .)
COPY . .

# installa il pacchetto della cartella (quindi la livbreria polinomio e gli script per gui e cli.)
RUN pip install .

# 6. Comando di avvio CMD, Lanciamo la CLI quanod il container parte per conferma che tutto sia funzionato correttamente.
# (sarebbe stato fine lanciare la GUI, ma ho letto che richiederebbe configurazioni video complesse)
CMD ["poly_bash", "--help"]