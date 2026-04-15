x=int(input("Dammi un valore superiore a 10->"))#inserimento valore iniziale
if x>10:#prima verifica 
    print("bravo, ora dammi un numero superiore a 50->")#risultato
    x=int(input(""))#inserimento
    if x>50:#seconda verifica
        print("bravissiomo, ora dammene uno superiore a 1000->")
        x=int(input(""))
        if x>1000:#terza verifica
            print("Complimenti, hai vinto!!!")
        else:
            print("Oh no, hai perso")#else terzo if
    else:
        print("Oh no, hai perso")#else secondo if
else:
    print("Oh no, hai perso")#else primo if
            
print("-----------------------")
#esercizio 2
sel=input("Seleziona l'azione da svolgere tra Aggiungere,Modificare e Rimuovere-->")#inserimento comando da svolgere
if sel=="Aggiungere":
    print("Perfetto, puoi aggiungere")
elif sel=="Modificare":
    print("Perfetto, puoi modificare")
elif sel=="Rimuovere":
    print("Perfetto, puoi rimuovere")
else : #qualsiasi altro comando digitato risulta invalido
    print("comando non valido")
    
print("-----------------------")

#esercizio 3
i=0
v=input("Nuovo utente?")
v2=input("hai già la password?")
if v2=="si":
    print("Inserire il nome utente:")
    password=input("Inserire password:")
    i=i+1

