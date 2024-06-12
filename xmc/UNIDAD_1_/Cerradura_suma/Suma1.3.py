#Estre programa indica cual de los dos numeros dados por el udusrio  es el mayor o menor 
#PEDIRLE AL USUARIO QUE INGRESE DOS NUMEROS FLOTANTES
print("INGRESE DOS NUMEROS FLOTANTES")
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))

#COMPARAR LOS NUMEROS
if  num1 > num2 :
    print("el primer numero es mayor que el segundo numero ")
elif num1<num2:
    print("el segundo numero es mayor que el primer numero ")
    format((num1,num2))
else:
    print("los numeros son iguales")