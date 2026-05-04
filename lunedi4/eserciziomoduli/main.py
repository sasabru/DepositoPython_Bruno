from tempo import Calendario
from analisi import AnalizzatoreVendite
from gestione_dati import Gestore

def avvia_sistema():
    mio_calendario=Calendario()
    mio_gestore=Gestore("report_finale.txt")
    print("Avvio sistema")
    while True:
        data_corrente=str(mio_calendario)
        print("Giorno attuale: ",data_corrente)
        importi=mio_gestore.acquisisci_importi()
        motore=AnalizzatoreVendite(importi)
        risultati=motore.elabora()
        if risultati!=None:
            print("Totale:",risultati["totale"])
            print("Media:",risultati["media"])
            lista_sopra=risultati["sopra_media"]
            if len(lista_sopra)==0:
                testo_sopra="Nessun valore sopra la media"
            else:
                testo_sopra=str(lista_sopra)
            print("Risultato sopra media:", testo_sopra)
            riga=data_corrente+" - Totale: "+str(risultati["totale"])+" - Media: "+ str(risultati["media"])+" - Sopra Media: " + testo_sopra
            mio_gestore.scrivi_su_file(riga)
        scelta=input("Vuoi passare al giorno successivo? (s/n): ")
        if scelta=="s":
            mio_calendario.avanza_giorno()
        else:
            print("Analisi completa ")
            break
avvia_sistema()