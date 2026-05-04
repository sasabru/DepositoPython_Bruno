class AnalizzatoreVendite:
    def __init__(self,dati):
        self._dati=dati
    
    def elabora(self):
        if len(self._dati)==0:
            return None
        totale= sum(self._dati)
        media= totale/len(self._dati)
        
        sopra_media=[]
        for valore in self._dati:
            if valore>media: 
                sopra_media.append(valore)
                
        return {
                "totale":totale,
                "media":media,
                "sopra_media": sopra_media
            }