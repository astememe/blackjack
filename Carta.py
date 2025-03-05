class Carta:
    def __init__(self, palo, valor, nombre):
        self.palo = palo
        self.valor = valor
        self.nombre = nombre
    def getCarta(self):
        return f"{self.nombre} de {self.palo}"
    def getValor(self):
        return self.valor
