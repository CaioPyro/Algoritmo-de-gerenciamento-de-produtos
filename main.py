# -*- coding: utf-8 -*-
import sqlite3
from procgen import clear, pausa
from banco import Banco
from dolar import ValorDoDolar

#Funções


def listar():
    db.select()

    for dados in db.dados:
        print(dados)

    pausa()


def inserir():
    nome_produto = input("Digite o nome do produto:")
    quantidade = input("Digite a quantidade do produto:")
    valor = input("Digite o valor do produto:")
    dados = (nome_produto, int(quantidade), float(valor))

    try:
      db.insert(dados)
    except sqlite3.OperationalError:
      print("Erro!")
    pausa()


def excluir():

  id = input("Digite o id:")
  escolha = input("Deseja realmente fazer essa exclusão?Tecle 'S' para sim ou 'N' para não: ")
  if(escolha == 'S' or escolha == 's'):
    db.delete(id)
    pausa("Exclusão concluída")
  if(escolha == 'N' or escolha == 'n'):
    print("Exclusão cancelada")
    pausa()
  else:
    print("Opção Inválida!")

def alterar():
    id = input("Digite o id:")
    db.select_one(id)
    for dados in db.dados:
        print(dados)

    nome_produto = input("Digite o nome do produto:")
    quantidade = input("Digite a quantidade do produto:")
    valor = input("Digite o valor do produto:")
    dados = (nome_produto, int(quantidade), float(valor), int(id))

    db.update(dados)
    pausa()


def criarBanco():
    conn = sqlite3.connect("meuBanco.db")
    c = conn.cursor()
    sqlstatement = "CREATE TABLE produtos(id INTEGER PRIMARY KEY AUTOINCREMENT, nome_produto VARCHAR(255), quantidade INTEGER, valor DECIMAL(9,2));"
    try:
        c.execute(sqlstatement)
    except sqlite3.OperationalError:
        print("Erro!")
    conn.commit()
    conn.close()


def entrada():
    id = input("Digite o id:")
    db.select_one(id)
    for dados in db.dados:
        print(dados)

    quantidade = input("Digite a quantidade a ser adicionado:")
    dados = (int(quantidade), int(id))

    db.somaEstoque(dados)
    pausa()


def saida():
    id = input("Digite o id:")
    db.select_one(id)
    for dados in db.dados:
        print(dados)

    quantidade = input("Digite a quantidade a ser retirado:")
    dados = (int(quantidade), int(id))

    db.subtrairEstoque(dados)
    pausa()


def AtualizarValor():
    percentual = float(input("Digite o percentual:"))
    percentual = percentual / 100
    dados =[]
    dados.append(percentual)

    db.atualizarValor(dados)
    pausa()

def mostrarDolar():
  dolar.consulta()
  valor = float(dolar.valor)
  dados =[]
  dados.append(valor)
  print("Valor do Dolar: ", dados)
  db.produtoDolar(dados)
  for dados in db.dados:
    print(dados)
  
  pausa()

criarBanco()
db = Banco()
dolar = ValorDoDolar()

opcao = 0
while opcao != 9:
    clear()
    print("""
      Menu
    
    
      1 – Listar Produtos 
      2 – Inserir Produto 
      3 – Excluir Produto 
      4 – Alterar Produto 
      5 – Entrada no estoque 
      6 – Saída no Estoque 
      7 – Listar Produtos com valor em dólar 
      8 – Atualizar valor 
      9 – Sair""")

    opcao = int(input("\nEscolha uma opção:"))

    if opcao == 1:
        listar()

    elif opcao == 2:
        inserir()

    elif opcao == 3:
      excluir()

    elif opcao == 4:
        alterar()

    elif opcao == 5:
        entrada()

    elif opcao == 6:
        saida()

    elif opcao == 7:
        mostrarDolar()

    elif opcao == 8:
        AtualizarValor()

    elif opcao == 9:
        print("Finalizando...")

    else:
        print("Opção inválida! Tente novamente")



