# szkice

from Nalesniki import *

if __name__ == "__main__":
    nalesniki = Nalesniki()
    nalesniki.pokaz_przepis()
    for i in range(len(nalesniki.skladniki)):
        nalesniki.dodaj(nalesniki.skladniki[i])

    nalesniki.wbij_jajko()
    nalesniki.wymieszaj()
    for i in range(10):
        nalesniki.usmaz()


