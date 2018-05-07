class NodoSkip:
	def __init__(self, elem):
		self.__elem = elem
		self.__der = None
		self.__izq = None
		self.__arriba = None
		self.__abajo = None

	def getElem(self):
		return self.__elem

	def setElem(self, elem):
		self.__elem = elem

	def getDer(self):
		return self.__der

	def setDer(self, nodo):
		self.__der = nodo

	def getIzq(self):
		return self.__izq

	def setIzq(self, nodo):
		self.__izq = nodo

	def getArriba(self):
		return self.__arriba

	def setArriba(self, nodo):
		self.__arriba = nodo
		
	def getAbajo(self):
	  return self.__abajo
	  
	def setAbajo(self, nodo):
	  self.__abajo = nodo

	def toString(self):
		return self.__elem + ""
		
	def ligaID(self, nodo):
	  self.setDer(nodo)
	  nodo.setIzq(self)