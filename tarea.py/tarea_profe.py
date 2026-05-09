#Desarrolle un programa que permita calcular la fecha de nacimiento a un solo digito la fecha de 2 personas y luego sume estas dos fechas para obtener su numero maestro
def calcular_numero_maestro(dia, mes, anio):
    # Sumar los dígitos del día, mes y año
    suma = sum(int(digito) for digito in str(dia) + str(mes) + str(anio))
    
    # Reducir la suma a un solo dígito
    while suma >= 10:
        suma = sum(int(digito) for digito in str(suma))
    
    return suma