class Persona:
    def __init__(self,nome,eta):
        self.__nome=nome
        self.__eta=eta
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valore):
        self.__nome=valore
    @property
    def eta(self):
        return self.__eta
    @eta.setter
    def nome(self, valore):
        if valore>0:
            self.__nome=valore
    def presentazione(self):
        print("Ciao sono ", self.__nome, "e ho ",self.__eta," anni")
    
class Studente(Persona):
    def __init__(self, nome, eta,voti):
        super().__init__(nome, eta)
        self.voti= voti
    def calcola_media(self):
        if sum(self.voti)>0:
            return sum(self.voti)/len(self.voti)
        else:
            return print("Errore")
    def presentazione(self):
        media=self.calcola_media()
        print("Studente: ",self.nome,", Età: ",self.eta,", Media Voti: ",media)
        
class Professore(Persona):
    def __init__(self, nome, eta,materia):
        super().__init__(nome, eta)
        self.materia= materia
    def presentazione(self):
        print("Professore: ",self.nome,", Età: ",self.eta,", Insegna: ",self.materia)
        
persona1=Studente("Salvatore",26, [20,30,26]) 
persona2=Professore("Aldo",40, "informatica")
persona1.presentazione()
persona2.presentazione()