class Studente:
    def __init__(self, nome):
        self.nome = nome
        
class Professore:
    def __init__(self, nome_prof):
        self.nome_prof = nome_prof
    def crea_aula(self, nome_aula, lista_studenti):
        nome_file = f"aula_{nome_aula}.txt"
        print("CREAZIONE AULA")
        with open(nome_file, "w") as f:
            f.write(f"Nome aula: {nome_aula} \n")
            f.write(f"Nome professore: {self.nome_prof}\n")
            f.write("Elenco studenti:\n")
            for studente in lista_studenti:
                f.write(f"-{studente}\n")
        print("File della classe generato con successo")   

nome_utente= input("Inserisci il nome utente: ")
scelta= input("Sei un professore o uno studente: ") #"studente" o "professore"
if scelta=="studente":
    utente=Studente(nome_utente)
    print("Benvenuto ",nome_utente)
elif scelta=="professore":
    utente=Professore(nome_utente)
    print("Benvenuto prof. ",nome_utente)
    while True:
            print("Menù professore:")
            azione=input("Cosa desideri fare?(creaaula/esci): ")
            if azione=="esci":
                print("Arrivederci prof")
                break
            elif azione=="creaaula":
                n_aula=input("Inserisci il nome dell'aula: ")
                lista_s=[]
                n_s=""
                while n_s!="0":
                    n_s=input("Inserisci il nome dello studente (digita 0 per terminare): ")
                    if n_s!="0":
                        lista_s.append(n_s)
                if lista_s:
                    utente.crea_aula(n_aula,lista_s)
                else:
                    print("Impossibile creare un'aula vuota")
            else:
                print("Comando non riconosciuto")
else:
    print("Ruolo non riconosciuto")