#Desarrolle un programa que permita ingresar la edad del usuario y despliegue si es mayor o menor de edad (edad maxima 130)
edad = int (input("Ingrese su edad: "))
if edad >= 18:
    print("Usted es mayor de edad")

if edad >= 130:
        print("Edad no valida, INGRESE SU EDAD REAL")

else: print("Usted es menor de edad")

#Leer cuento chino "Buena suerte Mala suerte"

edad = 0
edad = int (input("Ingrese su edad: "))
if edad < 0:
    print ("La edad no puede ser menor que cero")

else:
    if edad <18:
        print("Usted es menor de edad")

    if edad > 130:
        print("Su edad supera el limite permitido")
    else:
        print("Usted es mayor de edad")    

#Desarrolle un programa que permita ingresar 3 numeros y desplegar siempre el mayor: Haga simulaciones siempre con 3 numeros distintos

primer_num = int(input("Ingrese el primer numero:"))
segundo_num = int(input("Ingrese el segundo numero:"))
tercer_num = int(input("Ingrese el tercer numero:"))
if primer_num > segundo_num and primer_num > tercer_num:
    print("El numero mayor es: ", primer_num)
if segundo_num > tercer_num and segundo_num > primer_num:
        print("El numero mayor es: ", segundo_num)
if tercer_num > segundo_num and tercer_num > primer_num:
        print("El numero mayor es: ", tercer_num)


#Desarrolle un programa que permita ingresar 3 numeros y siempre los despliegue ascendentemente: Haga simulaciones siempre con 3 numeros distintos