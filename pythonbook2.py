# abbiamo dichiarato le variabili
nome = "Mario"
eta = 30
altezza = 1.75
italiano = True

# Condizioni
print("condizioni:")
if eta > 18:
    print("Sei maggiorenne")
else:
    print("Non sei maggiorenne")

# Cicli
print ("\nciclo for:")
for i in range(5):
    print(i)
j = 0

print("\nciclo while:")
while j < 5:
    print(j)
    j += 1

#Funzione
print ("\nfunzione:")
def saluta(nome):
    return "Ciao " + nome + "!"
print(saluta("Mario"))

