from turtle import *
import math

rozmiar_planszy_x = 15
rozmiar_planszy_y = 10
wielkosc_pola = 20

tlo = "white"

# wymiary planszy w px
w = rozmiar_planszy_x * wielkosc_pola
h = rozmiar_planszy_y * wielkosc_pola

def napisz(row, col, numer):

    przemiesc_sie_na_pole(row, col)

    colors = {1:"blue", 2:"green", 3:"red", 4:"violet",
                5:"brown", 6:"black", 7:"black", 8:"black", -1:"black", 0:"grey"}
    color(colors[numer])

    fd(wielkosc_pola/10)
    rt(90)
    fd(wielkosc_pola/3)
    lt(90)
    pendown()
    write(numer, font=("Arial", int(wielkosc_pola/2), "bold"))


def rysuj_bombe(row, col, c="red"):

    przemiesc_sie_na_pole(row, col)
    u = wielkosc_pola # unit - jednostka
    a = u/16 # wysokość
    b = u/18 # szerokość/2
    color(c)
    fillcolor(c)
    penup()

    rt(90)
    fd(u/2)
    lt(90)
    fd(u/6)
    lt(90)

    pendown()
    begin_fill()
    for i in range(8):
        fd(b)
        rt(90)
        fd(a)
        lt(67.5)
        fd(2*b)
        lt(67.5)
        fd(a)
        rt(90)
        fd(b)
    end_fill()
    penup()


def rysuj_flage(row, col):

    przemiesc_sie_na_pole(row, col)
    u = wielkosc_pola
    color("red")
    fillcolor("red")
    penup()

    rt(90)
    fd(2*u/5)
    lt(90)
    fd(u/6)

    pendown()
    begin_fill()
    fd(4*u/6)
    rt(120)
    fd(u/3)
    rt(120)
    fd(u/3)
    end_fill()
    penup()


def usun_flage(row, col):

    przemiesc_sie_na_pole(row, col)
    fillcolor(tlo)
    penup()

    fd(wielkosc_pola/12)
    rt(90)
    fd(wielkosc_pola/12)
    lt(90)

    begin_fill()
    for i in range(4):
        fd(5*wielkosc_pola/6)
        rt(90)
    end_fill()


def rysuj_krzyzyk(row, col):

    przemiesc_sie_na_pole(row, col)
    color("red")
    width(2)
    rt(45)
    pendown()
    fd(wielkosc_pola * math.sqrt(2))
    penup()
    lt(135)
    fd(wielkosc_pola)
    lt(135)
    pendown()
    fd(wielkosc_pola * math.sqrt(2))
    penup()
    width(1)


def rysuj_plansze():

    penup()
    color("grey")
    setheading(90) # lewo
    for i in range(rozmiar_planszy_y + 1):
        goto(-w/2, -h/2 + i * wielkosc_pola)
        pendown()
        forward(w)
        penup()

    setheading(0) # góra
    for i in range(rozmiar_planszy_x + 1):
        goto(-w/2 + i * wielkosc_pola, -h/2)
        pendown()
        forward(h)
        penup()

    # rysuj pasek
    goto(-w/2, -h/2 + wielkosc_pola * rozmiar_planszy_y)
    rt(90)
    width(2)
    pendown()
    fd(w)
    lt(90)
    fd(30)
    lt(90)
    fd(w)
    lt(90)
    fd(30)
    penup()
    width(1)


def pisz_koniec(text):

    czysc_info()
    color("red")
    penup()
    goto(-30, h/2 + 10)
    pendown()
    write(text, font=("Arial", 8, "bold"))
    penup()


def pisz_info(l_min, l_flag):

    czysc_info()
    color("black")
    penup()
    goto(-80, h/2 + 10)
    pendown()
    write(f"Liczba min: {l_min}     Liczba flag: {l_flag}")
    penup()


def czysc_info():

    setheading(0)
    penup()
    color(tlo)
    fillcolor(tlo)
    goto(-w/2+2, h/2+2)
    pendown()
    begin_fill()
    fd(26)
    rt(90)
    fd(w-6)
    rt(90)
    fd(26)
    rt(90)
    fd(w-4)
    end_fill()
    penup()


def przemiesc_sie_na_pole(row, col):

    penup()
    goto(row * wielkosc_pola - w/2, col * wielkosc_pola - h/2)
    setheading(0)
