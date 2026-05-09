#for x in range(3,14,2):
#print(x) 

import time


#while True:
#   for h in range(0, 24, 1):
#      for m in range(0, 60, 1):
#         for s in range(0, 60, 1):
#            print(h, ":", m, ":", s)
            #time.sleep(0.000000002)

#Desarrolle un prgrama que permita ingresar 5 numeros y al finalizar desplegar cuantos numeros pares ingreso el usuario
#Solo se deben considerar numeros positivos
#usando ciclo for
contador_pares = 0
contador_numeros = 0
for _ in range(5):
    numero = int(input("Ingrese un número positivo: "))
    if numero > 0:
        if numero % 2 == 0:
            contador_pares += 1
        contador_numeros += 1
    else:  
        print("Por favor, ingrese un número positivo.")    
print("Cantidad de números pares ingresados:", contador_pares)  
