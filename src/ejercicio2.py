''' 
        Solicitar al usuario que introduzca los nombres de pila de los alumnos de primaria de una escuela, 
        finalizando cuando se introduzca “x”. A continuación, solicitar que introduzca los nombres de los 
        alumnos de secundaria, finalizando al introducir “x”.

        Mostrar los nombres de todos los alumnos de primaria y los de secundaria, sin repeticiones.
        Mostrar qué nombres se repiten entre los alumnos de primaria y secundaria.
        Mostrar qué nombres de primaria no se repiten en los de nivel secundaria.
        Mostrar si todos los nombres de primaria están incluidos en secundaria.
'''

def obtener_nombres():
    nombres = []
    nombre = input("Introduce el nombre de un alumno (o 'x' para finalizar): ")
    while nombre.lower() != 'x':
        nombre = input("Introduce el nombre de un alumno (o 'x' para finalizar): ")
        nombres.append(nombre)
    nombres.remove("x") 
    return set(nombres)

def nombres_repetidos(primaria, secundaria):
    nombresRepetidos = primaria.intersection(secundaria)
    return nombresRepetidos

def nombres_no_repetidos(primaria, secundaria):
    nombresNoRepetidos = primaria.difference(secundaria)
    return nombresNoRepetidos

def nombresPrimaria_incluidosEn_nombresSecundaria(primaria, secundaria):
    todosLosNombresDePrimariaIncluidos = primaria.issubset(secundaria)
    return todosLosNombresDePrimariaIncluidos

if __name__ == "__main__":
    #Entrada
    print("Introduce los nombres de los alumnos de primaria:")
    
    #Proceso
    nombres_primaria = obtener_nombres()

    #Entrada
    print("\nIntroduce los nombres de los alumnos de secundaria:")
    
    #proceso
    nombres_secundaria = obtener_nombres()

    primaria = set(nombres_primaria)
    secundaria = set(nombres_secundaria)
    
    
    #Salida
    print("\nNombres de primaria: ")
    print(primaria)
    
    print("\nNombres de secundaria: ")
    print(secundaria)
    
    print("\nNombres que se repiten entre primaria y secundaria: ")
    nombresRepetidos = nombres_repetidos(primaria, secundaria)
    print(nombresRepetidos)
    
    print("\nNombres de primaria que no se repiten en secundaria: ")
    nombresNoRepetidos = nombres_no_repetidos(primaria, secundaria)
    print(nombresNoRepetidos)
    
    
    todosLosNombresDePrimariaIncluidos = nombresPrimaria_incluidosEn_nombresSecundaria(primaria, secundaria)
    #dividir en un if X = true, Sí... para que no aparezca true y aparezca el mensaje 
    print(todosLosNombresDePrimariaIncluidos)

    