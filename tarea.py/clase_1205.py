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

#Que los primeros 5 numeros sean perfectos  

#def es_perfecto(num):
#    suma = 0

#    for i in range(1, num , 1):
#        if num % i == 0:
#            suma = suma + i

#    if suma == num:
#        return True
#    else:
#        return False

#def primeros_perfectos(n: int):
#   mis_perfectos = []
#   numero = 1
#   cont = 1
#   while cont <= 5:
#      print(numero)
#      if es_perfecto(numero):
#         mis_perfectos.append(numero)
#         cont = cont + 1

#      numero = numero + 1

#   return mis_perfectos

#Las funciones nunca retorna print, nos sirve como traza
# Siempre vamos a retornar una variable tipo str
# Nunca una funcion debe incluir un input

