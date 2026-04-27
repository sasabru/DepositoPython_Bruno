class Convertitore:
    @staticmethod
    def euroindollari(x):
        t=1.8
        return x*t
    @staticmethod
    def kminmiglia(x):
        f=0.621371
        return x*f
    
dollari = Convertitore.euroindollari(100)
miglia = Convertitore.kminmiglia(10)
print("100 Euro corrispondono a ",dollari," dollari.")
print("10 Kilometri corrispondono a ",miglia," miglia.")
        
    