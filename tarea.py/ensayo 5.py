# Ejercicio 5
# ------------------------------------------------------------
# Una persona decide ahorrar todos los meses la misma cantidad
# de dinero. El programa debe pedir:
#   - El nombre de la persona
#   - Cuánto ahorra por mes
#   - A cuántos meses plazo quiere ahorrar
# Al monto acumulado se le suma un interés mensual del 3%.
# (interés simple: capital * tasa * meses)
# ¿Cuánto dinero tendrá al final del plazo incluyendo intereses?
 
# Tu código aquí:

Nombre = input("Inserte el nombre de la persona: ")
Ahorro_mensual = float(input("Inserte cuánto ahorra por mes: "))
Meses_plazo = int(input("Inserte a cuántos meses plazo quiere ahorrar: "))
Tasa_interes = 0.03
Capital_total = Ahorro_mensual * Meses_plazo
Interes_total = Capital_total * Tasa_interes * Meses_plazo
Monto_final = Capital_total + Interes_total
print(f"Al final del plazo, {Nombre} tendrá un total de: {Monto_final}")