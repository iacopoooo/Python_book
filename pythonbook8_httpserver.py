import socket

# Creazione di un socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 8080))
#per connettersi allo script da un altro dispositivo, ad esempio un cellulare
#dovreste sostituire localhost, con l'indirizzo ip locale del tuo computer
#apri il terminale winddows o mac/linux e digita ipconfig (su win) e ifconfig (su unix)
#dovresti vedere qualcosa del genere 192.168.1.5 (ip locale)
s.listen(5)
print('Server HTTP in ascolto su porta 8080...')

while True:
    clientsocket, address = s.accept()
    print(f"Connessione da {address} è stata stabilita!")
    # Risposta HTTP
    response = (
        'HTTP/1.1 200 OK\r\n'
        'Content-Type: text/plain\r\n'
        'Content-Length: 57\r\n'  # Lunghezza del contenuto del messaggio
        'Connection: close\r\n'
        '\r\n'
        'Hello world!\nSei riuscito a costruire il tuo primo server in Python!'
    )
    clientsocket.sendall(response.encode('utf-8'))
    clientsocket.close()

#potresti modificare lo script per modificare il messaggio di benvenuto, mostrare un immagine o per scambiare file