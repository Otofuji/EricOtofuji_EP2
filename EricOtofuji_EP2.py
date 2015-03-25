# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:29:02 2015

@author: Eric Otofuji
"""

from turtle import *
from random import *
et = window.textinput("Forca da Força do Enforcamento","E a letra é... ") #et é a letra que o usuário escolhe e consequentemente digita para jogar este jogo
db = open("db.txt", encoding="ansi") #db é o banco de dados de todas as palavras em língua portuguesa existentes, conforme alcor.concordia.ca/~vjorge/Palavras-Cruzadas/Lista-de-Palavras.txt
