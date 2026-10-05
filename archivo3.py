#leer los nombres, apellidos, edad y carrera de un estudiante
#guardado en un archivo llamado estudiante.txt
nombres = input("Dime tus nombres: ")
apellidos = input("Dime tus apellidos: ")
edad = input("Dime tu edad: ")
carrera = input("Dime tu carrera: ")

datos = f"Nombre: {nombres.title()}\nApellidos: {apellidos.title()}\nEdad: {edad}\nCarrera: {carrera.title()}\n"

with open("estudiante.txt", "a+", encoding="utf-8") as archivo:
    archivo.write(datos)

print("Archivo creado sastisfactoriamente.")