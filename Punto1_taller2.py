#Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

n = int(input("Ingrese un número entero: ")) # Ingreso del número entero 

lista = [] # Creación de una lista vacia en donde se guardarán los dígitos que componen el número

for i in str(n):  
    lista.append(i) # Separando los dígitos y agregandolos al final en la lista 
 
print("Los dígitos que componen al número son: "+str(lista)) # Impresión del resultado