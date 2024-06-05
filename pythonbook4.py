
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


