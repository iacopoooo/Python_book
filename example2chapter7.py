#provate ad inserire numeri con la virgola o lettere
#cosi vederete che il codice gestisce l'errore
def dividi_numeri():
    try:
        num1 = int(input("Inserisci il primo numero: "))
        num2 = int(input("Inserisci il secondo numero: "))
        risultato = num1 / num2
        print(f"Il risultato della divisione è: {risultato}")
    except ValueError:
        print("Errore: Per favore inserisci solo numeri interi.")
    except ZeroDivisionError:
        print("Errore: La divisione per zero non è permessa.")
    finally:
        print("Operazione tentata di divisione.")

# Chiamata alla funzione per testare la gestione delle eccezioni
dividi_numeri()






