# Pedimos los datos al usuario

print("¿Qué animal es tu mascota?")
animal = input()

print("Escribe un adjetivo para describir a tu mascota:")
adjetivo = input()

print("Escribe un lugar de la casa:")
lugar_casa = input()

print("Escribe un objeto:")
objeto = input()

print("Escribe una parte de la casa:")
parte_casa = input()

print("Escribe una emoción:")
emocion = input()

print("Escribe un mueble:")
mueble = input()

# Imprimimos la historia
print("Tengo una mascota que es un", animal + ".")
print("Es muy", adjetivo, "y siempre quiere jugar.")
print("Por la mañana corre por", lugar_casa + ".")
print("Después encuentra un", objeto, "y lo lleva en la boca.")
print("Cuando alguien entra por", parte_casa + ",", "mi mascota se pone", emocion + ".")
print("Al final se duerme en", mueble + ".")