class Animale:
    def __init__(self,nome,eta):
        self.nome = nome
        self.eta = eta
    def fai_suono(self):
        print(self.nome," emette un suono generico.")

class Leone(Animale):
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
    def fai_suono(self):
        print(self.nome," sta ruggendo")
    def caccia(self):
        print(self.nome," sta cacciando una preda")

class Mucca(Animale):
    def __init__(self,nome,eta):
        super().__init__(nome, eta)
    def fai_suono(self):
        print("La mucca ",self.nome," sta muggendo")
    def pascola(self):
        print(self.nome," sta pascolando e mangiando")

class Cane(Animale):
    def __init__(self,nome,eta):
        super().__init__(nome, eta)
    def fai_suono(self):
        print("Il cane",self.nome, "sta abbaiando")
    def scodinzola(self):
        print(self.nome," sta scodinzolando felice")

animale1 = Leone("Simba", 6)
animale2 = Mucca("Carolina", 4)
animale3 = Cane("Bobby", 2)
animale1.fai_suono()
animale1.caccia()
animale2.fai_suono()
animale2.pascola()
animale3.fai_suono()
animale3.scodinzola()