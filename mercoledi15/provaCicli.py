#esempio while
i=0
while i<5:
    print(i)
    i+=1
    
#ciclo booleano
controllore=True
while controllore:
    print("ciao")
    scelta=input("Vuoi continuare?").lower()
    if scelta=="no":
        controllore=False
        
#ciclo for

numeri=[1,2,3,4,5]
for numero in numeri:
    print(numero)
    
#for con range
for i in range(0,10,2):
    print(i)
    
#break--> viene utilizzato per interrompere immediatamente un ciclo se si verifica una determinata condizione
#continue--> salta il resto del codice all'interno di un ciclo e passare alla prossima iterazione
#pass--> viene utilizzata quando non si desidera eseguire alcuna azione all'interno di un ciclo