# Ejercicios de potenciacion en clase

print("------- Ejercicios de potenciacion en clase -------")

# Ejercicio 1: 7⁵ / 7² = 7⁵⁻² = 343 

print("------------------ Ejercicio 1 --------------------")

num1 = int(input("Ingresa el numero siete por favor: ")) # Pide número entero al usuario
num2 = int(input("Ingresa el numero cinco por favor: ")) # Pide número entero al usuario
num3 = int(input("Ingresa el numero dos por favor: ")) # Pide número entero al usuario
proceso = num1 ** num2 
proceso2 = num1 ** num3
proceso3 = proceso/proceso2
print(f"El resultado de 7⁵ / 7² es: {proceso3}")



# Ejercicio 2: 10⁴ / 10¹ = 10⁴⁻¹ = 10³ = 1,000

print("------------------ Ejercicio 2 --------------------")

numero = int(input("Ingresa el numero diez por favor: ")) # Pide número entero al usuario
numero2 = int(input("Ingresa el numero cuatro por favor: ")) # Pide número entero al usuario
numero3 = int(input("Ingresa el numero uno por favor: ")) # Pide número entero al usuario
procesos = numero** numero2 
procesos2 = numero ** numero3
procesofinal = procesos/procesos2
print(f"El resultado de 10⁴ / 10¹ es: {procesofinal}")



# Ejercicio 3: Potencia de una potencia: (3²)³ = 3⁶ = 729

print("------------------ Ejercicio 3 --------------------")

numeral = int(input("Ingresa el numero tres por favor: ")) # Pide número entero al usuario
numeral2 = int(input("Ingresa el numero dos por favor: ")) # Pide número entero al usuario
procedimiento = numeral**numeral2
pro = procedimiento**numeral
print(f"El resultado de (3²)³ es: {pro}")



# Ejercicio 4: Potencia de una potencia: (3²)⁴ = 3²^⁴ = 3⁸ = 6,561

print("------------------ Ejercicio 4 --------------------")

numeri = int(input("Ingresa el numero tres por favor: ")) # Pide número entero al usuario
numers = int(input("Ingresa el numero dos por favor: ")) # Pide número entero al usuario
numerss = int(input("Ingresa el numero cuatro por favor: ")) # Pide número entero al usuario
process = numeri**numers
process2 = process**numerss
print(f"El resultado de (3²)⁴ es: {process2}")



# Ejercicio 5: Potencia de una potencia: (5³)² = 5³^² = 5⁶ = 15,625

print("------------------ Ejercicio 5 --------------------")

num = int(input("Ingresa el numero cinco por favor: ")) # Pide número entero al usuario
num2 = int(input("Ingresa el numero tres por favor: ")) # Pide número entero al usuario
num3 = int(input("Ingresa el numero dos por favor: ")) # Pide número entero al usuario
potencia = num**num2
potencia2 = potencia**num3 
print(f"El resultado de (5³)² es: {potencia2}")



# Ejercicio 6: Potencia de una multiplicacion o producto: (2*3)² = 4*9 = 36

print("------------------ Ejercicio 6 --------------------")

nume = int(input("Ingresa el numero dos por favor: ")) # Pide número entero al usuario
nume2 = int(input("Ingresa el numero tres por favor: ")) # Pide número entero al usuario
procek = nume*nume2
procek2 = procek**nume
print(f"El resultado de (2*3)² es: {procek2}")
