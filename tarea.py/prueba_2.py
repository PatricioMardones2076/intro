#Desarrolle un programa que permita ingresar la estatura y peso de una persona, debe dividir el peso por la altura al cuadrado, el resultado debe desplegarlo como su IMC.

# Tu código aquí:
#Definir variables
estatura = 0.0
estatura = float(input("Ingrese su estatura en metros: "))
peso = 0.0
peso = float(input("Ingrese su peso en kg: "))

#Entrada
imc = peso / (estatura * estatura)

#Salida
print(f"Su IMC es: {imc}")
