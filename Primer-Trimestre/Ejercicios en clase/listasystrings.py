# Listas. Ejemplos y Practicas

print("----- Ejercicios de listas y strings en clase----")

# Agregar un nombre a una lista

nombres = ["Sofia", "Farid", "María"]
nombre = input("Ingresa tu nombre: ") # Para pedir el nombre al usuario
nombres.append(nombre)  # Agrega el nombre del usuario al final de la lista
print(nombres)
 
 
# Lista de numeros

numeros = [1, 2, 3, 4, 5]
eliminar = int(input("Que numero del 1 al 5 no te gusta? Escribelo tal cual como entero por favor: ")) # Para pedir el numero int que no le gusta al usuario para removerlo de la lista
numeros.remove(eliminar) # Para eliminar el numero que no le gusta al usuario de la lista
print(f"El numero que no le gusta al usuario es: {eliminar} y en la lista finalmente removido seria asi: {numeros}")


# Agregar palabra

lista = ["SENA","Programacion",5.0,"Trimestre"]
lista.append("Python") # Agrega una palabra al final de la lista
print(lista)

# Indexacion de un numero

numeros = [10, 20, 30, 40, 50]
print(numeros[2]) # Muestra el valor de la posicion 2 en la lista (30)

# Indexacion de un nombre

nombres = ["Pedro", "Laura", "Sofía", "Miguel"]
print(nombres[0])  # Muestra el valor de la posicion 0 en la lista ('Pedro')

# Lista de numeros

lista = []
num1 = int(input("Ingresa un numero entero: ")) # Para pedirle un numero int al usuario
num2 = int(input("Ingresa otro numero entero: ")) # Para pedirle otro numero int al usuario
num3 = int(input("Ingresa otro numero entero: ")) # Para pedirle otro numero int al usuario
lista.append(num1) # Para agregar el numero int del usuario al final de la lista
lista.append(num2) # Para agregar el numero int del usuario al final de la lista
lista.append(num3) # Para agregar el numero int del usuario al final de la lista
print(f"Los numeros que ingreso el usuario son: {lista[0]},{lista[1]},{lista[2]} y en la lista finalmente se verian asi: {lista}")

# Lista de dias de la semana

dias = []
dias.append("Lunes") # Para agregar el dia lunes al final de la lista
dias.append("Martes") # Para agregar el dia martes al final de la lista
dias.append("Miércoles") # Para agregar el dia miercoles al final de la lista
dias.append("Jueves") # Para agregar el dia jueves al final de la lista
dias.append("Viernes") # Para agregar el dia viernes al final de la lista
print(f"El primer dia de la semana es {dias[0]}, el segundo es {dias[1]}, el tercero es {dias[2]}, el cuarto es {dias[3]},y el quinto es {dias[4]} y en la lista finalmente se veria asi: {dias}")






