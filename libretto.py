"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""
import copy
from dataclasses import dataclass

@dataclass
class Voto:
    def __init__(self, esame, cfu, punteggio, lode, data):
        self.esame = esame
        self.cfu = cfu
        self.punteggio = punteggio
        self.lode = lode
        self.data = data

        if self.lode and self.punteggio!=30:
            raise ValueError("Lode non applicabile")

    def __str__(self):
        return f"Esame {self.esame} superato con {self.punteggio}"

    def __repr__(self):
        return f"Voto('{self.esame}', {self.cfu}, {self.punteggio}, {self.lode}, '{self.data}')"


class Libretto:
    def __init__(self):
        self._voti = []

    @property
    def voti(self):
        return self._voti
    def append(self, voto):
        if (self.verifica_conflitto(voto) is False
                and (self.verifica_esami_gia_registrati(voto)) is False):
            self._voti.append(voto)

    def media(self):
        if len(self._voti)==0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

    def stampa_corsi_voti_maggiori_25(self):
        for v in self._voti:
            if v.punteggio > 25:
                print(v.esame)

    def cerca_esame(self, nome_corso):
        for v in self._voti:
            if v.esame == nome_corso:
                return v.punteggio

    def verifica_esami_gia_registrati(self, voto):
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio:
                raise ValueError("Errore esame già inserito nel libretto")
                return True
        return False
    def verifica_conflitto(self, voto):
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio != voto.punteggio:
                raise ValueError("Errore esame in conflitto con il libretto")
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

voto_1 = Voto("Analisi Matematica 1", 10, 25, False, '2022-02-10')
voto_2 = Voto("Fisica 1", 10, 27, False, '2022-06-15')
voto_3 = Voto("Analisi Matematica 2", 8, 23, False, '2023-02-16')
voto_4 = Voto("Basi di Dati", 8, 30, True, '2023-01-30')
voto_5 = Voto("FIsica 2", 6, 25, False, '2023-02-05')
voto_6 = Voto("Statistica", 10, 20, False, '2022-02-14')
voto_7 = Voto("Algebra", 10, 30, False, '2022-06-27')
voto_8 = Voto("Informatica", 8, 23, False, '2022-02-04')
voto_9 = Voto("Economia", 8, 28, False, '2023-07-18')
voto_10 = Voto("Sistemi di produzione", 8, 30, True, '2023-07-15')
voto_11 = Voto("Sistemi elettrici", 8, 30, False, '2023-06-30')
voto_12 = Voto("Programmazione a oggetti", 8, 29, False, '2024-02-8')

mio_libretto = Libretto()

lista_voti = [voto_1, voto_2, voto_3, voto_4, voto_5, voto_6, voto_7, voto_8, voto_9, voto_10, voto_11, voto_12]
for v in lista_voti:
    mio_libretto.append(v)




mio_libretto.stampa_corsi_voti_maggiori_25()
print("Voto esame 'Economia': ",mio_libretto.cerca_esame("Economia"))

"""
voto_duplicato = Voto("FIsica 2", 6, 25, False, '2023-02-05')
voto_conflitto = Voto("FIsica 2", 6, 27, False, '2023-02-05')
mio_libretto.append(voto_duplicato)
mio_libretto.append(voto_conflitto)
"""

libretto_migliorato = copy.deepcopy(mio_libretto)           ## DEVO CREARE DUE OGGETTI SEPARATI
libretto_migliorato.migliora_voti()
print()
print("libretto onesto", mio_libretto.voti)
print("libretto migliorato", libretto_migliorato.voti)
print()
mio_libretto.stampa_ordineAlfabeticoEsame()
mio_libretto.stampa_ordinataPunteggioEsame()

mio_libretto.cancellaVotiBrutti()