from view import View
from voto import Libretto, Voto
import flet as ft

class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Libretto()
        self.startUpLibretto()
        self._model.stampa()


    def handleAdd(self, e):
        pass
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
