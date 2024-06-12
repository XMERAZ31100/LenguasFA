print("CERRADORA: operaciones basicas, suma , resta , multiplicacion , division ")
print()
#PEDIR AL USUARIO QUE INGRESE LOS NUMEROS 
num1 = float(input("INGRESE EL PRIMER NUMERO: "))
num2 = float(input("INGRESE EL SEGUNDO NUMERO: "))
print()
#REALIZAR LAS OPERACIONES BASICAS
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
#VALIDAR QUE NO SE DIVIDA ENTRE CERO
if num2 != 0 :
    division = num1 / num2
else:
    division = "NO SE PUEDE DIVIDIR ENTRE CERO"
print()
#IMPRIMIR LOS RESULTADOS
print("LA SUMA ES: ",suma)
print("LA RESTA ES: ",resta)
print("LA MULTIPLICACION ES: ",multiplicacion)
print("LA DIVISION ES: ",division)