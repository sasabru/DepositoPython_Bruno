class ContoBancario:
    def __init__(self,titolare,saldo_iniziale=0):
        self.__titolare=None
        self.__saldo=0
        self.titolare = titolare
        if saldo_iniziale>=0:
            self.__saldo=saldo_iniziale
    @property
    def titolare(self):
        return self.__titolare
    @titolare.setter
    def titolare(self, nuovo_titolare):
        if isinstance(nuovo_titolare, str) and nuovo_titolare.strip():
            self.__titolare = nuovo_titolare
        else:
            print("Errore: Il titolare deve essere una stringa valida.")
    @property
    def saldo(self):
        return self.__saldo
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            print("Deposito di ",importo,"€ eseguito.")
        else:
            print("Errore: Importo non valido.")  
    def preleva(self, importo):
        if 0 < importo <= self.__saldo:
            self.__saldo -= importo
            print(f"Prelievo di ",importo,"€ eseguito.")
        else:
            print("Fondi insufficienti o importo non valido.")     

conto1= ContoBancario("Salvatore", 1000)
print("Titolare attuale: ",conto1.titolare)
conto1.titolare="Salvatore Bruno"
print("Titolare attuale: ",conto1.titolare)

print("Saldo attuale: ",conto1.saldo)    
conto1.deposita(-20)
conto1.deposita(200)
print("Saldo attuale: ",conto1.saldo)    
conto1.preleva(2000)
conto1.deposita(150)
print("Saldo attuale: ",conto1.saldo)    