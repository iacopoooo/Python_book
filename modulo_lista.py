

# Esercizio 2
# crea il seguente file e nominalo modulo_lista.py
def trova_minimo(lista):
    """Restituisce il valore minimo nella lista."""
    if not lista: #questo è un altro modo per verificare che la lista non sia vuota
        return None  # Restituisce None se la lista è vuota
    minimo = lista[0]
    for numero in lista:
        if numero < minimo:
            minimo = numero
    return minimo

def trova_massimo(lista):
    """Restituisce il valore massimo nella lista."""
    if not lista:
        return None  # Restituisce None se la lista è vuota
    massimo = lista[0]
    for numero in lista:
        if numero > massimo:
            massimo = numero
    return massimo

def calcola_media(lista):
    """Restituisce la media dei valori nella lista."""
    if not lista:
        return 0  # Restituisce 0 se la lista è vuota per evitare divisione per zero
    somma = sum(lista)
    contatore = 0
    for _ in lista:
        contatore += 1
    media = somma / contatore
    return media
