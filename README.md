# Taller_2

# Punto 7 
Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.


1. Para este punto se crea una funcion la cual nos permirira hallar las vocales que se encuentran en la cadena ingresada, se crean dos listas una vacia para almacenar los datos de vocales que se encuentren en la cadena, y otra para poder comprar y saber si son o no vocales.

2. Para encontrar y contar las vocales de la cadena se inicia un contador en cero de vocales, y se recorre con un ciclo for cada caracter de la cadena. Si el caracter  recorrido llega a ser una vocal, se agrega a la lista vacía Lista y se aumenta el contador de vocales. Si el contador de vocales alcanza o supera el valor de 2, significa que se han encontrado dos o más vocales y se retorna la lista de vocales encontradas. si no existen vocales en la cadena se imprimira no existe.


3. Para ejectuar el programa se pide ingresar la cadena la cual se evaluara por la funcion, y se evaluara si cumple con las condiciones establecidas, si cumple se imprimira que se encontraron dos o mas vocales.

![reto 8 3](https://user-images.githubusercontent.com/124607325/236600046-b078d008-aa9a-41cb-8e9a-8a17fc15a356.png)

## Codigo :


       def Hallar_vocales_cadena(Cadena) -> chr:
           Lista = []  # Se Crea una lista vacía para almacenar las vocales encontradas
           Lista_vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]  # se crea una lista con todas las vocales en minúsculas y mayúsculas para poder comparar.
    
           vocales = 0  # se inicia el contador de vocales a cero
          for caracter in Cadena:  #  se recorre con el ciclo for cada caracter en la cadena
               if caracter in Lista_vocales:  # Si el caracter es una vocal,  se agregara a la lista vacia y aumentar el contador de vocales
                   Lista.append(caracter)
                   vocales += 1
                   if vocales >= 2:  # Si se han encontrado dos o más vocales, retornar la lista de vocales y terminar la función
                      return Lista
    
           print("No existe")  # Si no se encontraron dos o más vocales,  se imprimir un mensaje de error
    

       if __name__ == "__main__":
           cadena = input("Ingrese la cadena: ")
           Lista = Hallar_vocales_cadena(cadena)  # se llama a la función Hallar_vocales_cadena() para buscar las vocales en la cadena
           if Lista:  # Si se encontraron dos o más vocales, imprimir la lista de vocales encontradas
                   print("Se encontraron dos o más vocales en la cadena "+str(cadena) +", estas son: "+ str(Lista))     
                   
                   
                   
                   
# Punto 8 

Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.

1. Para este punto se cran tres listas vacias las cuales almmacenaran datos durante el priceso, las dos primeras listas seran aquellas que llenaremos con los valores que queremos comparar, y la tercera lista que es la lista de diferencia sera la que guarda los valores que no estan en la segunda lista pero si en la primera.

![reto 8 1](https://user-images.githubusercontent.com/124607325/236601075-0dc3cf0e-087b-482b-b4ec-f5359aac9d0d.png)

2. Se define la función para hallar los elementos que no se encuentran. Dentro de la función, se recorre con un ciclo for cada elemento de la lista 1 y se verifica si ese elemento no está en la lista 2. Si el elemento no está en la ista 2, se agrega a la lista Diferencia, y se devuelve la lista Diferencia con los elementos de la primera lista que no están en la segunda lista.

![reto 8 2](https://user-images.githubusercontent.com/124607325/236601699-2af4b1d5-0ba8-4bc4-8352-4d1625ccf97c.png)

3. Para ejecutar se pide ingresar el tamaño y los elementos de la lista 1 y 2. Luego, se llama a la función hallar_elemento() para obtener la lista de diferencia y se imprime la lista 1, la lista 2 y la lista de diferencia. 

![reto 8 3](https://user-images.githubusercontent.com/124607325/236601754-b6650f91-ba0b-4e7c-a91e-69996571a644.png)



## Codigo

       lista1 = []  # se crea una lista 1 vacia a la cual se le agregaran los valores
       lista2 = []  # se crea una lista 2  vacia a la cual se le agregaran los valores
       Diferencia = []   # se crea una lista  vacia llamada diferencia a la cual se le agregaran los valores que no esten en la segunda lista

       # se crea una función que recibe dos listas como parámetros y devuelve una lista con los elementos de la primera lista que no están en la segunda lista
       def hallar_elemento(lista1, lista2):
           for i in lista1:  # Se recorre cada elemento de la lista 1
               if i not in lista2:  # Si el elemento no está en la lista 2, se agrega a la lista de diferencia
                   Diferencia.append(i)
           return Diferencia  # Se devuelve la lista de diferencia

       if __name__ == "__main__":
           n = int(input("tamaño de la lista: "))  # Se solicita el tamaño de la lista 1 al usuario
           for i in range(n):  # Se itera n veces para que el usuario ingrese n elementos a la lista 1
              valor = input(" ingrese elementos a la lista: ")
              lista1.append(valor)  # Se agrega el valor ingresado a la lista 1
    
          m = int(input("tamaño de la lista: "))  # Se solicita el tamaño de la lista 2 al usuario
           for i in range(m):  # Se itera m veces para que el usuario ingrese m elementos a la lista 2
               valor = input(" ingrese elementos a la lista : ")
               lista2.append(valor)  # Se agrega el valor ingresado a la lista 2
    
           diferencia = hallar_elemento(lista1, lista2)  # Se llama a la función hallar_elemento() para obtener la lista de diferencia
           print(" la lista 1 es " + str(lista1), " la lista dos es " + str(lista2))  # Se imprime la lista 1 y la lista 2
           print("Elementos en la primera lista que no están en la segunda lista son :")
           print(diferencia)  # Se imprime la lista de diferencia
