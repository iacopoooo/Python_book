def dividi_numeri():
    try:
        num1 = input("Inserisci il primo numero: ")
        num2 = input("Inserisci il secondo numero: ")

        # Controllo se l'input non è un numero intero
        if not num1.isdigit() or not num2.isdigit():
            raise Exception("Input non valido, puoi inserire solo numeri interi e non lettere o caratteri speciali.")

        num1 = int(num1)
        num2 = int(num2)

        risultato = num1 / num2
        print(f"Il risultato della divisione è: {risultato}")
    except Exception as e:
        print(f"Errore: {e}")
    finally:
        print("Operazione tentata di divisione.")


# Chiamata alla funzione per testare la gestione delle eccezioni
dividi_numeri()
