"""
Scrivere un programma Python che permetta di gestire un libretto universitario.
Il programma dovrà definire una classe Voto, che rappresenta un singolo esame superato,
ed una classe Libretto, che contiene l'elenco dei voti di uno studente.
"""


mio_libretto = Libretto()






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