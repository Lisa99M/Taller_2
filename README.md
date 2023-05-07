# Taller-2

# Logo 

[![Atack-on-Codding-edited.jpg](https://i.postimg.cc/c47bzvy0/Atack-on-Codding-edited.jpg)](https://postimg.cc/jL5cwdSF)

# Punto 1 

Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

1. Para solucionar este punto lo primero que haremos será crear una función que separe los dígitos de un número recibido como parámetro. Esto lo conseguiremos convirtiendo el número a un dato tipo string y por medio de los ciclos for, recorriendo dicho número. En cada iteración del recorrido guradaremos cada dígito en una lista. Luego de tener la lista la retornaremos.

![image](https://user-images.githubusercontent.com/124721286/236653952-85d41bfa-f945-4d14-9954-5d4510492a47.png)

2. Por último asignaremos una función main en donde digitaremos el número y lo enviaremos como argumento a la función "digitosNumero". Al imprimir la lista, obtendremos cada dígito que compone al número

![image](https://user-images.githubusercontent.com/124721286/236653994-e0d5cc9e-3f5e-4474-bfc5-7fe8eee17798.png)


Codigo : 

    def digitosNumero(n:int) -> list:
    # Función que separa los dígitos que componen un número n recibido como parámetro 
    lista = [] # Creación de una lista vacia en donde se guardarán los dígitos que componen el número
    for i in str(n):  
        lista.append(i) # Separando los dígitos y agregandolos al final en la lista 
    return lista # Retorno de la lista con los digitos que componen al número

    if __name__ == "__main__":
        n = int(input("Ingrese un número entero: ")) # Ingreso del número entero 
        lista = digitosNumero(n) # Llamado de la función digitosNumero y envío del parámetro n 
        print("Los dígitos que componen al número son: "+str(lista)) # Impresión del resultado
       
       
# Punto 2 

Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

1. Para el desarrolo de este punto se define una función llamada "digitosNumero" que recibe un parámetro "n" , que es el número real que se desea descomponer en sus dígitos.![punto 2 2](https://user-images.githubusercontent.com/124607325/236652990-b5b8c071-a48a-40b7-ae50-de97ff769412.png)

2. Se crean dos listas vacías  "listaEntera" y "listaDecimal", que se utilizarán para almacenar los dígitos de la parte entera y decimal del número real "n". Y Se inicia  "bandera" en "True" para indicar que se está en la parte entera del número.
3. Se imprimen dos mensajes para mostrar como se divide el numero .

![punto 2 2](https://user-images.githubusercontent.com/124607325/236653026-b8cccaa2-4f53-431f-b66c-235392a4edd2.png)

4. Se crea un bucle "for", se verifica si la variable "bandera" es verdadera y si el carácter que se esta recorriendo en el bucle no es un punto decimal. Si ambas condiciones se cumplen, el carácter se agrega a la lista "listaEntera" utilizando la función "append()".

![punto 2 3](https://user-images.githubusercontent.com/124607325/236653063-879c4fe5-f7ae-413e-a353-43b3ceda4b68.png)


5. Si el carácter actual en el bucle es un punto decimal, la variable "bandera" se establece en "False" para indicar que se está en la parte decimal del número.

6. Si la variable "bandera" es falsa,  los dígitos se agregan a la lista "listaDecimal" utilizando la función "append()".

![Punto 2 4](https://user-images.githubusercontent.com/124607325/236653098-1d051a3b-ec9b-45fc-9020-4f726366ed1d.png)


7. Se imprimen las dos listas "listaEntera" y "listaDecimal" en líneas separadas para mostrar los dígitos de la parte entera y decimal del número, respectivamente.
![punto 2 5](https://user-images.githubusercontent.com/124607325/236653221-ba43e506-5c54-4d24-b547-20b58d96d05f.png)

8.  Se solicita ingresar un número real y se llama a la función "digitosNumero" para descomponer el número y mostrar sus dígitos.
![punto 2 6](https://user-images.githubusercontent.com/124607325/236653224-d9110547-bbd1-41b7-a241-92e1ed1ff0ad.png)


#### Codigo : 
        def digitosNumero(n:float):
        # Función que separa los dígitos de un número n recibido como parámetro, en su parte entera y su parte decimal

        listaEntera = [] # Creación de una lista vacia donde se guardarán los dígitos de la parte entera del número
        listaDecimal = [] # Creación de una lista vacia donde se guardarán los dígitos de la parte decimal del número
        bandera = True

        print("Los dígitos que componen al número son:") 
        print("PARTE ENTERA")

        for i in str(n):  
            if bandera and i != ".":
            listaEntera.append(i) # Separando los dígitos de la parte entera y agragandolos en el filan de la lista correspondiente 
            elif i == ".":
                bandera = False # Validando si nos encontramos en la parte decimal del número, en caso de serlo, obviar el punto
                continue
        
            if bandera == False:
                listaDecimal.append(i) # Separando los dígitos de la parte decimal y agregandolos en el final de la lista correspondiente
    
        print(listaEntera) # Impresión de los dígitos de la parte entera
        print("PARTE DECIMAL") 
        print(listaDecimal) # Impresión de los dígitos de la parte decimal 

         if __name__ == "__main__":
          n = float(input("Ingrese un número real: ")) # Ingreso del número entero
          digitosNumero(n) # Llamado de la función digitosNumero y envío del parámetro n 

# Punto 3 
Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
1. El primer paso srá crear una función que guarde los dígitos de dos números recibidos como praámetros en dos lista vacias, en donde a la primera se le ingresarán los dígitos al final de la lista por medio del método .append y la segunda se le agregarán los dígitos del segundo número al principio de la lista por medio del método .insert.   

![image](https://user-images.githubusercontent.com/124721286/236654095-f93c1073-5308-43bc-951c-eee1a95bab35.png)

2. En la misma función compararemos las listas. Si estas son iguales imprimiremos un mensaje indicando que los números son espejo, y si no son iguales indicaremos que los números no son espejo.

![image](https://user-images.githubusercontent.com/124721286/236654131-c29a613a-530f-44e4-ac03-24b17c4026a9.png)

3. Finalmente asignamos una función main en donde digitaremos los dos números y los enviaremos como parámetros a la función "numerosEspejos" a la cual también llamaremos. 

![image](https://user-images.githubusercontent.com/124721286/236654173-80e8055f-ddfd-443d-8e10-b7fb3dc97b65.png)


#### Código:
    def numerosEspejo(n1:int,n2:int):
    # Función que determina si dos números recibidos como parámtro son espejo uno del otro 
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

    if __name__ == "__main__":
        n1 = int(input("Ingrese el primer número entero: ")) # Ingreso del primer número
        n2 = int(input("Ingrese el segundo número entero: ")) # Ingreso del segundo número 
        numerosEspejo(n1,n2) # Llamado de la función numerosEspejo y envío de los parámetros n1 y n2 
        
        
# Punto 4
Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.

1. El primer paso será el de importar la libreria math de python.

![image](https://user-images.githubusercontent.com/124721286/236654386-42633384-c0e8-445a-a4a4-f49c5ad67f38.png)

2. Luego de esto definiremos una función la cual calculará la aproximación de la función coseno de un número x y haciendo uso de n terminos de la serie de Taylos (ambos datos recibidos como parámetros). Por medio del ciclo for programaremos una serie de Taylor la cual nos calculará una sumatoria y esta la retornaremos al finalizar el ciclo.

![image](https://user-images.githubusercontent.com/124721286/236654452-fec42159-cab1-47e0-87a8-5124e6af888c.png)

3. Como tercer paso crearemos una función que calcule los terminos que se necesitan para pasar los umbrales de error para un 10%, 1%, 0.1% y 0.001%. Esto mediante el ciclo while, en donde el error mientras sea mayor al error deseado, recalcularemos la sumatoria de la función pero haciendo uso de los terminos m que empiezan en 1 e irán aumentado de a uno hasta que se pase el umbral.

![image](https://user-images.githubusercontent.com/124721286/236654534-0a25a1fc-e880-48b9-84bc-9aaed165a01d.png)

4. Por último definimos un main en el cual ingresamos el número de terminos a usar y el valor de x. Haremos el llamado de las funciones y enviaremos sus correspondientes parámetros. 

![image](https://user-images.githubusercontent.com/124721286/236654573-cd75a962-7810-43b6-b368-5de54bffcc2d.png)


#### Código:
    import math # Importación de la libreria math de python 

    def aproximacion_coseno (x:float,n:int) -> float:
        # Función que realiza el cálculo aproximado de la función coseno para un número x recibido como parámetro y haciendo uso de n terminos también recibidos como parámetros
        sumatoria = 0
        for i in range (n):
            sumatoria += math.pow(-1, i) * (math.pow(x, 2*i)/ math.factorial(2*i)) # Serie de Taylor para la función coseno 
        return sumatoria  # Retorno del valor aproximado 

    def error_coseno(x:float,deseado:float):
      # Función que calcula el error entre el valor real y el aproximado de la función coseno para un número x recibido como parámetro y devuelve el número de términos que deden usarlse para conseguir un error deseado (también recibido como parámetro)
      m = 1 # Se inicia con 1 termino 
      error = 100 # Se inicia con un error del 100 % 
      while error >= deseado: # Mientras que el error supere al deseado aumentaremos los términos de uno uno y realizaremos el cálculo de la aproximación del coseno con el nuevo termino conseguido
         error = abs((math.cos(x) - aproximacion_coseno(x,m)) / math.cos(x)) * 100 
         m += 1
      print("\nEs necesario usar "+str(m-1)+" terminos para obtener un error del "+str(deseado)+" %")

    if __name__ == "__main__":
      n = (int(input("Número de términos de la serie de Maclaurin: "))) # Ingreso del número de terminos que usaremos inicialmente para calcular el valor aproximado de la función coseno 
      x = (float(input("\nValor real para calcular la aproximación de la función coseno alrededor de 0: "))) # Ingreso del número al cual calcularemos el valor aproximado de la función coseno
      sumatoria = aproximacion_coseno (x, n) # Llamado de la función aproximación_coseno y envío de los parámetros x y n 
      print("\nResultado usando la función creada: "+ str(sumatoria))
      print("\nResultado usando la función importada de math: "+ str(math.cos(x))) 
      diferencia = abs(math.cos(x) - sumatoria) # Cálculo de la diferencia entre el valor real y el valor aproximado 
      print("\nLa diferencia entre el valor real y la aproximación es: " + str(diferencia))

      error_coseno(x,10) # LLamado de la función error_coseno y envío de los parámetros x y 10 
      error_coseno(x,1) # LLamado de la función error_coseno y envío de los parámetros x y 1
      error_coseno(x,0.1) # LLamado de la función error_coseno y envío de los parámetros x y 0.1 
      error_coseno(x,0.001) # LLamado de la función error_coseno y envío de los parámetros x y 0.001

# Punto 5
Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.

1.En este punto primero se abordó el cálculo del mcm desde la perspectiva iterativa. Se crea una función que recibirá como parámetros os números a los q se les desea calcular el mcm y la cantidad de iteraciones (estas estarán dadas por la comparación del mayor entre ambos números). En cada iteración se divide i entre x y y, usando un condicional se determina que i es múltiplo de ambos números si su módulo es cero al dividir entre ambos números, de lo contrario se suma uno a i y continúa el ciclo. Al finalizar la función retorna el valor final de i.

[![recursiva.png](https://i.postimg.cc/GppYC54q/recursiva.png)](https://postimg.cc/QFRVgSkT)

2.Desde la perspectiva recursiva igualmente se define la función, que va a recibir los mismos parámetros mencionados anteriormente. Luego planteamos un caso base en que x o y es igual a uno. Se plantea el condicional de que si el módulo de i entre x y y es cero entonces i es múltiplo, de lo contrario se altera el valor de i en 1.

[![recursiva.png](https://i.postimg.cc/GppYC54q/recursiva.png)](https://postimg.cc/QFRVgSkT)

3.El usuario podrá seleccionar cuál de las funciones desea utilizar para lo cual podrá elegir las opciones uno o dos definidas en la función principal como True. Si no ingresa una opción válida se imprimirá un mensaje.

[![image-3.png](https://i.postimg.cc/ZqDNKx3Z/image-3.png)](https://postimg.cc/f3my8XBg)



#### Código:
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
    

# Punto 6
Desarrollar un programa que determine si en una lista no existen elementos repetidos.

1. El primer paso para este punto crear una función con la cual haremos nuestra lista. Creamos una lista vacía y en la variable t almacenamos el número de datos que deseamos tenga la lista. Luego a partir de un ciclo for los elementos son ingresados en la lista.
![Punto 6 1](https://user-images.githubusercontent.com/124607325/236653670-4a33b6fd-2ba2-4d4d-a59c-ee3d4bf4a6bc.png)

2. Ya con la lista creada con otro ciclo for la recorremos y con la función integrada cunt() obtendremos el número de cada elemento.
![punto 6 2](https://user-images.githubusercontent.com/124607325/236653632-92196dc0-12e7-49f2-a447-c24261926239.png)

3. Establecemos una bandera q en caso de ser igual a uno el programa imprimirá que no hay elementos repetidos en la lista, de lo contrario imprimirá que existen elementos repetidos.
![punto 6 3](https://user-images.githubusercontent.com/124607325/236653663-4e24ca45-657a-45bb-a59a-d361783ac2ba.png)


#### Código:
        
    def Creador_listas (n: str) -> list: #Funcion para crear la lista a examinar. 
        lista = []
    
        for i in range(t): #Ciclo for para ingresar los elementos de la lista.
            n = input("Ingresar elementos de la lista: ")
            lista.append(n)
        return lista

    if __name__ == "__main__": #Función principal con variables definidas.
        n = 0
        t = int(input("Insertar tamaño deseado para la lista: "))
        lista_creada = Creador_listas (n)#Llamando a la función que creamos para hacer la lista. 
        print(lista_creada)

        for i in lista_creada :
            if lista_creada.count(i) == 1:
               bandera = True
            else:
                bandera = False
        if bandera == True:
            print("En la lista " + str(lista_creada) + " no hay elementos repetidos")
        else:
            print("En la lista " + str(lista_creada) + " existen elementos repetidos")
            
# Punto 7 

Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.


1. Para este punto se crea una funcion la cual nos permirira hallar las vocales que se encuentran en la cadena ingresada, se crean dos listas una vacia para almacenar los datos de vocales que se encuentren en la cadena, y otra para poder comprar y saber si son o no vocales.
![reto 8 1](https://user-images.githubusercontent.com/124607325/236600027-4b48f2f2-7eb7-4937-b65d-295c9bde430c.png)


2. Para encontrar y contar las vocales de la cadena se inicia un contador en cero de vocales, y se recorre con un ciclo for cada caracter de la cadena. Si el caracter  recorrido llega a ser una vocal, se agrega a la lista vacía Lista y se aumenta el contador de vocales. Si el contador de vocales alcanza o supera el valor de 2, significa que se han encontrado dos o más vocales y se retorna la lista de vocales encontradas. si no existen vocales en la cadena se imprimira no existe.

![reto 8 2](https://user-images.githubusercontent.com/124607325/236600032-34a47994-6450-40ee-9bcf-54927c83018a.png)


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
           
 # Punto 9
 Resolver el punto 7 del taller 1 usando operaciones con vectores.
 
 1. En este punto lo primero que hicimos fue una función para crear el vector con 5 elementos.
![9 1 ](https://user-images.githubusercontent.com/124607325/236654825-494f3418-41b7-45f9-a519-c5ed3f5a8959.png)

 2. Llamamos a nuestra función

 3. Para el promedio utilizamos la función sum() para conocer la sumatoria de los números y luego dividimos entre 5
 ![9 2](https://user-images.githubusercontent.com/124607325/236654832-34f9b518-1a76-4bbd-b2bb-31a34be1d75d.png)


 4. Para el promedio multiplicativo empleamos un ciclo for para multiplocar todos números del vector. Luego le hallamos la ríz quinta al resultado.
 ![9 3](https://user-images.githubusercontent.com/124607325/236654860-6bf0ebe4-eca1-43a3-8251-732ff1aafaa4.png)


 5. Con la función sort() organizamos los elementos e orden ascendente, con los números organizados de esta manera imprimimos el número que ocupa la posición dos que sería el elemento cetral y por tanto la mediana.
![9 3](https://user-images.githubusercontent.com/124607325/236654896-2f9980c7-dd81-4c11-8b14-1abf63cffa5a.png)


 6. Utilizando reverse los reorganizamos en orden descendente.
 ![9 5](https://user-images.githubusercontent.com/124607325/236654918-2cd18976-a9fc-40f0-b106-9f25f3c2529e.png)


 7. Con los elementos organizados de esta manera ubicamos el menor, que corresponderá al índice [5-1], o sea estará ubicado de último mientras q el índice cero será el mayor. Elevamos el mayor número a la potencia del menor.
 ![9 6](https://user-images.githubusercontent.com/124607325/236654935-65a670f5-7c5a-49aa-a2bd-e1a24b46dda0.png)


 8. Con esta misma lógica al menor número se le halla la raíz cuadrada elevándolo a la 1/3.
 ![9 7](https://user-images.githubusercontent.com/124607325/236654944-f16f18e2-8666-4da9-a888-63ef824ae9f0.png)
 
 #### Código:
    v = [] #Crear un arreglo vacío para el vector
    for i in range (5): # Ciclo for para ingresar los elementos que formarán el vector
        elementos = int(input("Inserta elementos del vector: "))
        v.append(elementos)
    print(v)

    #El promedio
    sumatoria = sum(v) #Es la suma de todos los elementos del vector dividido entre la cantidad de elementos. Se utiliza la función sum() 
    promedio = sumatoria/5
    print("El promedio es: " + str(promedio))

    #El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
    mult = 1
    for i in v:#Ciclo for para multiplicar todos los elementos dentro del arreglo y luego se halla la raíz 5ta, ya que son 5 operandos.
        mult *= i 
        promedio_multiplicativo = mult**(1/5)
    print("El promedio multiplicativo es:" + str(promedio_multiplicativo))

    # Ordenar los números de forma ascendente
    v.sort()
    print("Números ordenados de forma ascendente: " + str(v))

    #La mediana
    print(v[3]) # Como el vector tiene 5 elementos la mediana será el valor que ocupe la tercera posición una vez ordenados estos de menor     a mayor

    #Ordenar los números de forma descendente
    v.sort(reverse = True) 
    print("Números ordenados de forma descendente: " + str(v))

    #La potencia del mayor número elevado al menor número
    potencia: float = v[0]**v[4] #En este caso basado en el orden que se le dio al arreglo en el paso anterior se realiza la operación de     potenciación indicando como base el primer elemento de la lista y como exponente el último
    print("Potencia del mayor número elevado al menor número: " +  str(potencia))

    #La raíz cúbica del menor número
    raiz_cubica = v[4]**(1/3) # Como los números fueron ordenados de mayor a menor anteriormente, solo se debe hallar la raíz del último       elemento en el arreglo
    print("Raíz cúbica del menor número: " + str(raiz_cubica))

# Punto 10
Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.

1. El primer paso será crear una función la cual realizará el llenado de la matriz de tamaño n, el cual será asignado por el usuario y se enviará como parámetro a la función. Primero se hará el llenado de las filas, donde cada elementos se guradará en la variable "num" y se utilizará el método .append para agregar este valor al final de la lista. Después de esto agregaremos cada fila a nuestra matriz haciendo nuevamente uso del método append. La función retornará la matriz creada. 

![image](https://user-images.githubusercontent.com/124721286/236654786-29fa9511-6619-45dc-ada1-ecbae1c0650c.png)

2. En el segundo paso, crearemos otra función la cual tendrá como objetivo imprimir la matriz anteriormente llenada y recibida como parámetro en esta nueva función. Imprimiremos fila por fila de la matriz haciendo uso del ciclo for; esto para que al momento de imprimirse se pueda visualizar como una matriz. 

![image](https://user-images.githubusercontent.com/124721286/236654796-a375c0a4-e0f3-4cb1-97fa-13a561290f27.png)

3. Como tercer paso lo que haremos será crear una nueva función que determine si la matriz ingresada anteriormente, es una matriz mágica, esto se consigue realizando la suma de cada una de las filas, columnas, la diagonal principal y la diagonal secundaria. Si cada una de estas sumas nos da como resultado el valor de n * ( n ^ 2 + 1 ) // 2 siendo n el tamaño de la matriz (La cual debe ser cuadrada y no tener elementos repetidos), podremos decir que la matriz es mágica. En caso de que todas las sumas den como resultado el valor anteriormente mencionado, retornaremos una variable bandera como True. Y en caso de no serlo retornaremos una variable bandera como False. 

![image](https://user-images.githubusercontent.com/124721286/236654807-a2682481-9ee1-4c38-916e-a8d931991296.png)

4. Posteriormente crearemos una nueva función que determinará si en la matriz existen elementos repetidos, esto, guardando todos los elementos en una lista y luego verificando que cada uno de los elementos se encuentre solo una vez en dicha lista haciendo uso del método .count. Si efectivamente solo se encuentran una vez, existe la posibilidad de que la matriz sea mágica y retornaremos una variable bandera como True; Sin embargo, si al menos un elemento se repite en la lista podremos decir que la matriz no es mágica y retornaremos una variable bandera como False.

![image](https://user-images.githubusercontent.com/124721286/236654818-66ccf3ed-bf36-44de-9733-8314b6f380d6.png)

5. Por último, definiremos una función main en donde asignaremos el tamaño de la matriz, para luego enviar este valor como parámetro a las funciones correspondientes. Realizaremos el llamado de las 4 funciones creadas y haremos las validacionesde las banderas retornadas por las funciones "matrizMagica" y "elementosRepetidos". En caso de que ambas banderas sean verdaderas mostraremos unmensaje indicando que la matriz ingresada es mágica. En caso de que la bandera de "matrizMagica" sea falsa pero la bandera de "elementosrepetidos" sea verdadera, mostraremos un mensaje indicando que la matriz ingresada no es mágica. Y, en caso de que la bandera de "elementosRepetidos" sea falsa mostraremos que la matriz no es mágica debido a que existen elementos repetidos

![image](https://user-images.githubusercontent.com/124721286/236654828-b1328ff3-b55d-420c-957b-51c74eba9fd6.png)

#### Código:
    def crearMatriz(n:int) -> list:
        # Función que realiza el llenado de una matriz cuadrada de tamaño n recibido como parámetro 
        matriz = [] # Creación de la matriz a la cual se le agregarán las fulas con los elementos 
        fila = [] # Creación de la fila en donde agregaremos los elementos 
        for i in range(n):
            for j in range(n):
                num = float(input("Ingrese el elemento ["+str(i+1)+"]["+str(j+1)+"] : ")) # Ingreso de los elementos que compondrán a las         filas y despues a la matriz
                fila.append(num) # Adición de cada uno de los elementos al final de la fila 
            matriz.append(fila) # Adición de cada fila al final de la matriz
            fila = [] # Vaciado de la fila para que pueda volver a ser llenada
        return matriz # Retorno de la matriz creada
    def imprimirMatriz(n:int,matriz:list):
        # Función que imprime las filas de una matriz recibida como parámetro de tamaño n también recibido como parámetro
        for i in range(n): print(matriz[i]) # Impresión de cada fila de la matriz
    def matrizMagica(n:int,matriz:list) -> bool:
        # Función que realiza la sumatoria de las filas, columnas y diagonales de una matriz recibida como parámetro y comprueba si cada           suma es igual a n * ( n ** 2 + 1 ) // 2 siendo n el tamaño de la matriz recibido como parámetro 
        sumaFilas = 0 
        sumaColumnas = 0 
        sumaDiagonal1 = 0 
        sumaDiagonal2 = 0 
        bandera = True 
        sumaMagica = n * ( n ** 2 + 1 ) // 2 # Formula que indica el resultado que debe tener cada suma de filas, columnas y diagonales           para que la matriz se considere como mágica
        for i in range(n):
            for j in range(n):
                sumaFilas = sumaFilas + matriz[i][j] # Cálculo de la sumatoria de cada una de las filas de la matriz
            if sumaFilas != sumaMagica: # Comparación del resultado de la suma de filas con el valor que debería ser para que se considere             la matriz como mágica
                bandera = False
                break 
            sumaFilas = 0
        for i in range(n):
            for j in range(n):
                sumaColumnas = sumaColumnas + matriz[j][i] # Cálculo de la sumatoria de cada una de las columnas de la matriz
            if sumaColumnas != sumaMagica: # Comparación del resultado de la suma de filas con el valor que debería ser para que se                   considere la matriz como mágica
                bandera = False
                break
            sumaColumnas = 0 
    
        for i in range(n):
            for j in range(n):
                if i == j:
                    sumaDiagonal1 = sumaDiagonal1 + matriz[i][j] # Cálculo de la sumatoria de la diagonal principal de la matriz
        if sumaDiagonal1 != sumaMagica: # Comparación del resultado de la suma de filas con el valor que debería ser para que se considere         la matriz como mágica
            bandera = False
        for i in range(n):
            sumaDiagonal2 = sumaDiagonal2 + matriz[i][n-i-1] # Cálculo de la sumatoria de la diagonal secundaria de la matriz
        if sumaDiagonal2 != sumaMagica: # Comparación del resultado de la suma de filas con el valor que debería ser para que se considere         la matriz como mágica
            bandera = False
        return bandera 
    def elementosRepetidos(n:int,matriz:list) -> bool:
        # Función que comprueba si los elementos ingresados en un matriz recibida como parámetros se repiten  
        repetidos = [] # creación de una lista vacia a la cual ingresaremos los datos de la matriz y comprobaremos si sus elementos se             repiten 
        for i in range(n): 
            for j in range(n):
                 repetidos.append(matriz[i][j]) # Ingreso de los elementos de la matriz a la lista 
        for i in repetidos:
            if repetidos.count(i) == 1: # Validación de que cada elemento en la lista exista solo una vez, en caso de serlo bandera = True         y en caso de no serlo bandera = False
                bandera = True
            else: 
                bandera = False 
                break
        return bandera # Retorno del valor de bandera 
    
    if __name__ == "__main__":
        n = int(input("Ingrese el tamaño de la matriz: ")) # Ingreso del tamaño que tendrá la matriz (para que pueda ser mágica debe ser           cuadarada)
        matrizM = crearMatriz(n) # Llamado de la función crearMatriz y envío del parámetro n 
        print("\nMATRIZ INGRESADA") 
        imprimirMatriz(n,matrizM) # Impresión de la matriz haciendo el llamado de la función imprimirMatriz y envío de los parámtros n y           matrizM
        magica = matrizMagica(n,matrizM) # Comprobación de que la matriz sea mágica haciendo el llamado de la función matrizMagica y envio         de los parámetros n y matrizM
        elementos = elementosRepetidos(n,matrizM) # Comprobación de que no existan elementos repetidos en la matriz haciendo el llamado de         la función elementosRepetidos y envio de los parámetros n y matrizM
        if elementos == True: # Validación de que no existan elementos repetidos en la matriz, en caso de que si se repitan, la matriz no         podrá ser mágica
            if magica == True: # Validación de que la matriz sea mágica 
                print("\nLa matriz ingresada es mágica")
            else:
                print("\nLa matriz ingresada no es mágica")
        else:
            print("\nLa matriz ingresada no es mágica debido a que hay elementos repetidos")
