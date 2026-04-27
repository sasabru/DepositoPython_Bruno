class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
    def muovi(self):
        print(f"{self.nome} è in movimento")
    def attacca(self):
        print(f"{self.nome} sta attaccando")
    def ritira(self):
        print(f"{self.nome} effettua un ritiro strategico")
    def __str__(self):
        return f"Unità {self.nome} ({self.numero_soldati} soldati)"
    def __repr__(self):
        return f"UnitaMilitare('{self.nome}', {self.numero_soldati})"
    def __len__(self):
        return self.numero_soldati
    def __eq__(self, altro):
        if isinstance(altro, UnitaMilitare):
            return self.numero_soldati == altro.numero_soldati
        return False
    def __getattribute__(self, nome_attr):
        return super().__getattribute__(nome_attr)
    

class Fanteria(UnitaMilitare):
    def costruisci_trincea(self):
        print(f"{self.nome} sta costruendo trincee")

class Artiglieria(UnitaMilitare):
    def calibra_artiglieria(self):
        print(f"{self.nome} sta calibrando i pezzi di artiglieria")

class Cavalleria(UnitaMilitare):
    def esplora_terreno(self):
        print(f"{self.nome} sta esplorando il terreno")

class SupportoLogistico(UnitaMilitare):
    def rifornisci_unita(self):
        print(f"{self.nome} sta effettuando i rifornimenti")

class Ricognizione(UnitaMilitare):
    def conduci_ricognizione(self):
        print(f"{self.nome} è in missione di ricognizione")

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self, nome_comando):
        UnitaMilitare.__init__(self, nome_comando, 0)
        self.unita_registrate = {}
    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Registrata: {unita.nome}")
    def mostra_unita(self):
        print("-Elenco Unità Registrate")
        for nome in self.unita_registrate:
            print(self.unita_registrate[nome])
    def dettagli_unita(self, nome):
        if nome in self.unita_registrate:
            unita = self.unita_registrate[nome]
            print(f"Dettagli per {nome}:")
            print(f"  Info: {unita}") 
            print(f"  Debug: {repr(unita)}") 
        else:
            print(f"Errore: Unità '{nome}' non trovata.")

u1 = Fanteria("Prima divisione", 500)
u2 = Artiglieria("Prima brigata", 500)
comando = ControlloMilitare("QG")
print(u1)               
print(len(u1))         
print(u1 == u2)        

comando.registra_unita(u1)
comando.registra_unita(u2)
comando.mostra_unita()
comando.costruisci_trincea()
comando.calibra_artiglieria()
comando.dettagli_unita("Seconda divisione")
comando.dettagli_unita("Prima divisione")
