def login():
    controllo=False
    while controllo!=True:
        utente=input("Inserisci il nome utente: ")
        password=input("Inserisci la password: ")
        for i in range(len(listaUtenti)):
            #print(utente,listaUtenti[i])
            if utente==listaUtenti[i] and password==listaPassword[i]:
                controllo=True
                break
        if controllo!=True:                    
            print("Nome utente o password errati, inserire di nuovo:")
    print("Accesso effettuato")

def somma(*args):
    sommatore=0
    for i in args:
        sommatore+= i
    return sommatore
def sottrazione(*args):
    risultato=args[0]
    for i in range(1,len(args),1):
        risultato-=args[i]
    return risultato
def moltiplicazione(*args):
    risultato=args[0]
    for i in range(1,len(args),1):
        risultato=risultato*args[i]
    return risultato
def divisione(x,y):
    if y!=0:
        risultato=x/y
        return risultato
    else :
        print("errore")

    
def potenza(x,y):
    risultato=x**y
    return risultato
    
def inserimentoVal():
    n=int(input("quanti numeri vuoi sommare? "))
    v=[n]
    for i in range(n):
        v.append(int(input("Numero: ")))
    return v
    

listaUtenti=["salvatore","lalala"]
listaPassword=["1234","5678"]
domanda_accesso=input("Ciao hai già un account?")#con "si" fa fare il login mentre con no fa creare un nuovo account
if domanda_accesso=="si":
    login()

elif domanda_accesso=="no":
    while True:
        nuovoUtente=input("Crea un nome utente: ")
        if nuovoUtente in listaUtenti:
            print("nome utente non disponibile, scegli un altro nome utente ")
        else:
            nuovaPassoword=input("Crea una password: ")
            listaUtenti.append(nuovoUtente)
            listaPassword.append(nuovaPassoword)
            print("Creazione account confermata, si prega di effettuare l'accesso ")
            break
    login()
    
operazioniSvolte=0
listaRisultati=[]
listaValori=[]
while operazioniSvolte<4:
    scelta=input("Scegli cosa fare (operazioni/stampa)")
    if scelta=="operazioni":
        scelta=input("Scegli l'operazione da fare (add,sot,mol,div,pot)")
        match scelta:
            case "add":
                valori=inserimentoVal()   
                listaRisultati.append(somma(*valori))
                listaValori.append(*valori)
                operazioniSvolte+=1             
            case "sot":
                valori=inserimentoVal()
                listaRisultati.append(sottrazione(*valori))
                listaValori.append(*valori)
                operazioniSvolte+=1             

            case "mol":
                valori=inserimentoVal()
                listaRisultati.append(moltiplicazione(*valori))
                listaValori.append(*valori)
                operazioniSvolte+=1
                
                
            case "div":
                valori=inserimentoVal()
                if len(valori)>2:
                    print("Errore")
                else:
                    listaRisultati.append(divisione(valori[0],valori[1]))
                    operazioniSvolte+=1
                for i in range(len(valori)):
                        listaValori.append(valori[i])
                    
            case "pot":
                valori=inserimentoVal()
                if len(valori)>2:
                    print("Errore")
                else:
                    listaRisultati.append(potenza(valori[0],valori[1]))
                    for i in range(len(valori)):
                        listaValori.append(valori[i])
                    operazioniSvolte+=1
    if scelta=="stampa":
        print("Lista valori: ",listaValori)
        print("Lista risultati: ",listaRisultati)
        operazioniSvolte+=1

        
print("rieffettuare accesso")
login()                
                    

                
            
        
        
    







