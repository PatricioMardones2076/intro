# Ejercicio 4
# ------------------------------------------------------------
# Pedro fue al supermercado y compró:
#   - Arroz: le pide al usuario el precio por kilo y cuántos kilos compró
#   - Leche: le pide al usuario el precio por litro y cuántos litros compró
#   - Pan: le pide al usuario el precio por unidad y cuántas unidades compró
# Pedro paga con un billete de $10.000.
# ¿Cuánto gastó en total y cuánto es su vuelto?
 
# Tu código aquí:
Precio_arroz = float(input("Inserte el precio por kilo de arroz: "))
Kilos_arroz = float(input("Inserte la cantidad de kilos de arroz comprados: "))
Precio_leche = float(input("Inserte el precio por litro de leche: "))
Litros_leche = float(input("Inserte la cantidad de litros de leche comprados: "))
Precio_pan = float(input("Inserte el precio por unidad de pan: "))
Unidades_pan = float(input("Inserte la cantidad de unidades de pan compradas: "))
Total_arroz = Precio_arroz * Kilos_arroz
Total_leche = Precio_leche * Litros_leche
Total_pan = Precio_pan * Unidades_pan
Total_gasto = Total_arroz + Total_leche + Total_pan
Pago = 10000
Vuelto = Pago - Total_gasto
print(f"El total que gastó Pedro es: {Total_gasto}")
print(f"El vuelto que le deben dar a Pedro es: {Vuelto}")