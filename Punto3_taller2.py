'''
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
'''

if __name__ == "__main__":

    n1 = int(input("Ingrese el primer número entero: ")) # Ingreso del primer número
    n2 = int(input("Ingrese el segundo número entero: ")) # Ingreso del segundo número 
    
    lista1 = [] # Creación de la primera lista en donde guardaremos los dígitos del primer número al final de la lista  
    lista2 = [] # Creación de la segunda lista en donde guardaremos los datos del segundo número al principio de la lista 

    for i in str(n1):
        lista1.append(i) # Adición de los dígitos del primer número al final en la lista
    for i in str(n2): 
        lista2.insert(0,i)  # Adición de los dígitos del segundo número al principio en la lista 

    if lista1 == lista2: # Validación de la igualdad de las 2 listas, en caso de ser iguales los números se considerarán como espejo y en caso de no serlo no se considerarán como espejo
        print("Los números son espejo")
    else:
        print("Los números no son espejo")
