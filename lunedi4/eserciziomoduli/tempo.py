class Calendario:
    def __init__(self,giorno:4,mese=5,anno=2026):
        self.giorno=giorno
        self.mese=mese
        self.anno=anno
        
    def avanza_giorno(self):
        self.giorno+=1
        if self.giorno>30:
            self.giorno=1
            self.mese+=1
            if self.mese>12:
                self.anno+=1
    
    def __str__(self):
        return f"{self.giorno:02d}/{self.mese:02d}/{self.anno}"