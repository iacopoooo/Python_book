
import os

# Creare una nuova cartella
os.mkdir('nuova_cartella')


import os

# Verificare se una cartella esiste
if os.path.exists('nuova_cartella'):
    print("La cartella esiste")
else:
    print("La cartella non esiste")


import os

# Rinominare una cartella
os.rename('nuova_cartella', 'cartella_rinominata')


import os

# Eliminare una cartella vuota
os.rmdir('cartella_rinominata')


# Creare e aprire un file per scrivere
with open('file_di_prova.txt', 'w') as file:
    file.write('Questo è un file di prova.\n')
    file.write('Scrittura di più righe.\n')


# Aprire un file per leggere
with open('file_di_prova.txt', 'r') as file:
    contenuto = file.read()
    print(contenuto)


# Aprire un file per aggiungere
with open('file_di_prova.txt', 'a') as file:
    file.write('Aggiunta di un\'altra riga.\n')


import shutil

# Copiare un file
shutil.copy('file_di_prova.txt', 'file_copiato.txt')

import os
import shutil

# Nome della cartella di destinazione
cartella_destinazione = 'cartella_destinazione'

# Verificare se la cartella di destinazione esiste e, se non esiste, crearla
if not os.path.exists(cartella_destinazione):
    os.mkdir(cartella_destinazione)

# Spostare un file
shutil.move('file_copiato.txt', 'cartella_destinazione/file_copiato.txt')


import os

# Eliminare un file
os.remove('file_di_prova.txt')


import os

# Elencare i file in una cartella
file_nella_cartella = os.listdir('.')
print(file_nella_cartella)


import os

# Creare una struttura di directory
os.makedirs('struttura/cartella1/cartella2')


import shutil

# Rimuovere una struttura di directory
shutil.rmtree('struttura')
