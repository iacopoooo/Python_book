print("Esempio con la gestione delle eccezioni:")
def dividi(numeratore, denominatore):
    try:
        risultato = numeratore / denominatore
    except ZeroDivisionError:
        print("Errore: divisione per zero.")
    except TypeError:
        print("Errore: entrambi i valori devono essere numeri.")
    else:
        print(f"Risultato: {risultato}")
    finally:
        print("Esecuzione completata.")

# Esempi di utilizzo della funzione dividi
dividi(10, 2)    # Caso senza eccezioni
dividi(10, 0)    # Caso con ZeroDivisionError
dividi(10, 'a')  # Caso con TypeError

print("\n==============================\n")

#uso senza la gestione delle eccezioni
print("Esempio senza gestire le eccezioni:")
def dividi(numeratore, denominatore):

         risultato = numeratore / denominatore
         return risultato
print(dividi(10, 2)) #cosi funziona
#print(dividi(10, 0)) # se decommentate genererà errroe
#print(dividi(10, 'a')) # se decommentate genererà errroe
