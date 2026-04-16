import random
z=input("Che punto dell'esercizio vuoi fare? (da 1 a 7) ")
def funzione1():
    c=True
    while c:
        x=int(input("Dammi un numero positivo: "))
        if x>0:
            c=False
    print("Il numero inserito è positivo")
    return x

def funzione2():
    n=int(input("Dammi la lunghezza della lista: "))
    lista=[]
    for i in range(0,n,1):
        lista.append(random.randint(1,n))
    return lista
    
def funzione3(x):
    print(x)
    contatore=0
    sommatore=0
    for i in x:
        if i%2==0:
            sommatore+=i
            contatore+=1
    print("Ci sono",contatore,"numeri pari e la somma è",sommatore)
    
def funzione4(x):
    print(x)
    for i in x:
        if i%2!=0:
            print(i," è un numero dispari")
    
    
def funzione5(x):
    
    controllore=True
    if x==1:
        print(x,"è primo")
    else:
        for i in range(2,x-1,1):
            if (x%i)==0:#controllo del resto, se è diverso da 0 allora non è primo
                controllore=False
        if controllore==True:
            print(x,"è primo")
        else:
            print(x,"non è primo")
            
        
            

def funzione6(x):
    print(x)
    for i in x:
        funzione5(i)
        
def funzione7(x):
    sommatore=0
    for i in x:
        sommatore+=i
    funzione5(sommatore)
    
    













match z:
    case "1":
        funzione1()
    case "2":
        print(funzione2())
    case "3":
        lista=funzione2()
        funzione3(lista)
        
    case "4":
        lista=funzione2()
        funzione4(lista)
    case "5":
        x=funzione1()
        funzione5(x)
    case "6":
        lista=funzione2()
        funzione6(lista)
    case "7":
        lista=funzione2()
        funzione7(lista)
    case _:
        pass
