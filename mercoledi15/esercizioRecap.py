x=int(input("Inserisci un numero: "))
while x<=0:
    x=int(input("Renserisci un numero positivo: "))
sommaPari=0
f=0
for i in range(1,x+1,1):
    if (i%2)==0:
        sommaPari+=i
    else:
        print("Numero dispari -> ",i)
print("La somma dei numeri pari è ",sommaPari)

for i in range(1,x,1):
    if (x%i)==0:#controllo del resto 
        f+=1
if x==1:
    print("Il numero ",x," è primo")
else:
    if f==1: #se f è uguale a 0 significa che è primo
        print("Il numero ",x," è primo")
    else:
        print("Il numero ",x," non è primo")
