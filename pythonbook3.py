# PRIMI SNIPPET

# Creazione di una lista
frutti = ["mela", "banana", "ciliegia"]

# Aggiunta di un elemento
frutti.append("arancia")

# Accesso a un elemento
print(frutti[2])  # stampa 'ciliegia'

# Rimozione di un elemento
frutti.remove("banana")


# Creazione di una tupla
colori = ("rosso", "verde", "blu")

# Accesso a un elemento
print(colori[1])  # stampa 'verde'

# Creazione di un dizionario
persona = {"nome": "Giovanni", "età": 30, "città": "Milano"}

# Accesso a un valore tramite chiave
print(persona["nome"])  # stampa 'Giovanni'

# Aggiunta di una nuova coppia chiave-valore
persona["professione"] = "Ingegnere"

# Creazione di un set
animali = {"gatto", "cane", "uccello"}

# Aggiunta di un elemento
animali.add("pesce")

# Verifica se un elemento è presente nel set
print("cane" in animali)  # stampa True


#==================== ESERCIZI =====================================#

#lista numero

numeri=[1,3,4,8,10]

print(numeri[1]+numeri[2]+numeri[3]+numeri[4]+numeri[0])




#script migliorato
# Lista di numeri
numeri = [1, 3, 4, 8, 10]

# Calcolo della somma degli elementi della lista
somma = sum(numeri)

# Stampa del risultato
print(somma)




#stavo diventando bravo :)

# Lista originale con duplicati
lista_con_duplicati = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 6, 7]

# Conversione della lista in un set per rimuovere i duplicati
set_senza_duplicati = set(lista_con_duplicati)

# (Opzionale) Conversione del set di nuovo in una lista
lista_senza_duplicati = list(set_senza_duplicati)

# Stampa della lista senza duplicati
print(lista_senza_duplicati)





# Creazione del set con un possibile errore di duplicazione
animali = {"gatto", "cane", "uccello", "gatto"}  # "gatto" duplicato non ha effetto

# Stampa del set originale per vedere l'effetto dei duplicati
print("Set originale:", animali)

# Rimozione di "gatto" dal set
animali.remove("gatto")

# Stampa del set dopo la rimozione
print("Set dopo la rimozione di 'gatto':", animali)




# Tupla per immagazzinare i giorni della settimana
week_days = ("lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica")

# Stampa dei giorni della settimana
for day in week_days:
    print(day)
    #day l'avrei potuta chimare giorni o Marcello; è il nome della variabile che deve stampare la tupla
    #la tupla è immutabile,che significa che i dati non possono essere modificati una volta creati.
    #day stampa ad ogni iterazione del ciclo,  il valore del prossimo elemento della tupla giorni_della_settimana.





# Dizionario per immagazzinare i contatti
contacts = {
    "Joe": "348/4455667",
    "Phil": "329/7788999",
    "Attilio": "345/12345672",
    "Clarissa": "333/9988111"
}

# Stampa dei contatti
for name, phone in contacts.items():
    print(f"Nome: {name}, Numero di telefono: {phone}")
