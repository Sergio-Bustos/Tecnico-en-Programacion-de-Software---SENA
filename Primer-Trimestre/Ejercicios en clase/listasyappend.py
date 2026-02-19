# Uso de listas y .append. Ejercicios y practicas

print("------------ Ejercicios de .append en listas en clase -----------")

# Agregar un nombre a una lista

nombres = ["Ana", "Luis", "María"]
nombre = input("Ingresa tu nombre: ") # Para pedir el nombre al usuario
nombres.append(nombre)  # Agrega el nombre del usuario al final de la lista
print(nombres)
 
# Lista de numeros

numeros = []
numero1 = int(input("Ingresa el numero 1: ")) # Para pedirle al usuario el numero int 1
numero2 = int(input("Ingresa el numero que le sigue al anterior: ")) # Para pedirle al usuario el numero int que sigue del 1
numero3 = int(input("Ingresa el numero que le sigue al anterior: ")) # Para pedirle al usuario el numero int que sigue despues del 2
numero4 = int(input("Ingresa el numero que le sigue al anterior: ")) # Para pedirle al usuario el numero int que sigue despues del 3
numero5 = int(input("Ingresa el numero que le sigue al anterior: ")) # Para pedirle al usuario el numero int que sigue despues del 4
numeros.append(numero1) # Para agregar el numero int 1 dado por el usuario al final de la lista
numeros.append(numero2) # Para agregar el numero int 2 dado por el usuario al final de la lista
numeros.append(numero3) # Para agregar el numero int 3 dado por el usuario al final de la lista
numeros.append(numero4) # Para agregar el numero int 4 dado por el usuario al final de la lista
numeros.append(numero5) # Para agregar el numero int 5 dado por el usuario al final de la lista
print(f"Los numeros dados por el usuario son {numeros[0]},{numeros[1]},{numeros[2]},{numeros[3]},{numeros[4]} y en la lista finalmente se verian asi: {numeros}")

# Lista con strings y numeros

lista = ["Hola", 7, "Mundo", 3.14]
lista.append("Python") # Para agregar el string 'Python' al final de la lsita
print(lista)

# Indexacion de un numero

numeros = [10, 20, 30, 40, 50]
print(numeros[2]) # Para agarrar el valor de la posicion 2 (30)

# Indexacion de un nombre

nombres = ["Pedro", "Laura", "Sofía", "Miguel"]
print(nombres[0]) # Para agarrar el valor de la posicion 0 ('Pedro')

# Lista de numeros

lista = []
num1 = int(input("Ingresa el numero 1: ")) # Para pedirle al usuario el numero int 1
num2 = int(input("Ingresa el numero que le sigue: ")) # Para pedirle al usuario el numero int que sigue del 1
num3 = int(input("Ingresa el numero que le sigue al anterior: ")) # Para pedirle al usuario el numero int que sigue despues del 2
lista.append(num1) # Para agregar el numero int 1 dado por el usuario al final de la lista
lista.append(num2) # Para agregar el numero int 2 dado por el usuario al final de la lista
lista.append(num3) # Para agregar el numero int 3 dado por el usuario al final de la lista
print(f"Los numeros dados por el usuario son {lista[0]},{lista[1]},{lista[2]} y en la lista finalmente se verian asi: {lista}")


# Lista de dias de la semana

dias = []
dia1 = input("Ingresa el dia lunes: ") # Para pedirle al usuario el string del dia lunes
dia2 = input("Ingresa el dia que le sigue al anterior: ") # Para pedirle al usuario el string del dia que va despues del lunes
dia3 = input("Ingresa el dia que le sigue al anterior: ") # Para pedirle al usuario el string del dia que va despues del martes
dia4 = input("Ingresa el dia que le sigue al anterior: ") # Para pedirle al usuario el string del dia que va despues del miercoles
dia5 = input("Ingresa el dia que le sigue al anterior: ") # Para pedirle al usuario el string del dia que va despues del jueves
dias.append(dia1) # Para añadir el dia 1 de la semana al final de la lista
dias.append(dia2) # Para añadir el dia 2 de la semana al final de la lista
dias.append(dia3) # Para añadir el dia 3 de la semana al final de la lista
dias.append(dia4) # Para añadir el dia 4 de la semana al final de la lista
dias.append(dia5) # Para añadir el dia 5 de la semana al final de la lista
print(f"Los dias que ingreso el usuario son: {dias[0]},{dias[1]},{dias[2]},{dias[3]},{dias[4]} y en la lista finalmente se verian asi: {dias}")
# Lista de animales

listas = []
animal1 = input("Ingresa un animal: ") # Para pedirle al usuario un animal
animal2 = input("Ingresa otro animal: ") # Para pedirle al usuario otro animal
animal3 = input("Ingresa otro animal: ") # Para pedirle al usuario otro animal
animal4 = input("Ingresa otro animal: ") # Para pedirle al usuario otro ultimo animal
listas.append(animal1) # Para agregar el animal 1 al final de la lista
listas.append(animal2) # Para agregar el animal 2 al final de la lista
listas.append(animal3) # Para agregar el animal 3 al final de la lista
listas.append(animal4) # Para agregar el animal 4 al final de la lista
print(f"Los animales que ingreso el usuario son: {listas[0]},{listas[1]},{listas[2]},{listas[3]} y en la lista finalmente se verian asi: {listas}")

# Agregar dos numeros a la lista

nums = [10, 20, 30]
nums.append(40) # Se agrega el numero 40 al final de la lista
nums.append(50) # Se agrega el numero 50 al final de la lista
print(nums)

# Sumar dos listas entre si

colores1 = ["rojo", "azul", "verde"]
colores2 = ["amarillo", "negro"]
colores = colores1 + colores2 # Para sumar las dos listas,aunque tambien se puede usar .extend() que fusiona o junta las dos listas
print(colores)


