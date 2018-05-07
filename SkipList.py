from NodoSkipList import *
import math
import random2 as r2 

class SkipList:
  def __init__(self):
    self.__contador = 0
    self.__niveles = 1
    self.__cabeza = NodoSkip(None)
    self.__cola  = NodoSkip(None)
    self.__cabeza.setDer(self.__cola)
    self.__cola.setIzq(self.__cabeza)
  
  def getContador(self):
    return self.__contador
  
  def getNiveles(self):
    return self.__niveles
    
  def getCabeza(self):
    return self.__cabeza
    
  def busca(self, elem):
    temp = __buscaInterno(elem)
    if temp.getElem() == elem:
      return True
    return False
    
  def __buscaInterno(self, elem):
    i = 0
    actual = self.__cabeza
    while i <= self.__niveles:
      while actual.getDer().getElem() is not None and actual.getDer().getElem() < elem:
        actual = actual.getDer()
      if i < self.__niveles:
        actual = actual.getAbajo()
      i += 1
    return actual
      
  def borra(self,elem):
    temp = __buscaInterno(elem)
    if temp.getElem() is not elem:
      return
    while temp is not None:
      temp.getIzq().setDer(temp.getDer())
      temp.getDer().setIzq(temp.getIzq())
      temp = temp.getArriba()
    self.__contador -= 1
    if self.__niveles > math.log(self.__contador + 1, 2):
      self.__cabeza = cabeza.getAbajo()
      self.__cola = cola.getAbajo()
      self.__niveles -= 1
      actual = self.__cabeza
      while actual is not None:
        actual.setArriba(None)
        actual = actual.getDer()
        
  def inserta(self, elem):
    nuevo = NodoSkip(elem)
    i = 1
    temp = self.__buscaInterno(elem)
    nuevo.ligaID(temp.getDer())
    temp.ligaID(nuevo)
    self.__contador -= 1
    volados = math.log(cont, 2)
    while i < volados and r2.random() > 0.5:
      if i == niveles:
        self.agregaNivel()
      while temp.getArriba() is None:
        temp = temp.getIzq()
      temp = temp.getArriba()
      nuevo2 = NodoSkip(elem)
      nuevo2.ligaID(temp.getDer())
      temp.ligaID(nuevo2)
      nuevo2.setAbajo(nuevo)
      nuevo.setArriba(nuevo2)
      nuevo = nuevo2
      i += 1
      
  def agregaNivel(self):
    temp = NodoSkip(None)
    temp.setAbajo(self.__cabeza)
    self.__cabeza.setArriba(temp)
    self.__cabeza = temp
    temp = NodoSkip(None)
    temp.setAbajo(self.__cola)
    self.__cola.setArriba(temp)
    self.__cola = temp
    self.__cabeza.ligaID(cola)
    
  def print(self):
    s = ""
    temp = self.__cabeza
    cont = 1
    while (cont < self.__niveles):
      temp = temp.getAbajo
      cont += 1
    while temp.getDer().getElem() is not None:
      temp = temp.getDer()
      s += temp.getElem()
      s += " "
    return s
      