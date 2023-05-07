# Punto 7

##  Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.

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
    