'''
    El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.

    ejemplo, el conjunto potencia de {1,2,3} es:

    {∅,{1},{2},{3},{1,2},{1,3},{2,3},{1,2,3}}

    Escriba la función conjunto_potencia(s) que reciba como parámetro un conjunto cualquiera s y 
    retorne su «lista potencia» (la lista de todos sus subconjuntos):

     conjunto_potencia({6, 1, 4})
[set(), set([6]), set([1]), set([4]), set([6, 1]), set([6, 4]), set([1, 4]), set([6, 1, 4])]

    TRUCO --> FROZENSET()

'''

def conjunto_potencia(s):
    
    '''Genera y devuelve el conjunto potencia de un conjunto dado.'''
    
    potencia = [set()]  # Inicializa el conjunto vacío
    
    for elemento in s:
        # Para cada elemento en s, genera nuevos subconjuntos
        subconjuntos = []
        
        for subconjunto in potencia:
            # Añade la unión de cada subconjunto con el elemento en la lista subconjuntos[]
            subconjuntos.append(subconjunto | {elemento})   
        
        # Concatena los nuevos subconjuntos a la lista potencia (conjunto vacío creado anteriormente)
        potencia = potencia + subconjuntos
    
    return potencia # Devuelve la lista potencia que guarda cada subconjunto

if __name__ == "__main__":
    #Entrada
    s = {9, 2, 8}
    
    #Proceso
    resultado = conjunto_potencia(s)
    
    #Salida
    print(resultado)