#BIENVENIDO AL PROGRAMA 
print("CERRADURA: La multiplicacion de dos numeros reales siempre da como resultado otro numero real")
print(" a * b pertenece a R")
print() #linea en blanco para separar la introduccion de la siguiente seccion

#IMPRIME EL MENSAJE QUE INDICA QUE EL PROGRAMA DEMOSTRARA LA PROPIEDAD DE CERRADURA 
print("El siguiente programa realiza la propiedad de cerradura")
print()

#SOLICITA AL USUARIO QUE INGRESE DOS NUMEROS
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#CALCULA LA MULTIPLICACION DE DOS NUMEROS
multi = a * b


#VERIFICA SI LA MULTIPLICACION ES UN NUMERO ENTERO
if  multi.is_integer():
    resultado = "entero"
else:
    resultado = "racional"

#MUESTRA EL RESULTADO DE LA MULTIPLICACIONY SI TIPO 
print()
print("La MULTIPLICACION de", a, "y", b, "es:", multi)
print()
print("El resultado de la multiplicacion es un número", resultado)