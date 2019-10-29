# ------------- Obsługa myszki - początek-------------
from turtle import onscreenclick
from time import sleep
import tkinter

zdarzenie_myszki = ""
x_myszki = 0
y_myszki = 0


def ustaw_guziki_myszy(guzik):
    def result(x, y):
        global zdarzenie_myszki, x_myszki, y_myszki
        zdarzenie_myszki, x_myszki, y_myszki = guzik, x, y

    return result


def daj_zdarzenie():
    global zdarzenie_myszki, x_myszki, y_myszki
    while zdarzenie_myszki == "":
        tkinter._default_root.update()
        sleep(0.01)
    print(f"zdarzenie={zdarzenie_myszki}, x={x_myszki}, y={y_myszki}")
    pom, zdarzenie_myszki = zdarzenie_myszki, ""
    return pom, x_myszki, y_myszki


def ini_myszki():
    for guzik, numer in zip(["l_klik", "m_klik", "r_klik"], range(1, 4)):
        # print("ustawiam zdarzenie: " + guzik)
        onscreenclick(ustaw_guziki_myszy(guzik.lower()), numer)


# ------------- Obsługa myszki - koniec-------------
