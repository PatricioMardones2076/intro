# Operadores aritmeticos
+ suma (tercera prioridad)
- resta (tercera prioridad)
* multiplicacion (segunda prioridad)
/ division (segunda prioridad)
% resto (segunda prioridad)
** potencia (primera prioridad) 

#Declaración de variables
ed = 37
ed_prox_anio = 0

ed = int(input("Su edad: ")) #int convierte un cadena(string, texto, alfanumérico) a número entero, float convierte a decimal

ed_prox_anio = ed + 1

#Salida
print("Su edad actual es", ed, "el próximo año vas a tener", ed_prox_anio)