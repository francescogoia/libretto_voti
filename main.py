import flet as ft
from UI.view import View
from UI.controller import Controller
from modello.voto import Libretto


def main(page: ft.page):
    v = View(page)
    l = Libretto()
    c = Controller(v, l)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target = main)
