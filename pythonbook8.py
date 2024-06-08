#inizio capitolo 8

#Thread

import threading

def stampa_numeri():
    for i in range(1, 6):
        print(i)

# Creazione di due thread che eseguono la stessa funzione
t1 = threading.Thread(target=stampa_numeri)
t2 = threading.Thread(target=stampa_numeri)

t1.start()
t2.start()

t1.join()
t2.join()







#Sqlite3

import sqlite3

# Connessione al database SQLite
conn = sqlite3.connect('esempio.db')
c = conn.cursor()

# Creazione di una tabella
c.execute('''CREATE TABLE if not exists inventario (id INTEGER PRIMARY KEY, nome TEXT, quantità INTEGER)''')

# Inserimento di dati
c.execute("INSERT INTO inventario (nome, quantità) VALUES ('penna', 100)")

# Interrogazione del database
c.execute('SELECT * FROM inventario')
print(c.fetchall())

conn.commit()
conn.close()



#Server

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 12345))
s.listen(5)
print('Server in ascolto...')

while True:
    clientsocket, address = s.accept()
    print(f"Connessione da {address} è stata stabilita!")
    clientsocket.send(bytes("Benvenuto al server!", "utf-8"))
    clientsocket.close()

