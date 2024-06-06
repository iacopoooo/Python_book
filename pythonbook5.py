#Esempiodi funzione
def saluta(nome):
    print(f"Ciao, {nome}!")

# Chiamata della funzione
saluta("Marco")

#Funzione con più parametri
def descrivi_animale(animale, nome):
    print(f"Ho un {animale} di nome {nome}.")

# Uso della funzione con parametri
descrivi_animale("cane", "Pippo")


#Importare moduli
import math #modulo o pacchetto

# Uso di una funzione dal modulo math
print(math.sqrt(16))  # Stampa la radice quadrata di 16


# Esercizio di verifica
def count_media(lista):
    # Controlla se la lista è vuota
    if len(lista) == 0:
        """"
        La funzione len() restituisce il numero di elementi (lunghezza) in un oggetto.
        """
        return 0  # Restituisce 0 se la lista è vuota per evitare divisione per zero
    #senza questo controllo il codice produrrebbe errore

    # Calcola la somma di tutti i numeri nella lista
    somma = sum(lista)
    """"
    La funzione sum() di Python può essere utilizzata per trovare rapidamente la somma di una serie di valori numerici
    """

    # Calcola la lunghezza della lista
    tot_numbers = len(lista)

    # Calcola la media
    media = somma / tot_numbers

    return media


# Esempio di utilizzo
numeri = [1, 2, 3, 4]
media = count_media(numeri)
print(f"La media della lista è: {media}")
