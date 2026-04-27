class Libro:
    def __init__(self,titolo,autore,pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    
    def descrizione(self):
         return f"Il libro '{self.titolo}' è stato scritto da {self.autore} e ha {self.pagine} pagine."
        

def main():
    libro1=Libro("i promessi sposi","Manzoni","200")
    libro2=Libro("harry potter", "jk rowling", "500")
    print(libro1.descrizione())
    print(libro2.descrizione())

main()
    