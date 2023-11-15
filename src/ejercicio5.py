''' 
    Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

    Crea un conjunto pares que contenga los números pares del conjunto numeros.
    Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
    Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
'''

def calcular_pares_de_un_conjunto(numeros):
    numerosPares = numeros & set(range(2, 11, 2)) # (2 = inicio, 11-1 = 10 = final, 2 = pasos)

    return numerosPares

def calcular_multiplosde3_de_un_conjunto(numeros):
    multiplosDeTres = numeros & set (range(3,11,3)) # (3 = inicio. 11-1 = 10 = final, 3 = pasos)
    return multiplosDeTres

def intersección_Pares_MultiplosdeTres(numerosPares, multiplosDeTres):
    paresMultiplosDeTres = numerosPares & multiplosDeTres
    return paresMultiplosDeTres

if __name__ == "__main__":
    #Entrada
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    paresMultiplosDeTres = {}
    
    #Proceso
    numerosPares = calcular_pares_de_un_conjunto(numeros)     
    multiplosDeTres = calcular_multiplosde3_de_un_conjunto(numeros) 
    paresMultiplosDeTres = intersección_Pares_MultiplosdeTres(numerosPares, multiplosDeTres)
    
    #Salida
    print ("numeros pares = " + str(numerosPares))
    print ("Multiplos de 3 = " + str(multiplosDeTres))
    print("Pares multiplos de 3 = " + str(paresMultiplosDeTres))