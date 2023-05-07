'''
Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
'''
def minimoComunMultiploIterativo(x:int,y:int,iterador:int) -> int:
    # Función que calcula el mínimo común multiplo de dos números recibidos como parámetros por medio de las iteraciones 
    i = iterador # Inicialización de un iterador que comienza desde el número mayor entre x y 
    bandera = True
    while bandera:
        if i % x == 0 and i % y == 0: # Validación de que el número i sea multiplo de ambos números, en caso de sero bandera = False y en caso de no serlo i aumentará de 1 en uno 
            bandera = False
        else: 
            i += 1
    return i # Retorno del valor i 

def minimoComunMultiploRecursivo(x:int,y:int,iterador:int) -> int:
    # Funcion que calcula el mínimo común multiplo de dos números recibidos como parámetros por medi de la recursividad 
    i = iterador # Inicialización de un iterador que comienza desde el número mayor entre x y 
    if x == 1 or y == 1: # Caso base para no entrar en un bucle infinito, se trata del caso de cuando x o y es uno, en este caso el mcm se calcula realizando x * y
        return x * y
    elif i % x == 0 and i % y == 0: # Validación de que el número i sea multiplo de ambos números, en caso de sero se retorna el valor de i y se llamará a la función pero alterando el parámetro de "iterador" en uno 
        return i
    else: 
        return minimoComunMultiploRecursivo(x,y,iterador+1)

if __name__ == "__main__":
    x = int(input("Ingrese el número 1 : ")) # Ingreso del primer número entero
    y = int(input("Ingrese el número 2 : ")) # Ingreso del segundo número entero 
    lista = [x,y] # Creación de una lista en donde se guardarán los valores de x y y
    iterador = max(lista) # Asignación del valor de iterador, el cual será el número mayo entre x y 
    bandera = True
    while bandera or op != 1 and op != 2: # Ciclo do while que valida que se esté ingresando la opción correcta 
        bandera = False 
        op = int(input("Ingrese la opción que desea ejecutar \n1. Calculo del mcm con iteraciones \n2. Calculo del mcm con recursividad \n")) # Ingreso de la opción que el usuario desea ejecutar 
        if op != 1 and op != 2: # Mostrar mensaje en caso de que la opción ingresada no sea correcta
            print("La opción ingresada no es válida")
    if op == 1: # Caso en donde se desea calcular el mcm haciendo uso de la función iterativa 
        mcm = minimoComunMultiploIterativo(x,y,iterador) # Llamado de la función minimoComunMultiploIterativo y envío de los parámetros x, y, iterador
        print("El mínimo comun múltiplo calculado con iteraciones entre "+str(x)+" y "+str(y)+" es: "+str(mcm))
    else: # Caso en donde se desea calcular el mcm haciendo uso de la función recursiva
        mcm = minimoComunMultiploRecursivo(x,y,iterador) # Llamado de la función minimoComunMultiplorecursivo y envío de los parámetros x, y, iterador
        print("El mínimo comun múltiplo calculado con recursividad entre "+str(x)+" y "+str(y)+" es: "+str(mcm))
    