from UI.view import View
from modello.voto import Libretto, Voto
import flet as ft

class Controller(object):
    def __init__(self, view: View, libretto: Libretto):
        self._view = view
        self._model = libretto
        self.startUpLibretto()
        self._model.stampa()


    def handleAdd(self, e):
        """
        esame: str
        cfu: int
        punteggio: int
        lode: bool
        data: str
        :param e:
        :return:
        """
        nomeEsame = self._view._txtIn.value
        if nomeEsame == "":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto",
                                                      color="red"))
            self._view.update()
            return

        str_cfu = self._view._txtCFU.value
        try:
            int_cfu = int(str_cfu)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il campo CFU deve essere un intero",
                                                      color="red"))
            self._view.update()
            return
        punteggio = self._view._ddVoto.value
        if punteggio == None:
            self._view._lvOut.controls.append(ft.Text("Il campo PUNTEGGIO va selezionato",
                                                      color="red"))
            self._view.update()
            return
        if punteggio == "30 e Lode":
            punteggio = 30
            lode = True
        else:
            punteggio = int(punteggio)
            lode = False
        data = self._view._datePicker.value
        if data == None:
            self._view._lvOut.controls.append(ft.Text("Seleziona una data",
                                                      color="red"))
            self._view.update()
            return
        self._model.append(Voto(nomeEsame, int_cfu, punteggio, lode,
                                f"{data.year}-{data.month}-{data.day}"))        ## metodi di dateTime
        self._view._lvOut.controls.append(ft.Text("Voto correttamente aggiunto",
                                                  color="green"))
        self._view.update()
        return

    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))
        self._view._page.update()

    def startUpLibretto(self):
        self._model.append(Voto("Fisica 1", 10, 27, False, "2022-06-30"))
        self._model.append(Voto("Statistica", 10, 20, False, '2022-02-14'))
        self._model.append(Voto("Sistemi di produzione", 8, 30, True, '2023-07-15'))
        self._model.append(Voto("Algebra", 10, 30, False, '2022-06-27'))
        self._model.append(Voto("Programmazione a oggetti", 8, 29, False, '2024-02-8'))
