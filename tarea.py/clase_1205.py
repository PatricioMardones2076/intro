#Desarrolle una funcion, y la funcion recibe un argumento. La funcion retornara un True si el numero que recibio es un numero perfecto
def es_numero_perfecto(numero):
    if numero < 1:
        return False
    
    suma_divisores = sum(i for i in range(1, numero) if numero % i == 0)
    
    return suma_divisores == numero
numero = int(input("Ingrese un número para verificar si es perfecto: "))
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
    print(True)
else:
    print(f"{numero} no es un número perfecto.")
    print(False)
