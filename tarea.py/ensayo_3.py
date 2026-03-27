# Ejercicio 3
# ------------------------------------------------------------
# Una empresa tiene 3 empleados. A cada uno se le descuenta
# un 20% de su sueldo bruto en impuestos y un 7% en salud.
# El programa debe pedir el nombre y sueldo bruto de cada empleado.
# Muestra el sueldo líquido (después de ambos descuentos) de cada uno
# y el total que debe pagar la empresa en sueldos líquidos.
 
# Tu código aquí:
Empleado_1 = input("Inserte nombre del empleado 1: ")
Sueldo_bruto_1 = float(input("Inserte sueldo bruto del empleado 1: "))
Empleado_2 = input("Inserte nombre del empleado 2: ")
Sueldo_bruto_2 = float(input("Inserte sueldo bruto del empleado 2: "))
Empleado_3 = input("Inserte nombre del empleado 3: ")
Sueldo_bruto_3 = float(input("Inserte sueldo bruto del empleado 3: "))

Descuento_impuestos = 0.20
Descuento_salud = 0.07
Sueldo_liquido_1 = Sueldo_bruto_1 * (1 - Descuento_impuestos - Descuento_salud)
Sueldo_liquido_2 = Sueldo_bruto_2 * (1 - Descuento_impuestos - Descuento_salud)
Sueldo_liquido_3 = Sueldo_bruto_3 * (1 - Descuento_impuestos - Descuento_salud)
Total_sueldos_liquidos = Sueldo_liquido_1 + Sueldo_liquido_2 + Sueldo_liquido_3
print(f"El sueldo líquido de {Empleado_1} es: {Sueldo_liquido_1}")
print(f"El sueldo líquido de {Empleado_2} es: {Sueldo_liquido_2}")
print(f"El sueldo líquido de {Empleado_3} es: {Sueldo_liquido_3}")
print(f"El total que debe pagar la empresa en sueldos líquidos es: {Total_sueldos_liquidos}")