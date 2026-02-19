# Entrada datos; Input,float,int. Ejercicios y practicas

print("------------ Ejercicios de entrada de datos en clase -----------")

# Pedirle al usuario su edad

edad = int(input("Ingresa tu edad: ")) # Para pedirle la edad al usuario
print(f"Tu edad es de {edad} años,¡que joven!")


# Calcular la edad que tendra en el año siguiente

edad2 = int(input("¿Cuántos años tienes? ")) # Para pedirle la edad al usuario
print(f"El año que viene tendrás {edad2 + 1} años.") # Sumar 1 año a la edad actual e imprimir el resultado


# Suma de dos numeros

a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
print(f"La suma de {a} + {b} es {a + b}")



# Promedio de tres numeros

n1 = float(input("Nota 1: ")) # Para pedirle la primera nota al usuario
n2 = float(input("Nota 2: ")) # Para pedirle la segunda nota al usuario
n3 = float(input("Nota 3: ")) # Para pedirle la tercera nota al usuario
promedio = (n1 + n2 + n3) / 3 # Para promediar las 3 notas
print(f"Tu promedio es: {promedio}")



# Cuadrado o potencia de un numero

num = float(input("Número: ")) # Para pedirle un numero int al usuario
cuadrado = num ** 2 # Para potenciarlo
print(f"El cuadrado de {num} es {cuadrado}")



# Nombre completo del usuario

nombre = input("Nombre: ") #  Para pedirle los nombre al usuario
apellido = input("Apellido: ") # Para pedirle los apellidos del usuario
print(f"Tu nombre completo es: {nombre} {apellido}")



# Calcular el año de nacimiento

edad3 = int(input("¿Cuántos años tienes? ")) # Para pedir el año de nacimiento del usuario
año_actual = 2025 
nacimiento = año_actual - edad3 # Restar el año actual menos el año de nacimiento del usuario
print(f"Naciste en el año {nacimiento}")



# Comida favorita

comid= input("¿Cual es tu comida favorita?: ") # Para pedirle la comida favorita al usuario
print(f"A mi tambien me gusta {comid} pero prefiero comer otras comidas")



# Color favorito

color = input("¿Cuál es tu color favorito? ") # Para pedirle el color favorito al usuario
print(f"Tu color favorito es {color}")



# Numero favorito

numero = int(input("¿Cuál es tu número favorito? ")) # Para pedirle el numero favorito al usuario
print(f"Tu número favorito es {numero}, a mi tambien me gusta mucho")



# Carro que quiere

carro = input("¿Que marca de carro te gustaria tener?: ") # Para pedirle la marca de carros deseada por el usuario
print(f"Que bueno un {carro},aunque es muy caro,tu puedes lograrlo :)")



# De manera individual desarrolle un programa que permita calcular el promedio final de puntos de los equipos de un torneo

equipo1 = int(input("¿Cuantos puntos tiene el Real Madrid?: ")) # Para pedir la cantidad de puntos del Real Madrid
equipo2 = int(input("¿Cuantos puntos tiene el Barcelona?: ")) # Para pedir la cantidad de puntos del Barcelona
equipo3 = int(input("¿Cuantos puntos tiene el Manchester City?: ")) # Para pedir la cantidad de puntos del Manchester City
equipo4 = int(input("¿Cuantos puntos tiene el Cali?: ")) # Para pedir la cantidad de puntos del Cali
equipo5 = int(input("¿cuantos puntos tiene el America?: ")) # Para pedir la cantidad de puntos del America
suma = equipo1+equipo2+equipo3+equipo4+equipo5 # Para sumar todos los puntos
promed = suma/5  # Para promediar finalmente los puntos de todos los equipos
print(f"el promedio de los puntos de todos los 5 equipos es: {promed} ")



# Ahora igual pero que diga el nombre del equipo que ingresó el usuario y los puntos

nombre = input("Ingrese el nombre de un equipo: ") # Para que el usuario diga el nombre del equipo
temporada1 = int(input("Cuantos puntos obvtuvo en la primer temporada: ")) # Para que el usuario diga cuantos puntos obtuvo el equipo en la temporada
temporada2 = int(input("Cuantos puntos obtuvo en la segunda temporada: "))  # Para que el usuario diga cuantos puntos obtuvo el equipo en la otra temporada
temporada3 = int(input("Cuantos puntos obtuvo en la tercer temporada: ")) # Para que el usuario diga cuantos puntos obtuvo el equipo en la otra temporada
promediadoss =  temporada1 + temporada2 + temporada3 # Para sumar todos los puntos
pro = promediadoss / 3 # Para promediar todos los puntos del equipo en esas tres temporadas
print(f"El promedio de puntos de {nombre} fueron de: {pro} puntos ")