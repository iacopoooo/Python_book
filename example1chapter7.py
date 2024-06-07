
import tkinter as tk

def mostra_risposta():
    # Recupera il testo dall'entry widget e aggiorna l'etichetta
    risposta = entry.get()
    label.config(text=f"Hai scritto: {risposta}")

# Crea la finestra principale
root = tk.Tk()
root.title("Input dell'Utente")

# Crea un widget di entry
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# Crea un pulsante che quando cliccato eseguirà la funzione 'mostra_risposta'
button = tk.Button(root, text="Invia", command=mostra_risposta)
button.pack(pady=10)

# Crea un'etichetta per mostrare la risposta
label = tk.Label(root, text="")
label.pack(pady=20)

# Avvia il ciclo principale dell'evento
root.mainloop()
