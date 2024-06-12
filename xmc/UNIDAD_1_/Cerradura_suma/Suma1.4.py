#BIENVENIDO AL PROGRAMA 
print("CERRADURA: La suma de dos numeros reales siempre da como resultado otro numero real")
print(" a + b pertenece a R")
print() #linea en blanco para separar la introduccion de la siguiente seccion

#IMPRIME EL MENSAJE QUE INDICA QUE EL PROGRAMA DEMOSTRARA LA PROPIEDAD DE CERRADURA 
print("El siguiente programa realiza la propiedad de cerradura")
print()

#SOLICITA AL USUARIO QUE INGRESE DOS NUMEROS
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

#CALCULA LA SUMA DE DOS NUMEROS
suma = a + b


#VERIFICA SI LA SUMA ES UN NUMERO ENTERO
if suma.is_integer():
    resultado = "entero"
else:
    resultado = "racional"

#MUESTRA EL RESULTADO DE LA SUMA Y SI TIPO 
print()
print("La suma de", a, "y", b, "es:", suma)
print()
print("El resultado de la suma es un número", resultado)