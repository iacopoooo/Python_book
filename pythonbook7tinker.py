
import tkinter as tk

# Crea la finestra principale
root = tk.Tk()

# Imposta il titolo della finestra
root.title("Finestra di Esempio")

# Avvia il ciclo principale dell'evento
root.mainloop()




import tkinter as tk

def saluta():
    print("Ciao mondo!")

root = tk.Tk()
root.title("Pulsante")

# Crea un pulsante e lo aggiunge alla finestra
pulsante = tk.Button(root, text="Clicca qui", command=saluta)
pulsante.pack()

root.mainloop()
