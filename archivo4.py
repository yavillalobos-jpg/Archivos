# Crea un programa que permita guardar n cantidad de notas en un archivo,
# leer las notas y calcular el promedio, la nota mas alta y la nota mas baja.

while True:
	try:
		cantidad = int(input("Cuantas notas deseas guardar? "))
		if cantidad > 0:
			break
		print("La cantidad debe ser mayor que cero.")
	except ValueError:
		print("Ingresa un numero entero valido.")

notas = []
for numero in range(cantidad):
	while True:
		try:
			nota = float(input(f"Ingresa la nota {numero + 1}: "))
			notas.append(nota)
			break
		except ValueError:
			print("Ingresa una nota numerica valida.")

with open("notas.txt", "w", encoding="utf-8") as archivo:
	for nota in notas:
		archivo.write(f"{nota}\n")

with open("notas.txt", "r", encoding="utf-8") as archivo:
	notas = [float(linea) for linea in archivo]

promedio = sum(notas) / len(notas)
print(f"Promedio: {promedio:.2f}")
print(f"Nota mas alta: {max(notas)}")
print(f"Nota mas baja: {min(notas)}")
