import copy
from dataclasses import dataclass

@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

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
class Libretto:
    def __init__(self):
        self._voti = []

    @property
    def voti(self):
        return self._voti
    def append(self, voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
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

    def migliora_voti(self):
        for v in self._voti:
            if 24 <= v.punteggio <= 28:
                v.punteggio += 2
            elif v.punteggio >= 18:
                v.punteggio += 1

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




def chiaveOrdinamentoEsamiAlfabetico(voto):
    return voto.esame
def chiaveOrdinamentoEsamiPunteggio(voto):
    return voto.punteggio
