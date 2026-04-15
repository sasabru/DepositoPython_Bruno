#esercizio 1
controllo=True
while controllo:
    x=int(input("Inserisci un numero: "))
    while x<0:
        x=int(input("Reinserisci un numero: "))
    for i in range(x,-1,-1):
        print(i)
    scelta=input("Vuoi continuare? ")
    if scelta=="no":
        controllo=False

#esercizio 2
contatore=0 #contatore numeri primi
while contatore!=5:
    a=int(input("Dammi un numero: "))
    f=0
    for z in range(a-1,1,-1):#for che scorre i numere dal precedente al nostro fino al 2
        if a%z!=0:#controllo del resto 
            f+=1
    if f==0: #se f è uguale a 0 significa che è primo
        contatore+=1
    print("Contatore:",contatore)
    
    