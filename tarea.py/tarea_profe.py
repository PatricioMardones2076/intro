#Desarrolle un programa que permita calcular la fecha de nacimiento a un solo digito la fecha de 2 personas y luego sume estas dos fechas para obtener su numero maestro
def calcular_numero_maestro(dia, mes, anio):
    # Sumar los dígitos del día, mes y año
    suma = sum(int(digito) for digito in str(dia) + str(mes) + str(anio))
    
    # Reducir la suma a un solo dígito
    while suma >= 10:
        suma = sum(int(digito) for digito in str(suma))
    
    return suma
# Solicitar la fecha de nacimiento de la primera persona
dia1 = int(input("Ingrese el día de nacimiento de la primera persona: "))
mes1 = int(input("Ingrese el mes de nacimiento de la primera persona: "))
anio1 = int(input("Ingrese el año de nacimiento de la primera persona: "))
# Solicitar la fecha de nacimiento de la segunda persona
dia2 = int(input("Ingrese el día de nacimiento de la segunda persona: "))
mes2 = int(input("Ingrese el mes de nacimiento de la segunda persona: "))
anio2 = int(input("Ingrese el año de nacimiento de la segunda persona: "))
# Calcular el número maestro para cada persona
numero_maestro1 = calcular_numero_maestro(dia1, mes1, anio1)
numero_maestro2 = calcular_numero_maestro(dia2, mes2, anio2)
# Sumar los números maestros de ambas personas
numero_maestro_total = numero_maestro1 + numero_maestro2
# Reducir el número maestro total a un solo dígito
while numero_maestro_total >= 10:
    numero_maestro_total = sum(int(digito) for digito in str(numero_maestro_total))
# Mostrar el número maestro total
print("El número maestro total es:", numero_maestro_total)
