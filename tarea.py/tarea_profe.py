#Desarrolle un programa que permita calcular la fecha de nacimiento a un solo digito la fecha de 2 personas y luego sume estas dos fechas para obtener su numero maestro
def calcular_numero_maestro(dia, mes, anio):
    fecha = f"{dia:02d}{mes:02d}{anio}"
    suma = sum(int(digito) for digito in fecha)
    while suma >= 10:
        suma = sum(int(digito) for digito in str(suma))
    return suma