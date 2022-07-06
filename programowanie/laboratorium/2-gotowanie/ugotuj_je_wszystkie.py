## GOTOWANIE
from Nalesniki import Nalesniki
from Polewa import Polewa_czekoladowa
from Tort import Tort


def nalesniki():
    x = Nalesniki()
    x.pokaz_przepis()
    for e in range(4):
        x.dodaj(x._skladniki[e])
    if not x.wbij_jajko():
        x.napraw()
    x.wymieszaj()
    for i in range(10):
        x.usmaz()
    x.status()


def polewa():
    x = Polewa_czekoladowa()
    x.pokaz_przepis()
    x.dodaj("smietana30%")
    for i in range(80, 5):
        x.podgrzej()
    x.dodaj("czekolada")
    while not x.status():
        x.podgrzej()
    return x


def tort(polewa):
    t = [
        "              ",
        " \(*=*)/ ",
        "     ( )     ",
        "   _/ \_   ",
        "              "
    ]
    x = Tort(polewa)
    x.dekoruj(t)
    x.status()


nalesniki()
tort(polewa())
