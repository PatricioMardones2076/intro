#Desarrolle una funcion, y la funcion recibe un argumento. La funcion retornara un verdadero si el numero que recibio es un numero perfecto
def es_numero_perfecto(numero):
    suma = 0
    for x in range (1, numero):
        if numero % x == 0:
            suma = suma + x
    return suma == numero
# Solicitar al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
# Verificar si el número es perfecto y mostrar el resultado
if es_numero_perfecto(numero):
    print(f"{numero} es un número perfecto.")
else:    print(f"{numero} no es un número perfecto.")
# Ejemplo de uso
print(es_numero_perfecto(6))  # Debería retornar True, ya que 6 es un número perfecto (1 + 2 + 3 = 6)
