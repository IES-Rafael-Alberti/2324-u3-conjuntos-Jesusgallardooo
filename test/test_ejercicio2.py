import pytest

from src.ejercicio2 import nombres_repetidos, nombres_no_repetidos, nombresPrimaria_incluidosEn_nombresSecundaria,obtener_nombres

#def test_obtener_nombres(): ¿?¿?¿?

def test_nombres_repetidos():
    primaria = {"Juan", "Ana", "Carlos", "Maria"}
    secundaria = {"Ana", "Carlos", "Luis", "Maria"}
    
    assert nombres_repetidos(primaria, secundaria) == {'Ana', 'Carlos', 'Maria'}
    
    primaria = {"Juan", "Pedro", "Lucia"}
    secundaria = {"Ana", "Carlos", "Luis", "Maria"}
    
    assert nombres_repetidos(primaria, secundaria) == set()

def test_nombres_no_repetidos():
    primaria = {"Juan", "Ana", "Carlos", "Maria"}
    secundaria = {"Ana", "Carlos", "Luis", "Maria"}
    
    assert nombres_no_repetidos(primaria,secundaria) == {'Juan'}
    
    primaria = {"pedro"}
    secundaria = {"pedro"}
    
    assert nombres_no_repetidos(primaria,secundaria) == set()

def test_nombresPrimaria_incluidosEn_nombresSecundaria():
    primaria = {"Juan", "Ana", "Carlos", "Maria"}
    secundaria = {"Juan", "Ana", "Carlos", "Maria"}
    
    assert nombresPrimaria_incluidosEn_nombresSecundaria(primaria, secundaria) == True
    
    

    
    
    