import functools

class Calculadora():
    def calcular(self, values):
        return sum(map(lambda x : int(x), values.split(',')))