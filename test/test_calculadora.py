import pytest
from lib.calculadora import Calculadora

def test_calcular_dois_numeros():
    calc = Calculadora()
    resultado = calc.calcular("1,2")
    assert resultado == 3
    
def test_calcular_dois_numeros_pipe():
    calc = Calculadora()
    resultado = calc.calcular("1|2", '|')
    assert resultado == 3
    
def test_calcular_apenas_tres_numeros():
    calc = Calculadora()
    resultado = calc.calcular("1,2,6")
    assert resultado == 9

def test_calcular_apenas_tres_numeros_ponto():
    calc = Calculadora()
    resultado = calc.calcular("1.2.6.1", '.')
    assert resultado == 10