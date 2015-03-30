# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:29:02 2015
@author: Eric Otofuji
"""
import turtle
import random
window=turtle.Screen()
window.bgcolor("white")
window.title("Forca da Força do Enforcamento")
forca=turtle.Turtle()
forca.speed(5)
forca.pendown()
dfup=200
ang90=90
dfrg=52
dfdw=21
forca.color("black")
forca.setpos(21,0)
forca.left(ang90)
forca.forward(dfup)
forca.right(ang90)
forca.forward(dfrg)
forca.right(dfup)
forca.forward(dfdw)
arq = open("db.txt", encoding="utf-8") 
word=arq.readlines()
w = random.choice(word)
error=0
if error==1:
    err1=turtle.Turtle()
    err1.speed(5)
    err1.pendown()
    dfup=200
    ang90=90
    dfrg=52
    dfdw=21
    err1.color("black")
    err1.setpos(21,0)
    err1.forward(dfup)
    err1.right(ang90)
    err1.forward(dfrg)
    err1.right(dfup)
    err1.forward(dfdw)
    err1.circle(12)
if error==2:
    err2=turtle.Turtle()
    err2.speed(5)
    err2.pendown()
    dfup=200
    ang90=90
    dfrg=52
    dfdw=21
    err2.color("black")
    err2.setpos(21,0)
    err2.forward(dfup)
    err2.right(ang90)
    err2.forward(dfrg)
    err2.right(dfup)
    err2.forward(dfdw)
    err2.circle(12)
    err2.left(ang90)
    err2.forward(dfdw)
    err2.forward(dfrg)
if error==3:
    err3=turtle.Turtle()
    err3.speed(5)
    err3.pendown()
    dfup=200
    ang90=90
    ang45=45
    dfrg=52
    dfdw=21
    err3.color("black")
    err3.setpos(21,0)
    err3.forward(dfup)
    err3.right(ang90)
    err3.forward(dfrg)
    err3.right(dfup)
    err3.forward(dfdw)
    err3.circle(12)
    err3.left(ang90)
    err3.forward(dfdw)
    err3.forward(dfrg)
    err3.left(ang45)
    err3.forward(dfdw)
if error==4:
    err4=turtle.Turtle()
    err4.speed(5)
    err4.pendown()
    dfup=200
    ang90=90
    ang45=45
    dfrg=52
    dfdw=21
    err4.color("black")
    err4.setpos(21,0)
    err4.forward(dfup)
    err4.right(ang90)
    err4.forward(dfrg)
    err4.right(dfup)
    err4.forward(dfdw)
    err4.circle(12)
    err4.left(ang90)
    err4.forward(dfdw)
    err4.forward(dfrg)
    err4.right(ang45)
    err4.forward(dfdw)
if error==5:
    err5=turtle.Turtle()
    err5.speed(5)
    err5.pendown()
    dfup=200
    ang90=90
    ang45=45
    dfrg=52
    dfdw=21
    err5.color("black")
    err5.setpos(21,0)
    err5.forward(dfup)
    err5.right(ang90)
    err5.forward(dfrg)
    err5.right(dfup)
    err5.forward(dfdw)
    err5.circle(12)
    err5.left(ang90)
    err5.forward(dfdw)
    err5.forward(dfdw)
    err5.left(ang45)
    err5.forward(dfdw)
if error==6:
    err6=turtle.Turtle()
    err6.speed(5)
    err6.pendown()
    dfup=200
    ang90=90
    ang45=45
    dfrg=52
    dfdw=21
    err6.color("black")
    err6.setpos(21,0)
    err6.forward(dfup)
    err6.right(ang90)
    err6.forward(dfrg)
    err6.right(dfup)
    err6.forward(dfdw)
    err6.circle(12)
    err6.left(ang90)
    err6.forward(dfdw)
    err6.forward(dfdw)
    err6.right(ang45)
    err6.forward(dfdw)
if error==7:
    err7=turtle.Turtle()
    err7.speed(5)
    err7.pendown()
    dfup=200
    ang90=90
    ang45=45
    dfrg=52
    dfdw=21
    err7.color("red")
    err7.setpos(21,0)
    err7.forward(dfup)
    err7.right(ang90)
    err7.forward(dfrg)
    err7.right(dfup)
    err7.forward(dfdw)
    err7.circle(12)
    err7.left(ang90)
    err7.forward(dfdw)
    err7.forward(dfrg)
    print("Sinto muito. Você perdeu. É tarde demais e foi morto por enforcamento.")
#line=turtle.Turtle()
#line.setpos(400,85)
#line.pendown()
#line.write(len(w)*"___ ")
while error<7:
    et= input("E a letra é... ") #et é a letra que o usuário escolhe e consequentemente digita para jogar este jogo
    for i in w:    
        if et in w:
            print (et[i])   
        else:
            error+=1
window.exitonclick()