import copy
import dataclasses
import operator

from dataclasses import dataclass, field
from database.voti_dao import VotiDao

@dataclass(order=True)      ## crea i metodi di confronto, che altrimenti non sono creati di default
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str = field(compare=False)

    def str_punteggio(self):
        """
        Costriusce la stringa che rappresenta in forma leggibile il punteggio
        tenendo conto della possibilità di lode
        :return: "30 e lode" oppure il punteggio (senza lode) sotto forma di stringa
        """
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"
        ## NOOO return self.punteggio

    def copy(self):
        return (Voto(self.esame, self.cfu, self.punteggio, self.lode, self.data))

    def __str__(self):
        return f"{self.esame} ({self.cfu} CFU: voto {self.str_punteggio()} il {self.data})"



class Libretto:
    def __init__(self):
        self._voti = []
        self._voti_dao = VotiDao()


    @property
    def voti(self):
        return self._voti
    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
            self._voti_dao.add_voti(voto)
        else:
            raise ValueError("Voto non valido")


    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

    def findByPunteggio(self, punteggio, lode):
        """
        Seleziona tutti e soli voti che hanno un punteggio definito.
        :param punteggio: numero intero che rappresenta il punteggio
        :param lode: booleano che indica la presenza della lode
        :return: lista di oggetti di tipo voto che hanno il punteggio specificato (può anche essere vuota)
        """
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi        ## lista di stringhe (nomi dei corsi)

    def findByEsame(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: stringa, nome dell'esame da ricercare
        :return: oggetto di tipo voto corrispondente al nome cercato (se trovato) oppure None
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        return None         ## non serve ma si vede
    def findByEsame2(self, esame):
        """
        Cerca il voto a partire dal nome dell'esame
        :param esame: stringa, nome dell'esame da ricercare
        :return: oggetto di tipo voto corrispondente al nome cercato (se trovato) oppure
        un'eccezione ValueError se l'elemento non viene trovato
        """
        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")

    def has_voto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome e lo stesso punteggio
        :param voto: oggetto voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def has_conflitto(self, voto):
        """
        Ricerca se nel libretto esiste già un esame con lo stesso nome ma punteggio diverso
        :param voto: oggetto voto da confrontare
        :return: True se esiste, False se non esiste
        """
        for v in self._voti:
            if v.esame == voto.esame and not(v.punteggio == voto.punteggio and v.lode == voto.lode) :
        ##    if v.esame == voto.esame and (v.punteggio != voto.punteggio or v.lode != voto.lode)
                return True
        return False

    def copy(self):
        nuovo = Libretto()
        for v in self._voti:
            nuovo._voti.append(v.copy())  ## inserisco un nuovo voto, con gli stessi attributi
        return nuovo
    def crea_migliorato(self):
        """
        Crea una copia del libretto e migliora i voti in esso presenti
        :return:
        """
        nuovo = Libretto()
        ## nuovo._voti = self._voti.copy()
        ## oppure nuovo._voti = self._voti[:]
        for v in self._voti:
            nuovo._voti.append(v.copy())       ## inserisco un nuovo voto, con gli stessi attributi
        for v in nuovo._voti:
            if 18 <= v.punteggio <= 23:
                v.punteggio += 1
            elif 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio == 29:
                v.punteggio = 30
        return nuovo

    def crea_ordinato_per_esame(self):
        nuovo = self.copy()
        ## ordina i nuovo._voti()

        nuovo.ordina_per_esame()
        return nuovo
    def crea_ordinato_per_punteggio(self):
        nuovo = self.copy()
        nuovo.ordina_per_punteggio()
        return nuovo

    def ordina_per_esame(self):
        ## ordina self.-voti per nome esame
        ##self._voti.sort(key = estrai_campo_esame)
        ##self._voti.sort(key=operator.attrgetter("esame"))           ## la chiave è il campo esame, attrgetter() estrae l'attributo di un oggetto
        self._voti.sort(key= lambda v: v.esame)                     ## lambda argomento: valore di ritorno

    def ordina_per_punteggio(self):
        self._voti.sort(key=lambda  v: (v.punteggio, v.lode), reverse=True)             ## True è maggiore di False
    def stampa(self):
        print(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            print(v)
        print(f"La media vale {self.media():.2f}")          ## solo due cifre decimali

    def stampaGUI(self):
        outlList = []
        """
        outlList.append(f"Hai {len(self._voti)} voti")
        for v in self._voti:
            outlList.append(v)
        outlList.append(f"La media vale {self.media():.2f}")
        """
        voti = self._voti_dao.get_voti()
        for v in voti:
            outlList.append(v)

        return outlList


    def cancella_voti_inferiori(self, punteggio):
        """voti_nuovi = []
            for v in self._voti:
            if v.punteggio >= punteggio:
                voti_nuovi.append(v)          ## remove chiede l'oggetto, pop l'indice      """
        voti_nuovi = [ v for v in self._voti if v.punteggio >= punteggio ]
        self._voti = voti_nuovi

        """
        Opzione 1:
        metodo stampa_per_nome e metodo stampa_per_punteggio, che semplicemente stampano e non modificano nulla
        
        Opzione 2:
        metodo crea_libretto_ordinato_per_nome e metodo crea_libretto_ordinato_per_punteggio, che creano
        delle copie separate sulle quali potrò chiamare il metodo stampa()
        
        Opzione 3:
        metodo ordina_per_nome, che modifica il libretto stesso riordinando i voti, e ordina_per_punteggio, poi userò stampa()
        + aggiungiamo gratis un metodo copy()
        
        Opzione 2bis:
        crea una copia shallow del libretto
        """

    def stampa_ordineAlfabeticoEsame(self):
        ## sorted() FA UNA COPIA
        copiaVotiOrdinata = sorted(self._voti, key=chiaveOrdinamentoEsamiAlfabetico)
        print(copiaVotiOrdinata)
    def stampa_ordinataPunteggioEsame(self):
        copiaVotiOrdinata = sorted(self._voti, key=chiaveOrdinamentoEsamiPunteggio, reverse=True)
        print(copiaVotiOrdinata)
    def cancellaVotiBrutti(self):
        votiBelli = []
        for v in self._voti:
            if v.punteggio >= 24:
                votiBelli.append(v)
        self._voti = votiBelli
        print(self._voti)



def estrai_campo_esame(v):
    return v.esame

def chiaveOrdinamentoEsamiAlfabetico(voto):
    return voto.esame

def chiaveOrdinamentoEsamiPunteggio(voto):
    return voto.punteggio
