#programa que realiza la comparacion (mayor, menor) de dos numeros 
#PEDIRLE AL USUARIO QUE INGRESE DOS NUMEROS FLOTANTES
print("INGRESE DOS NUMEROS FLOTANTES")
num1= float(input("INGRESA EL PRIMER NUMERO"))
num2= float(input("INGRESE EL SEGUNDO NUMERO"))
#COMPARAR LOS NUMEROS
if num1 > num2:
    print("EL PRIMER NUMERO ES MAYOR")
elif num1 < num2:
    print("EL SEGUNDO NUMERO ES MAYOR")
    format((num2,num1))
else:
    print("AMBOS NUMEROS SON IGUALES")
    
