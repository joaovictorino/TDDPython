import pytest
from Calculadora import Calculadora

def test_calcular_dois_numeros():
    calc = Calculadora()
    resultado = calc.calcular("1,2")
    assert resultado == 3

    
def test_calcular_apenas_tres_numeros():
    calc = Calculadora()
    resultado = calc.calcular("1,2,6")
    assert resultado == 9