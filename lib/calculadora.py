class Calculadora():
    def calcular(self, valor, separador = ','):
        return sum(map(lambda x : int(x), valor.split(separador)))