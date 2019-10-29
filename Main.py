from turtle import *
from time import sleep
from random import randint

from rysowanie import *
from obsluga_myszki import *


tablica_bomb = [[False]*rozmiar_planszy_y for i in range(rozmiar_planszy_x)]
tablica_flag = [[False]*rozmiar_planszy_y for i in range(rozmiar_planszy_x)]
tablica_odslonietych = [[False]*rozmiar_planszy_y for i in range(rozmiar_planszy_x)]
liczba_min = 0
liczba_ustawionych_flag = 0
liczba_odslonietych_pol = 0

def ini_grafiki():
    window = Screen()
    window.setup(width=w+50, height=h+100, startx=0, starty=0)
    mode("logo")
    tracer(0, 0)
    bgcolor(tlo)


def gra():

    trwa = True;
    while trwa:
        zdarzenie, x, y = daj_zdarzenie()
        row = (x + w/2) // wielkosc_pola
        col = (y + h/2) // wielkosc_pola
        row = int(row)
        col = int(col)
        if row < 0 or col < 0 or row >= rozmiar_planszy_x or col >= rozmiar_planszy_y:
            pass
        else:
            print(f"Wybrane pole: ({row}, {col})")
            if zdarzenie == "l_klik":
                odslon_pole(row, col)
                sprawdz_czy_wygral()
            elif zdarzenie == "r_klik":
                oznacz_flaga(row, col)
                sprawdz_czy_wygral()
            elif zdarzenie == "m_klik":
                print("Czy są przewidziane zwolnienia z egzaminu?")
            else:
                print("Nieobsługiwane zdarzenie: " + zdarzenie)

            pisz_info(liczba_min, liczba_ustawionych_flag)


def oznacz_flaga(row, col):

    global liczba_ustawionych_flag
    # jeśli pole już zostało odsłonięte -> zignoruj
    if tablica_odslonietych[row][col]:
        pass
    # jeśli pole było już oznaczone flagą odznacz je i usuń obrazek flagi
    elif tablica_flag[row][col]:
        tablica_flag[row][col] = False
        usun_flage(row, col)
        liczba_ustawionych_flag -= 1
    # pole nie było oznaczone flagą -> oznacz i narysuj
    else:
        tablica_flag[row][col] = True
        rysuj_flage(row, col)
        liczba_ustawionych_flag += 1


def odslon_pole(row, col):

    # jeśli pole już zostało odsłonięte -> zignoruj
    # jeśli pole zostało oznaczone flagą -> zignoruj
    if tablica_odslonietych[row][col] or tablica_flag[row][col]:
        pass
    # odsłonięto bombę -> koniec gry
    elif tablica_bomb[row][col]:
        koniec_gry(row, col)
    # pole nie zostało jeszcze odsłonięte i nie ma na nim bomby
    else:
        global liczba_odslonietych_pol
        liczba_odslonietych_pol += 1
        tablica_odslonietych[row][col] = True
        mozliwosci = [(-1,-1), (-1,0), (-1,1), (0,1),
                        (1,1), (1,0), (1,-1), (0,-1)]
        ile = 0
        # sprawdź ile sąsiadów
        for x,y in mozliwosci:
            temp_row = row + x
            temp_col = col  + y
            if (temp_row >= 0) and (temp_col >= 0) and (temp_row < rozmiar_planszy_x) and (temp_col < rozmiar_planszy_y):
                if tablica_bomb[temp_row][temp_col]:
                    ile += 1

        # jeśli nie było sąsiadów, odsłoń rekursywnie granice pustego obszaru
        if ile == 0:
            for x,y in mozliwosci:
                temp_row = row + x
                temp_col = col  + y
                if (temp_row >= 0) and (temp_col >= 0) and (temp_row < rozmiar_planszy_x) and (temp_col < rozmiar_planszy_y):
                    odslon_pole(temp_row, temp_col)

        # oznacz graficznie odkryte pole
        napisz(row, col, ile)




def losuj_gre():

    global liczba_min
    liczba_bomb = randint(rozmiar_planszy_x, int((rozmiar_planszy_x * rozmiar_planszy_y)/2))
    print(liczba_bomb)
    ile = 0
    for i in range(liczba_bomb):
        a = randint(0, rozmiar_planszy_x - 1)
        b = randint(0, rozmiar_planszy_y - 1)
        print(a,b)
        if not tablica_bomb[a][b]:
            ile += 1
        tablica_bomb[a][b] = True
        # rysuj_bombe(a,b, "grey") # RYSUJE PODPOWIEDZI

    print(f"Rozłożono {ile} bomb (wylosowano {liczba_bomb})")
    liczba_min = ile
    pisz_info(liczba_min, liczba_ustawionych_flag)
    return ile

    
def sprawdz_czy_wygral():

    # jesli liczba odslonietych pol jest maksymalna (x*y-liczba_min) -> wygrana
    if rozmiar_planszy_x * rozmiar_planszy_y == liczba_odslonietych_pol + liczba_min:
        wygrana()

    # jeśli tyle samo min co flag i wszystkie pozycje takie same -> wygrana
    czy_wygral = True
    if liczba_min == liczba_ustawionych_flag:
        for x in range(rozmiar_planszy_x):
            for y in range(rozmiar_planszy_y):
                if not tablica_bomb[x][y] == tablica_flag[x][y]:
                    czy_wygral = False

        if czy_wygral:
            wygrana()


def wygrana():
    print("WYGRANA")
    for x in range(rozmiar_planszy_x):
        for y in range(rozmiar_planszy_y):
            if tablica_bomb[x][y]:
                usun_flage(x,y)
                rysuj_bombe(x,y,"green")
                rysuj_flage(x,y)
    pisz_koniec("WYGRANA!!!")
    exitonclick()


def koniec_gry(row,col):
    # oznaczenia graficzne
    for x in range(rozmiar_planszy_x):
        for y in range(rozmiar_planszy_y):
            if tablica_bomb[x][y]:
                if tablica_flag[x][y]:
                    rysuj_bombe(x,y,"green")
                    rysuj_flage(x,y)
                else:
                    rysuj_bombe(x,y)
            elif tablica_flag[x][y]:
                rysuj_krzyzyk(x, y)

    rysuj_bombe(row,col,"yellow")
    pisz_koniec("KONIEC GRY")
    exitonclick()


def main():
    ini_grafiki()
    ini_myszki()
    rysuj_plansze()
    losuj_gre()
    gra()


main()
