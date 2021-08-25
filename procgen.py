# -*- coding: utf-8 -*-
from os import system, name

def clear():
  if name == "nt":
    _ = system("cls")
  else:
    _ = system("clear")

def pausa(mensagem = "Pressione qualquer tecla para continuar..."):
  print("")
  print(mensagem)
  system("read n1")