#Preguntar dos edades al usuario. Si alguna de las dos edades es menor a 18,
# mostrar un mensaje de alerta “Hay un menor de edad” si no, mostrar el mensaje
# “todos son mayores de edad”

edad1 = int(input("Ingrese su edad: "))
edad2 = int(input("Ingrese su edad: "))

if edad1 < 18 or edad2 < 18:
    print("Hay un menor de edad ")
else:
    print("Todos son mayores de edad")