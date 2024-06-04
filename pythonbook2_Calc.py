
#calcolatrice
def calcolatrice():

    num1 = float(input("Inserisci il primo numero: "))

    num2 = float(input("Inserisci il secondo numero: "))

    operazione = input("Scegli l'operazione (+, -, *, /): ")

    if operazione == '+':

        return num1 + num2

    elif operazione == '-':

        return num1 - num2

    elif operazione == '*':

        return num1 * num2

    elif operazione == '/':

        if num2 != 0:

            return num1 / num2

        else:

            return "Errore: divisione per zero"

    else:

        return "Operazione non valida"

# Chiamata della funzione

risultato = calcolatrice()

print("Risultato:", risultato)
