comando = input("Inserisci comando: ")
match comando:
    case "start":
        print("Avvio programma")
    case "stop":
        print("Chiusura programma")
    case "pausa":
        print("Programma in pausa")
    case _:
        print("Comando non riconosciuto")
        
        
#esercizio 1
eta=int(input("Quanti anni hai? "))
if eta<18:
    print("Mi dispiace, non puoi vedere questo film")
else: 
    print("Puoi vedere questo film")
    
#esercizio 2

x=int(input("Dammi il primo numero: "))
y=int(input("Dammi il secondo numero: "))
operazione=input("Scegli l'operazione da svolgere: ")
match operazione:
    case "addizione":
        print(x+y)
    case "sottrazione":
        print(x-y)
    case "moltiplicazione":
        print(x*y)
    case "divisione":
        if y!=0:
            print(x/y)
        else:
            print("Errore: divisione per zero")
            
    case _:
        print("Operazione non valida")
