class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def muovi(self,dx,dy):
        self.x+=dx
        self.y+=dy
        print("Nuova posizione=(",dx,",",dy,")")
    def distanza_da_origine(self):
        distanza=(self.x**2+self.y**2)**0.5
        return distanza
    def stampa(self):
        print("Il punto è in posizione (",self.x,",",self.y,")")
        
def main():
    punto1=Punto(4,5)    
    punto2=Punto(1,8)
    punto1.muovi(3,1)
    punto2.muovi(5,0)
    print("la distanza dall'origine è: ",punto1.distanza_da_origine())
    print("la distanza dall'origine è: ",punto2.distanza_da_origine())
    punto1.stampa()
    punto2.stampa()
    
main()