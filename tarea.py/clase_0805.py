#Un programa que permita ingresar 10 números al usuario y al finalizar desplegar los elementos y en que posición de la lista están los mayores al promedio.
#ontador = 0
#suma = 0
#numeros = []
#for i in range (10):
#    numero = float(input("Ingrese un número: "))
#    numeros.append(numero)
#    suma = suma + numero

#promedio = suma / 10
#print(f"El promedio es: {promedio}")

#for i, numero in enumerate(numeros):
#    if numero > promedio:
#        print(f"El número {numero} está en la posición {i}")

#Ordenar ascendentemente una lista de tamaño 10 previamente poblada con números.(no puede ocupar el método sort de la lista)
#numeros = []
#for i in range(10):
#    numero = float(input("Ingrese un número: "))
#    numeros.append(numero)
#for i in range(len(numeros)):
#    for j in range(i + 1, len(numeros)):
#        if numeros[i] > numeros[j]:
#            numeros[i], numeros[j] = numeros[j], numeros[i]
#print("Números ordenados ascendentemente:")
#for numero in numeros:
#    print(numero)

#Poblar de forma automática una lista de tamaño 10 con los 1ros números primos(divisibles solo por 1 y por si mismo).
#def es_primo(num):
#    if num < 2:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True
#primos = []
#num = 2
#while len(primos) < 10:
#    if es_primo(num):
#        primos.append(num)
#    num += 1
#print("Los primeros 10 números primos son:")
#for primo in primos:
#    print(primo)

#def es_primo(numero):
#   divisibles = 0

#   for x in range(1, numero + 1):
#      if numero % x == 0:
#         divisibles = divisibles + 1

#   if divisibles == 2:
#      return True
#   else:
#      return False
   

#def los_primeros_numeros_primos(cuantos):
#   contar_primo = 0
#   n = 1
#   while contar_primo < cuantos:
#      if es_primo(n):
#         print(f"{n} es primo")
#         contar_primo = contar_primo + 1

#      n = n + 1

#los_primeros_numeros_primos(100)

#Desarolle una funcion que reciba 2 numeros como argumentos y retorne un True si esos dos numeros son amigos 
#la suma de los divisores del numero a y la suma de los divisores del numero b es igual a el numero a y el numero b respectivamente.
#(ejemplo: 220 y 284)

#def suma_divisores(numero):
#   suma = 0
#   for x in range(1, numero):
#      if numero % x == 0:
#         suma = suma + x
#   return suma

#Desarrolle una funcion que retorne el factorial de un numero dado por el usuario
#def factorial(numero):
#   if numero == 0 or numero == 1:
#      return 1
#   else:
#      return numero * factorial(numero - 1)
   
#Desarrrolle una funcion que reciba 2 listas y retorne 1 lista que contenga la suma cruzada
#def suma_cruzada(lista1, lista2):
#   if len(lista1) != len(lista2):
#      raise ValueError("Las listas deben tener la misma longitud")
#   resultado = []
#   for i in range(len(lista1)):
#      resultado.append(lista1[i] + lista2[i])
#   return resultado
#lista1 = [1, 2, 3]
#lista2 = [4, 5, 6]
#resultado = suma_cruzada(lista1, lista2)
#print("La suma cruzada de las listas es:", resultado)
