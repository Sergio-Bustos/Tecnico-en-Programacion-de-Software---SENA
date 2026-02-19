# Ejercicios y practicas de diccionarios

print("------Ejercicios de diccionarios en clase------")


# Carro y sus caracteristicas

carro = {
    "marca":  "BMW",
    "placa": "WDK257",
    "modelo": "M3",
    "año_modelo": 2023,
    "motor": "V3"
}

print(f"La marca del carro es: {(carro['marca'])},la placa es: {(carro['placa'])},el modelo del carro es: {(carro['modelo'])},el año del modelo {(carro['modelo'])} es {(carro['año_modelo'])},y el motor que tiene el {(carro['modelo'])} es {(carro['motor'])}")


# Coordenadas

d = {
    (1,2): "Punto A",
    (3,4): "Punto B"
}
print(d.get((3,4))) # .get() agarra el par llave y valor

# Diccionario de estudiante: Crea un diccionario con nombre, edad y nota. Muestra los datos.


estudiante = {
    "nombre": input("Nombre del estudiante: "), # Para pedir el nombre
    "edad": int(input("Edad del estudiante: ")), # Para pedir la edad al usuario
    "nota": float(input("Nota del estudiante: ")) # Para pedirle la nota al usuario
}

print(f"Datos del estudiante: {estudiante}")

# Suma de notas de estudiantes: Tres estudiantes con su nota. Muestra el promedio.

notas = {
    "Ana": float(input("Nota de Ana: ")), # Para pedirle la nota al usuario
    "Luis": float(input("Nota de Luis: ")), # Para pedirle la nota al usuario
    "Carlos": float(input("Nota de Carlos: ")) # Para pedirle la nota al usuario
}

promedio = (notas["Ana"] + notas["Luis"] + notas["Carlos"]) / 3

print(f"Notas de los estudiantes: {notas}")
print(f"Promedio general: {promedio}")

