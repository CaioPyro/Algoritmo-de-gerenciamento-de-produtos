# -*- coding: utf-8 -*-
import sqlite3


class Banco():
  def __init__(self):
    self.conn = sqlite3.connect("meuBanco.db")

  def __del__(self):
    self.conn.close()

  def select(self):
    self.__cursor = self.conn.cursor()

    sqlstatement = "select * from produtos"

    try:
      self.__cursor.execute(sqlstatement)
    except sqlite3.OperationalError:
      print("Erro!")

    self.dados = self.__cursor.fetchall()


  def select_one(self, id):
    self.__cursor = self.conn.cursor()

    sqlstatement = "Select * from produtos where id=?"

    try:
      self.__cursor.execute(sqlstatement, id)
    except sqlite3.OperationalError:
      print("Erro!")

    self.dados = self.__cursor.fetchall()

  def select_valor(self):
    self.__cursor = self.conn.cursor()

    sqlstatement = "select valor from produtos"

    try:
      self.__cursor.execute(sqlstatement)
    except sqlite3.OperationalError:
      print("Erro!")

    self.dados = self.__cursor.fetchall()

  def insert(self, dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = "INSERT INTO produtos (nome_produto, quantidade, valor) VALUES (?, ?, ?)"
    try:
      self.__cursor.execute(sqlstatement, dados)
    except sqlite3.OperationalError:
      print("Erro!")

    self.conn.commit()


  def update(self, dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = """UPDATE produtos
  SET nome_produto=?, quantidade=?, valor=?
  WHERE id=?
  """

    try:
      self.__cursor.execute(sqlstatement, dados)
    except sqlite3.OperationalError:
      print("erro")

    self.conn.commit()


  def delete(self, id):
    self.__cursor = self.conn.cursor()
    sqlstatement = "DELETE FROM produtos WHERE id=?"
    try:
      self.__cursor.execute(sqlstatement, id)
    except sqlite3.OperationalError:
      print("Erro!")

    self.conn.commit()

  def somaEstoque(self,dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = """UPDATE produtos
  SET quantidade=quantidade + ?
  WHERE id=?
  """

    try:
      self.__cursor.execute(sqlstatement, dados)
    except sqlite3.OperationalError:
      print("erro")

    self.conn.commit()    

  def subtrairEstoque(self,dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = """UPDATE produtos
  SET quantidade=quantidade - ?
  WHERE id=?
  """

    try:
      self.__cursor.execute(sqlstatement, dados)
    except sqlite3.OperationalError:
      print("Erro!")

    self.conn.commit()

  def atualizarValor(self, dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = """UPDATE produtos
  SET valor= valor + (valor * ?)
  """
    try:
      self.__cursor.execute(sqlstatement, dados)
    except sqlite3.OperationalError:
      print("Erro!")
    
    self.conn.commit()

  def produtoDolar(self,dados):
    self.__cursor = self.conn.cursor()
    sqlstatement = "select nome_produto,valor,sum(valor*?) as 'Valor em dolar' from produtos group by valor"

    try:
      self.__cursor.execute(sqlstatement,dados)
    except sqlite3.OperationalError:
      print("Erro!")

    self.dados = self.__cursor.fetchall()