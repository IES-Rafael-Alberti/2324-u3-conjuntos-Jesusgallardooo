''' 
    Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
    la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). 
    Ejemplo:

[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]

    Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
    retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. Notar que cada 
    cliente puede haber hecho más de una compra en el mes, por lo que la función debe retornar una estructura 
    que contenga cada domicilio una sola vez.
'''

def facturar_compras(compras):
    
    ''' 
        Crea una cadena vacía para almacenar en ella cada dato de la factura
        para cada cliente.
    '''
    
    mensaje = ""

    for compra in compras:
        
        ''' 
            Recorre cada compra almacenada en la lista compras, clasificando sus
            4 componentes en una variable distinta, para luego crear un mensaje con
            La información de la factura correspondiente. 
        '''
        
        cliente = compra[0]
        dia = compra[1]
        monto = compra[2]
        domicilio = compra[3]

        mensaje = mensaje + "Nombre del cliente: " + cliente + "\n"
        mensaje = mensaje + "Día del mes: " + str(dia) + "\n"
        mensaje = mensaje + "Monto: " + str(monto) + "\n"
        mensaje = mensaje + "Domicilio: " + domicilio + "\n"
        mensaje = mensaje + "____________________________________\n\n"

    return mensaje

if __name__ == "__main__":
    #Entrada
    compras = [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
        ("Jorge Russo", 15, 958, "Mirasol 218")]
    
    #Proceso
    facturasCompras = facturar_compras(compras)
    
    #Salida
    print(facturasCompras)