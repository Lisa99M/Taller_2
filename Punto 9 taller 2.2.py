#Hacer el ejercicio 7 del reto 1 empleando operaciones con vectores. Ejercicio 7: Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
def Crear_vector (elementos: float) -> list:

    v = [] #Crear un arreglo vacío para el vector
    for i in range (5): # Ciclo for para ingresar los elementos que formarán el vector
        elementos = float(input("Inserta elementos del vector: "))
        v.append(elementos)
    return v
if __name__ == "__main__":
    elementos = 0
    v = Crear_vector(elementos)
    print("Vector: " + str(v)) 
    
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
    print("La mediana es: " + str(v[2])) # Como el vector tiene 5 elementos la mediana será el valor que ocupe la tercera posición una vez ordenados estos de menor a mayor

#Ordenar los números de forma descendente
    v.sort(reverse = True) 
    print("Números ordenados de forma descendente: " + str(v))

#La potencia del mayor número elevado al menor número
    potencia: float = v[0]**v[4] #En este caso basado en el orden que se le dio al arreglo en el paso anterior se realiza la operación de potenciación indicando como base el primer elemento de la lista y como exponente el último
    print("Potencia del mayor número elevado al menor número: " +  str(potencia))

#La raíz cúbica del menor número
    raiz_cubica = v[4]**(1/3) # Como los números fueron ordenados de mayor a menor anteriormente, solo se debe hallar la raíz del último elemento en el arreglo
    print("Raíz cúbica del menor número: " + str(raiz_cubica))

    




