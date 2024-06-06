

#in un altro file scrivete questo codice

import modulo_lista # importo il modulo creato prima

# Esempio di lista
numeri = [1, 2, 3, 4, 5]

# Trova il valore minimo
minimo = modulo_lista.trova_minimo(numeri)
print(f"Il valore minimo nella lista è: {minimo}")

# Trova il valore massimo
massimo = modulo_lista.trova_massimo(numeri)
print(f"Il valore massimo nella lista è: {massimo}")

# Calcola la media
media = modulo_lista.calcola_media(numeri)
print(f"La media della lista è: {media}")
