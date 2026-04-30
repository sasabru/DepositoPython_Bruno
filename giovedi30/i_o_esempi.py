file = open("fileprova.txt","r")
contenuto = file.read() # Legge l'intero contenuto del file
riga = file.readline() # Legge solo la prima riga
print(contenuto)
print(riga)
file.close()

file = open("filenuovo.txt","w") # Apertura in modalità scrittura
file.write("Questo è un esempio di scrittura su file.")
file.close() # Chiusura del file