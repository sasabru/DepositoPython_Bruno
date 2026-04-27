class Posto:
    def __init__(self,numero,fila):
        self._numero=numero
        self._fila=fila
        self._occupato=False
    def prenota(self):
        if not self._occupato:
            self._occupato=True
            return True
        return False
    def libera(self):
        if self._occupato:
            self._occupato=False
            return True
        return False
    
    @property
    def numero(self): return self._numero
    @property
    def fila(self): return self._fila    
    @property
    def occupato(self): return self._occupato

class PostoVip(Posto):
    def __init__(self,numero,fila,servizi_extra):
        super().__init__(numero,fila)
        self.servizi_extra=servizi_extra
    def prenota(self):
        if super().prenota():
            servizi_testo = ", ".join(self.servizi_extra)
            print("Servizi vip attivati:", servizi_testo)
            return True
        return False

class PostoStandard(Posto):
    def __init__(self,numero,fila,costo):
        super().__init__(numero,fila)
        self.costo=costo
    def prenota(self):
        if super().prenota():
            print("Costo prenotazione standard:", self.costo)
            return True
        return False    

class Teatro:
    def __init__(self):
        self._posti=[]
    def aggiungi_posto(self,posto):
        self._posti.append(posto)
    def prenota_posto(self,numero,fila):
        fila=fila.upper()
        for p in self._posti:
            if p.numero==numero and p.fila.upper()==fila:
                if p.prenota():
                    print("Posto prenotato")
                else:
                    print("Posto già occupato")
                return
        print("Posto non esistente")
    def stampa_posti_occupati(self):
        print("Posti occupati:")
        occupati= [p for p in self._posti if p.occupato]
        if not occupati:
            print("Nessun posto occupato")
        else:
            for p in occupati:
                if isinstance(p, PostoVip):
                    tipo="Vip"
                else:
                    tipo="Standard"
                print(tipo," Fila:",p.fila,"  Numero:",p.numero )
                
                
teatro=Teatro()
teatro.aggiungi_posto(PostoStandard(1, "A", 10.0))
teatro.aggiungi_posto(PostoStandard(2, "A", 10.0))
teatro.aggiungi_posto(PostoStandard(1, "C", 15.0))
teatro.aggiungi_posto(PostoStandard(2, "C", 15.0))
teatro.aggiungi_posto(PostoStandard(3, "C", 15.0))
teatro.aggiungi_posto(PostoStandard(4, "C", 15.0))
teatro.aggiungi_posto(PostoStandard(5, "C", 15.0))
teatro.aggiungi_posto(PostoVip(1, "B", ["Drink omaggio"]))
teatro.aggiungi_posto(PostoVip(2, "B", ["Servizio al posto", "Cuscino Extra"]))
teatro.aggiungi_posto(PostoVip(1, "D", ["Calice di spumante", "Programma di sala"]))
teatro.aggiungi_posto(PostoVip(2, "D", ["Calice di spumante", "Programma di sala"]))
teatro.aggiungi_posto(PostoVip(3, "D", ["Aperitivo buffet", "Accesso prioritario"]))

while True:
    print("OPERAZIONI DISPONIBILI:")
    print("1. Prenota un posto")
    print("2. Visualizza posti occupati")
    print("3. Esci ")
    comando = input("Cosa desideri fare? ")
    if comando == "3":
        print("Arrivederci!")
        break
    elif comando == "2":
        teatro.stampa_posti_occupati()
    elif comando == "1":
        f = input("Inserisci la fila: ")
        n_input = int(input("Inserisci il numero del posto: "))
        teatro.prenota_posto(n_input,f)
        
    else:
        print("Comando non riconosciuto")