# Operadores Lógicos and, or, not, xor

#   a  | b | a and b
#   .v. | v | v
#   .v. | f | f
#   .f. | v | f
#   .f. | f | f

#    a  | b | a or b
#   .v. | v | v
#   .v. | f | v
#   .f. | v | v
#  .f. | f | f

#   a | not a
#   v   f
#   f   v

#Ejercicio mayor de 3 números
#numA = int(input("1er número : "))
#numB = int(input("2do número : "))
#numC = int(input("3er número : "))

#if numA > numB and numA > numC:
#    print(numA)
#else:
#    if numB > numC:
#        print(numB)
#    else:
#        print(numC)

edad = int(input("Edad : "))

if edad > 0 and edad < 130: # 0 < edad < 130
   if edad <= 18:
      print("mayor")
   else:
      print("menor")
else:
   print("!!!...Edad inválida, debe estar entre cero y 130...!!!")
if edad < 0 and edad >10:
   print ("infante")
if edad <11 and edad > 18:
   print ("Preadolescente")
if edad <18 and edad > 30:
   print ("Adulto Joven")
if edad <30 and edad > 50:
   print ("Adulto")
if edad <50 and edad >130:
    print ("Adulto Mayor") 