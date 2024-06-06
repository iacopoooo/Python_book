print ("========= Esempio 1: =========")

class Automobile:
    def __new__(cls, *args, **kwargs):
        print("Chiamato __new__")
        instance = super().__new__(cls)  # Creazione dell'istanza
        return instance

    def __init__(self, marca, modello, anno):
        print("Chiamato __init__")
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        return f"{self.marca} {self.modello} del {self.anno}"

    def accendi(self):
        return f"{self.marca} {self.modello} è accesa."

# Creazione di un'istanza della classe Automobile
auto1 = Automobile("Fiat", "Punto", 2020)
#auto2 = Automobile("Tesla", "Model S", 2022)
"""se decommentassi auto2, nell'output avrei 
Chiamato __new__
Chiamato __init__
Chiamato __new__
Chiamato __init__, 
questo perchè ho due istanze auto1 e auto2"""
# Utilizzo dei metodi
print(auto1.descrizione())
print(auto1.accendi())

print("========= Fine esempio 1 ========= \n")
#per semplicità viene omesso il costruttore new
#pertanto tutti le classi python iniziano con init direttamente

print("========= Esempio 2: =========")
print("USATE QUESTO")
class Automobile:  # classe
    def __init__(self, marca, modello, anno):  # metodo
        self.marca = marca  # attributo
        self.modello = modello  # attributo
        self.anno = anno  # attributo

    def descrizione(self):  # metodo
        print(f"{self.marca} {self.modello} del {self.anno}")  # metodo
        #notare la print direttamente nel metodo

    def accendi(self):  # metodo
        return f"{self.marca} {self.modello} è accesa."  # metodo
#qui ho utilizzato return, per cui quando chiamo il metodo devo utilizzare print

# Creazione di istanze della classe Automobile
auto1 = Automobile("Fiat", "Punto", 2020)  # istanza
auto2 = Automobile("Tesla", "Model S", 2022)  # istanza

# Utilizzo dei metodi

#print è nella creazione del metodo
auto1.descrizione()  # metodo

#qui non c'era è allora devo inserire print
print(auto2.accendi())  # metodo

print("========= Fine esempio 2 =========")

"""
La maggior parte delle classi in Python rappresenta tipi mutabili (cioè, i loro attributi possono cambiare dopo la creazione dell'istanza). __init__ è perfetto per questo scopo.
__new__ è più adatto ai tipi immutabili, come le tuple, gli interi, le stringhe, ecc., dove l'oggetto deve essere completamente costruito prima che qualsiasi cosa possa essere fatta su di esso.
In altre parole nel 99% dei casi utilizzerete init
"""

#Dichiarazione di classe
class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def stampa_info(self):
        print(f"Il nome dell'animale è {self.nome} e la specie è {self.specie}.")

# Creazione di un'istanza della classe
mio_cane = Animale(nome="Fido", specie="Cane")
mio_cane.stampa_info()


# Dichiaazione di un metodo
class Animale:
    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def suona(self): # metodo
        if self.specie == "Cane":
            print("Bau bau!")
        else:
            print("Questo animale fa un altro suono.")

# Creazione di un oggetto di tipo Animale
mio_cane = Animale(nome="Fido", specie="Cane")
mio_gatto = Animale(nome="Micio", specie="Gatto")

# Chiamata del metodo suona
mio_cane.suona()  # Output: Bau bau!
mio_gatto.suona()  # Output: Questo animale fa un altro suono.


# Ereditarietà senza costruttore
class Cane(Animale):
    def set_razza(self, razza): # senza questa riga il codice produrrebbe errore
        self.razza = razza

    def stampa_info(self):
        print(f"Il nome del cane è {self.nome}, la razza è {self.razza}.")

# Creazione di un oggetto di tipo Cane e impostazione della razza
print("output senza costruttore:")
mio_cane = Cane(nome="Fido", specie="Cane")
mio_cane.set_razza("meticcio")
mio_cane.stampa_info()

# Ereditarietà
class Cane(Animale):
    def __init__(self, nome, razza):
        super().__init__(nome, "Cane")
        self.razza = razza

    def stampa_info(self):
        print(f"Il nome del cane è {self.nome}, la razza è {self.razza}.")



# Polimorfismo
class Gatto(Animale):
    def __init__(self, nome, colore):
        super().__init__(nome, "Gatto")
        self.colore = colore

    def stampa_info(self):
        print(f"Il nome del gatto è {self.nome}, il colore è {self.colore}.")




# Utilizzo di classi derivate
mio_cane = Cane(nome="Fido", razza="bassotto") # vedi ereditarietà
mio_gatto = Gatto(nome="Micio", colore="arancione")# vedi ereditarietà

# Chiamata dei metodi
mio_cane.suona()  # Output: Bau bau!
mio_gatto.suona()  # Output: Questo animale fa un altro suono.

# Polimorfismo: i metodi sovrascritti vengono chiamati
mio_cane.stampa_info()  # Output: Il nome del cane è Fido, la razza è bassotto.
mio_gatto.stampa_info()  # Output: Il nome del gatto è Micio, il colore è arancione.



# Incapsulamento
class Animale:
    def __init__(self, nome, specie):
        self.__nome = nome  # Attributo privato
        self.__specie = specie  # Attributo privato

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_specie(self):
        return self.__specie

    def set_specie(self, specie):
        self.__specie = specie

    def suona(self):  # metodo
        if self.__specie == "Cane":
            print("Bau bau!")
        else:
            print("Questo animale fa un altro suono.")

# utilizzo dell'incapsulamento
mio_cane = Animale(nome="Fido", specie="Cane")
print(mio_cane.get_nome())  # Output: Fido
mio_cane.set_nome("Pongo")
print(mio_cane.get_nome())  # Output: Buddy

mio_cane.suona()  # Output: Bau bau!


