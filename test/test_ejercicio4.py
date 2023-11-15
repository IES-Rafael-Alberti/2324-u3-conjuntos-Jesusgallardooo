import pytest

from src.ejercicio4 import diferencia_conjuntos, intersección_Frutas



def test_diferencia_conjuntos():
    assert diferencia_conjuntos({1,2,3}, {2,3,4}) == {1}
    
def test_intersección_Frutas():
    
    frutas1 = {'manzana', 'pera', 'naranja', 'plátano', 'uva'}
    frutas2 = {'manzana', 'pera', 'durazno', 'sandía', 'uva'} 
    
    assert intersección_Frutas(frutas1,frutas2) == {'uva', 'pera', 'manzana'}