''' 
    Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}

    Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
    Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
'''

def intersección_conjuntos(vocales, alfabetoSinVocales):
    
    ''' Calcula la intersección de dos conjuntos '''
    
    caracteresComunes = vocales & alfabetoSinVocales
    return caracteresComunes

if __name__ == "__main__":
    #Entrada
    vocales = {'a', 'e', 'i', 'o', 'u'}
    alfabetoSinVocales = set('bcdfghjklmnpqrstvwxyz')

    #Proceso
    caracteresComunes = intersección_conjuntos(vocales, alfabetoSinVocales)

    #Salida
    print("Letras Comunes:", caracteresComunes) #Conjunto vacío.    

