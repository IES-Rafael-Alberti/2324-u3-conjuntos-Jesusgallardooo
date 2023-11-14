import pytest
from src.ejercicio6 import intersección_conjuntos

conjunto1 = {'a', 'e', 'i', 'o', 'u'}
conjunto2 = {'a', 'b', 'c', 'd', 'e'}
conjunto3 = {'a', 'e', 'i', 'o', 'b'}

def test_intersección_conjuntos():
    assert intersección_conjuntos(conjunto1, conjunto2) == {'a', 'e'}
    assert intersección_conjuntos(conjunto1, conjunto3) == {'a', 'e', 'i', 'o'}