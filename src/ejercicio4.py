''' 
    Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
    Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
    Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
    Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
'''
def diferencia_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto1 - conjunto2
    return diferencia



def intersección_Frutas(setFrutas1, setFrutas2):
    frutasComunes = setFrutas1 & setFrutas2
    return frutasComunes

if __name__ == "__main__":
    #Entrada
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]

    #Proceso
    setFrutas1 = set(frutas1)
    setFrutas2 = set(frutas2)
    
    frutasComunes = intersección_Frutas(setFrutas1, setFrutas2)
    
    frutasSoloEnFrutas1 = diferencia_conjuntos(setFrutas1, setFrutas2)
    frutasSoloEnFrutas2 = diferencia_conjuntos(setFrutas2,setFrutas1)
    
    #Salida
    print("Frutas que estan en ambos conjuntos: " + str(frutasComunes)) 
    print("Frutas que estan solo en el 1er conjunto: " + str(frutasSoloEnFrutas1)) 
    print("Frutas que estan solo en el 2do conjunto: " + str(frutasSoloEnFrutas2)) 
    
    