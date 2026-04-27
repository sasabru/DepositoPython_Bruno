class Animali:
    numero_animali=0
    def __init__(self,nome, specie):
        self.nome= nome
        self.specie= specie
        Animali.numero_animali+=1
        
    @classmethod
    def quanti_animali(cls):
        print("Ci sono ",cls.numero_animali," animali")

animale1=Animali("Dumbo", "Elefante")
animale2=Animali("Nemo", "Pesce")
animale3=Animali("Bambi", "Cervo")
Animali.quanti_animali()

        
        