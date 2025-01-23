#Pedir al usuario un número, mostrar un mensaje indicando si el número
#ingresado es un número par o impar.  Recuerda que los textos que leemos del
#usuario son de tipo string, deberás convertirlo a entero y verificar si es par o impar,
#se deben mostrar los textos “es par” o “es impar” según corresponda.

numero = int(input("Ingrese un numero:"))

if numero % 2 == 0:
    print("El numeor es par.")
else:
    print("El numero es impar.")