class Prodotto:
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Elettronica(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, garanzia):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.garanzia = garanzia

class Abbigliamento(Prodotto):
    def __init__(self, nome, costo_produzione, prezzo_vendita, materiale):
        super().__init__(nome, costo_produzione, prezzo_vendita)
        self.materiale = materiale

class Fabbrica:
    def __init__(self):
        self.inventario = {}
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
        else:
            self.inventario[prodotto] = quantita
        print(f"Aggiunti {quantita} pezzi di {prodotto.nome}")
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario and self.inventario[prodotto] >= quantita:
            self.inventario[prodotto] -= quantita
            profitto = prodotto.calcola_profitto() * quantita
            print(f"Venduti {quantita} pezzi. Profitto: {profitto}€")
        else:
            print("Scorte insufficienti")
    def resi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto] += quantita
            print(f"Resi {quantita} pezzi di {prodotto.nome}")

f = Fabbrica()
p1 = Elettronica("Laptop", 800, 1200, "2 anni")
p2 = Abbigliamento("Camicia", 10, 50, "Seta")
f.aggiungi_prodotto(p1, 5)
f.vendi_prodotto(p1, 2)
f.resi_prodotto(p1, 1)