class Gestore:
    def __init__(self,nome_file="report_vendite.txt"):
        self.nome_file=nome_file
        
    def acquisisci_importi(self):
        while True:
            ingresso=input("inserisci gli importi separati da spazio: ").strip()
            parti=ingresso.split()
            if len(parti)==0:
                print("Dati mancanti")
                continue
            valido=True
            for p in parti:
                if p.isdigit()==False:
                    valido=False
            if valido==True:
                lista_numeri=[]
                for x in parti:
                    lista_numeri.append(int(x))
                return lista_numeri
            else:
                print("Valore errato. Lista azzerata")
                
    def scrivi_su_file(self,messaggio):
        with open(self.nome_file, "a") as f:
            f.write(messaggio+"\n")
                