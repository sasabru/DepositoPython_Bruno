import random
class MetodoPagamento:
    def __init__(self):
        self.credito = round(random.uniform(0.01, 9999.99), 2)
    def effettua_pagamento(self,x):
        print("Stai pagando: ",x)
class CartaDiCredito(MetodoPagamento):
    def effettua_pagamento(self,x):
        t=5
        totale=(t*x/100)+x
        print("Credito iniziale: ",self.credito)
        print("Stai pagando con carta di credito ",x,"€ al tasso del ",t,"%")
        if self.credito >= totale:
            self.credito -= totale
            print("Pagamento di ",totale,"€ APPROVATO. Nuovo saldo: ",self.credito,"€")
        else:
            print("Pagamento di ",totale,"€ NEGATO. Credito insufficiente (Saldo: ",self.credito,"€)")
class Paypal(MetodoPagamento):
    def effettua_pagamento(self,x):
        t=3
        totale=(t*x/100)+x
        print("Credito iniziale: ",self.credito)
        print("Stai pagando con paypal ",x,"€ al tasso del ",t,"%")
        if self.credito >= totale:
            self.credito -= totale
            print("Pagamento di ",totale,"€ APPROVATO. Nuovo saldo: ",self.credito,"€")
        else:
            print("Pagamento di ",totale,"€ NEGATO. Credito insufficiente (Saldo: ",self.credito,"€)")
class BonificoBancario(MetodoPagamento):
    def effettua_pagamento(self,x):
        t=8
        totale=(t*x/100)+x
        print("Credito iniziale: ",self.credito)
        print("Stai pagando con bonifico bancario ",x,"€ al tasso del ",t,"%")
        if self.credito >= totale:
            self.credito -= totale
            print("Pagamento di ",totale,"€ APPROVATO. Nuovo saldo: ",self.credito,"€")
        else:
            print("Pagamento di ",totale,"€ NEGATO. Credito insufficiente (Saldo: ",self.credito,"€)")
class GestorePagamenti():
    def transazione(self,metodo,x):
        metodo.effettua_pagamento(x)

importo=round(random.uniform(0.01, 9999.99),2)
metodo_scelto=input("Seleziona il metodo di pagamento (paypal/bonifico/cartadicredito):")
      
gestore=GestorePagamenti()
paypal=Paypal()
bonifico=BonificoBancario()
cartadicredito=CartaDiCredito()

if metodo_scelto=="paypal":
    metodo_da_usare=paypal
elif metodo_scelto=="bonifico":
    metodo_da_usare=bonifico
elif metodo_scelto=="cartadicredito":
    metodo_da_usare=cartadicredito
else:
    metodo_da_usare=None

if metodo_da_usare==None:
    print("Metodo di pagamento non disponibile")
else:
    gestore.transazione(metodo_da_usare,importo)