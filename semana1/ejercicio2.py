#El peso promedio de un adulto debe ser su estatura menos un metro,
#el rango aceptable es +-5kg, ejemplo si mido 1.60, mi peso promedio debe ser de 55kg a 65kg.
# Pídale al usuario que ingrese su estatura y verifique si está en el peso promedio.

estatura = float(input("Ingrese la estatura de la persona en metros: "))
pesoPromedio = (estatura - 1)*100
pesoMinimo = pesoPromedio - 5
pesoMaximo = pesoPromedio + 5
pesoKg = float(input("Ingrese el peso de la persona en Kg: "))

if pesoMinimo <= pesoKg <= pesoMaximo:
    print("Esta dentro del promedio normal")
else:
    print ("No esta dentro del promedio normal")