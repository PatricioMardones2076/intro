# Don Juanito es muy detallista en todo, sabe que para lavar 1 kilo de ropa necesita 300 gramos de detergente(fijo) y 100 gramos de suavizante(fijo), hoy llegó a su casa y ya no le queda ropa limpia, debe lavar de inmediato los 13 kilos de ropa sucia que tiene ¿Cuántos KILOS de detergente y suavizante necesita?

# Tu código aquí:

#Declaracion de variables
Kilos_de_ropa_sucia = ""
Kilos_de_ropa_sucia = int(input("Inserte la cantidad de kilos de ropa sucia: "))
Detergente_por_kilo = 0
Detergente_por_kilo = 0.3
Suavizante_por_kilo = 0
Suavizante_por_kilo = 0.1  

#Entrada
Kilos_de_detergente_necesarios = Kilos_de_ropa_sucia * Detergente_por_kilo
Kilos_de_suavizante_necesarios = Kilos_de_ropa_sucia * Suavizante_por_kilo

#Salida
print(f"Don Juanito necesita {Kilos_de_detergente_necesarios} kg de detergente y {Kilos_de_suavizante_necesarios} kg de suavizante para lavar los 13 kilos de ropa sucia.")