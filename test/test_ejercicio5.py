import pytest

from src.ejercicio5 import calcular_pares_de_un_conjunto, calcular_multiplosde3_de_un_conjunto, intersección_Pares_MultiplosdeTres

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
pares = {2, 4, 6, 8, 10}
multiplosDeTres = {9, 3, 6}

def test_calcular_pares_de_un_conjunto():
    assert calcular_pares_de_un_conjunto(numeros) == {2, 4, 6, 8, 10}

def test_calcular_multiplosde3_de_un_conjunto():
    assert calcular_multiplosde3_de_un_conjunto(numeros) ==  {9, 3, 6}
    
def test_intersección_Pares_MultiplosdeTres():
    assert intersección_Pares_MultiplosdeTres(pares, multiplosDeTres) == {6}