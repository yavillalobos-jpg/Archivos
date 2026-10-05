#Leer un archivo "misdatos.txt" usando with
with open("misdatos.txt", "r", encoding="utf-8") as archivo:
    content = archivo.read()
print(content)