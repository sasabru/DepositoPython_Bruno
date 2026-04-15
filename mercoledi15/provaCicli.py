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