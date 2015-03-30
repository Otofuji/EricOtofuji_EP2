# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:29:02 2015

@author: Eric Otofuji
"""

import turtle
import random
window=turtle.screen()
window.bgcolor("white")
window.title("Forca da Força do Enforcamento")
forca=turtle.Turtle()
forca.speed(5)
forca.penup()
dfup=200
ang90=90
dfrg=52
dfdw=21
forca.color("black")
forca.setpos(21,0)
forca.forward(dfup)
forca.right(ang90)
forca.forward(dfrg)
forca.right(dfup)
forca.forward(dfdw)
with open("db.txt", encoding="utf-8") as db: #from alcor.concordia.ca/~vjorge/Palavras-Cruzadas/Lista-de-Palavras.txt
    word=db.read().splitlines()
w = random.shuffle(word)
while w == w:
    w = random.shuffle(word)
et = window.textinput("E a letra é... ") #et é a letra que o usuário escolhe e consequentemente digita para jogar este jogo
while et != "a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k" or "l" or "m" or "n" or "o" or "p" or "q" or "r" or "s" or "t" or "u" or "v" or "w" or "x" or "y" or "z" or "A" or "B" or "C" or "D" or "E" or "F" or "G" or "H" or "I" or "J" or "K" or "L" or "M" or "N" or "O" or "P" or "Q" or "R" or "S" or "T" or "U" or "V" or "W" or "X" or "Y" or "Z" or "-":
    et = input("NÃO, CRIATURA! Use apenas letras ou hífen! Escolha uma LETRA ou hífen: ")
