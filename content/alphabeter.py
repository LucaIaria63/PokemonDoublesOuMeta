import turtle
from tkinter import *


'''
TO BE USED WITH TKINTER ( UNCOMMENT THIS CODE AND Replace with StringVar EverWhere)
from tkinter import  ttk

txt = StringVar()
bg = StringVar()
fg = StringVar()
txt.set("")
bg.set("black")
fg.set("red")
font = StringVar()
font.set("10")
'''

#To be used without tkinter
txt = ""
bg = "white"
fg = "black"
font = 1
startx=-300
starty = 200
speedOfCursor = 100

#End of initialization

def setSpeed(speed):
    global speedOfCursor
    speedOfCursor= speed

def setStartX(X):
    global startx
    startx= X
def setStartY(Y):
    global  starty
    starty= Y
def setTxt(text):
    global txt
    txt = text
def setBackGroundColor(color):
    global bg
    bg = color
def setForeGroundColor(color):
    global fg
    fg = color
def setFontSize(size):
    global font
    font = size

def printBlank():
    turtle.color(bg)
    turtle.forward(30)


def printA(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(90)


def printB(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)

def printC(color):
    turtle.color(color)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color(str(bg))
    turtle.forward(100)
    turtle.left(90)

def printD(color):
    turtle.color(color)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)


def printE(color):
    turtle.color(color)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color(str(bg))
    turtle.forward(100)
    turtle.left(90)

def printF(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color(str(bg))
    turtle.forward(100)
    turtle.left(90)


def printG(color):
    turtle.color(color)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color(str(bg))
    turtle.forward(50)
    turtle.color(color)
    turtle.forward(50)
    turtle.left(90)

def printH(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.color(str(bg))
    turtle.forward(50)
    turtle.right(90)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(90)


def printI(color):
    turtle.color(color)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.color(str(bg))
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

def printJ(color):
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.color(color)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(180)
    turtle.forward(50)
    turtle.color(str(bg))
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)


def printK(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(70.71)
    turtle.left(180)
    turtle.forward(70.71)
    turtle.left(90)
    turtle.forward(70.71)
    turtle.left(45)

def printL(color):
    turtle.left(90)
    turtle.forward(100)
    turtle.color(color)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)


def printM(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(135)
    turtle.forward(55.90)
    turtle.left(90)
    turtle.forward(55.90)
    turtle.right(135)
    turtle.forward(100)
    turtle.left(90)


def printN(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(150)
    turtle.forward(115.70)
    turtle.left(150)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)

def printO(color):
    turtle.left(90)
    turtle.forward(5)
    turtle.color(color)
    turtle.forward(90)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(90)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(180)
    turtle.forward(7.07)
    turtle.left(45)
    turtle.forward(40)
    turtle.color(str(bg))
    turtle.forward(5)

def printP(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(45)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.color(str(bg))
    turtle.forward(50)

def printQ(color):
    turtle.left(90)
    turtle.forward(10)
    turtle.color(color)
    turtle.forward(80)
    turtle.right(45)
    turtle.forward(14.14)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(14.14)
    turtle.right(45)
    turtle.forward(80)
    turtle.right(45)
    turtle.forward(14.14)
    turtle.right(45)
    turtle.forward(30)
    turtle.right(45)
    turtle.forward(14.14)
    turtle.right(180)
    turtle.forward(14.14)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(7.07)
    turtle.left(90)
    turtle.forward(7.07)
    turtle.left(180)
    turtle.forward(14.14)
    turtle.left(180)
    turtle.forward(7.07)
    turtle.left(90)
    turtle.forward(7.07)
    turtle.left(135)
    turtle.color(str(bg))
    turtle.forward(5)

def printR(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(45)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(45)
    turtle.left(180)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(58.30)
    turtle.left(60)

def printS(color):
    turtle.color(color)
    turtle.forward(45)
    turtle.left(45)
    turtle.forward(7.07)
    turtle.left(45)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(7.07)
    turtle.left(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(40)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(45)
    turtle.color(str(bg))
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(5)
    turtle.left(180)

def printT(color):
    turtle.forward(30)
    turtle.left(90)
    turtle.color(color)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(180)
    turtle.forward(60)
    turtle.color(str(bg))
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)

def printU(color):
    turtle.forward(5)
    turtle.color(color)
    turtle.left(135)
    turtle.forward(7.07)
    turtle.right(45)
    turtle.forward(95)
    turtle.left(180)
    turtle.forward(95)
    turtle.left(45)
    turtle.forward(7.07)
    turtle.left(45)
    turtle.forward(40)
    turtle.left(45)
    turtle.forward(7.07)
    turtle.left(45)
    turtle.forward(95)
    turtle.left(180)
    turtle.forward(95)
    turtle.right(45)
    turtle.forward(7.07)
    turtle.left(135)
    turtle.color(str(bg))
    turtle.forward(5)

def printV(color):
    turtle.forward(25)
    turtle.color(color)
    turtle.left(135)
    turtle.forward(55.90)
    turtle.right(45)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.left(45)
    turtle.forward(55.90)
    turtle.left(90)
    turtle.forward(55.90)
    turtle.left(45)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.color(str(bg))
    turtle.forward(50)
    turtle.left(90)

def printW(color):
    turtle.color(color)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(55.90)
    turtle.right(90)
    turtle.forward(55.90)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(180)
    turtle.forward(100)
    turtle.left(90)

def printX(color):
    turtle.forward(50)
    turtle.color(color)
    turtle.left(116.551)
    turtle.forward(111.80)
    turtle.left(180)
    turtle.forward(55.90)
    turtle.right(53.102)
    turtle.forward(55.90)
    turtle.left(180)
    turtle.forward(111.80)
    turtle.right(153.449)
    turtle.color(str(bg))
    turtle.forward(100)
    turtle.left(90)

def printY(color):
    turtle.forward(25)
    turtle.color(color)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(40)
    turtle.forward(65)
    turtle.left(180)
    turtle.forward(65)
    turtle.left(100)
    turtle.forward(65)
    turtle.left(180)
    turtle.forward(65)
    turtle.left(40)
    turtle.forward(50)
    turtle.left(90)
    turtle.color(str(bg))
    turtle.forward(30)

def printZ(color):
    turtle.color(color)
    turtle.left(63.45)
    turtle.forward(111.80)
    turtle.left(116.55)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(116.551)
    turtle.forward(111.80)
    turtle.left(116.55)
    turtle.forward(50)

def printNewLine():
    turtle.color(str(bg))
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.setx(startx)

    turtle.sety(turtle.ycor()-150)

def printData(txt):


    turtle.color(str(bg))
    turtle.setx(startx)
    turtle.sety(starty)
    turtle.speed(speedOfCursor)
    print(fg)
    print(bg)
    print(txt)
    turtle.width(int(font))
    turtle.bgcolor(str(bg))
    txtnew = str(txt).upper()

    for i in txtnew:
        if turtle.xcor() > 500:
            printNewLine()
        if i == 'A':
            print("inside")
            printA(str(fg))
        elif i == 'B':
            printB(str(fg))
        elif i == 'C':
            printC(str(fg))
        elif i == 'D':
            printD(str(fg))
        elif i == 'E':
            printE(str(fg))
        elif i == 'F':
            printF(str(fg))
        elif i == 'G':
            printG(str(fg))
        elif i == 'H':
            printH(str(fg))
        elif i == 'I':
            printI(str(fg))
        elif i == 'J':
            printJ(str(fg))
        elif i == 'K':
            printK(str(fg))
        elif i == 'L':
            printL(str(fg))
        elif i == 'M':
            printM(str(fg))
        elif i == 'N':
            printN(str(fg))
        elif i == 'O':
            printO(str(fg))
        elif i == 'P':
            printP(str(fg))
        elif i == 'Q':
            printQ(str(fg))
        elif i == 'R':
            printR(str(fg))
        elif i == 'S':
            printS(str(fg))
        elif i == 'T':
            printT(str(fg))
        elif i == 'U':
            printU(str(fg))
        elif i == 'V':
            printV(str(fg))
        elif i == 'W':
            printW(str(fg))
        elif i == 'X':
            printX(str(fg))
        elif i == 'Y':
            printY(str(fg))
        elif i == 'Z':
            printZ(str(fg))
        elif i == ' ':
            printBlank()
        printBlank()

