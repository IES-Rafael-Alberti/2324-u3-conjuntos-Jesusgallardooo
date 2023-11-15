import pytest

from src.ejercicio3 import conjunto_potencia

def test_conjunto_potencia():
    
    # Caso de prueba con un conjunto vacío
    assert conjunto_potencia(set()) == [set()]

    # Caso de prueba con un conjunto no vacío
    conjunto_s = {1, 2, 3}
    assert conjunto_potencia(conjunto_s) ==   [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}]

