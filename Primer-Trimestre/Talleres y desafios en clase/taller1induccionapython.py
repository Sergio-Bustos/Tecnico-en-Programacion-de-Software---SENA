# Taller numero uno induccion a Python:

print("------- Taller 1 induccion a Python interactivo -------")

# Ejercicio 1: Crea una variable llamada 'nombre' y asignale tu nombre como string

print("------------------ Ejercicio 1 --------------------")

nombre = input("Introduce tu nombre completo: ") # Pide el nombre completo al usuario
print(f"Tu nombre es: {nombre}, me alegra conocerte")


# Ejercicio 2: Imprime un saludo personalizado usando la variable nombre

print("------------------ Ejercicio 2 --------------------")

nombre_completo = input("Ingresa tu nombre completo por favor: ") # Pide otra vez el nombre completo al usuario
print(f"Holaaa {nombre_completo} mucho gusto conocerte")



# Ejercicio 3: Crea una variable 'ciudad' con el nombre de tu ciudad

print("------------------ Ejercicio 3 --------------------")

ciudad = input("¿En que ciudad vives?: ") # Pide la ciudad donde vive el usuario
print(f"Vives en {ciudad},¡es muy bonito!")


# Ejercicio 4: Imprime 'hola, soy {nombre} y vivo en {ciudad}'

print("------------------ Ejercicio 4 --------------------")

nombres = input("Ingresa tu nombre completo: ") # Pide el nombre completo al usuario
ciudades = input("Ingresa la ciudad donde vives: ") # Pide la ciudad donde vive el usuario
print(f"Hola,soy {nombres}, y vivo en {ciudades}")



# Ejercicio 5: Usa 'input()' para pedir al usuario su color favorito y guarda la respuesta en 'color'

print("------------------ Ejercicio 5 --------------------")

color = input("Ingresa tu color favorito: ") # Pide el color favorito del usuario
print(f"Hola, el {color} es muy lindo")



# Ejercicio 6: Imprime un mensaje que diga 'tu color favorito es {color}'

print("------------------ Ejercicio 6 --------------------")

colores = input("Ingresa tu color favorito es: ") # Pide otra vez el color favorito del usuario
print(f"Tu color favorito es {colores}")



# Ejercicio 7: Preguntale al usuario su animal favorito

print("------------------ Ejercicio 7 --------------------")

animal = input("¿Cual es tu animal favorito? : ") # Pide el animal favorito del usuario
print(f"Tu animal favorito es: {animal}, es muy bonito la verdad")



# Ejercicio 8: Concatena 'nombre' y ciudad' en una sola variable llamada presentacion

print("------------------ Ejercicio 8 --------------------")

nombress = input("Ingresa tu nombre: ") # Pide el nombre completo al usuario
ciudadess = input("Ingresa tu ciudad: ")  # Pide la ciudad donde vive el usuario
presentacion = nombress + " vives en " + ciudadess
print(presentacion) 



# Ejercicio 9: Pide 4 datos al usuario,e imprime el resultado

print("------------------ Ejercicio 9 --------------------")

carro = input("¿Que marca de carro tienes?: ") # Pide la marca del carro que tiene
pais = input("¿De que pais eres?: ") # Pide el pais de nacimiento del usuario
edad = int(input("¿Cual es tu edad?: ")) # Pide la edad del usuario
print(f"Tienes un carro de marca {carro},vienes de {pais},y tienes {edad} años,¡que vida tan lujosa!")



# Ejercicio 10: Pide 5 datos y haz una operacion matematica

print("------------------ Ejercicio 10 --------------------")

num1 = int(input("Ingresa un numero: ")) # Pide un numero entero
num2 = int(input("Ingresa otro segundo numero: ")) # Pide otro numero entero
num3 = int(input("Ingresa otro tercer numero: ")) # Pide otro numero entero
num4 = int(input("Ingresa otro cuarto numero: ")) # Pide otro numero entero
num5 = int(input("Ingresa un quinto y ultimo numero: ")) # Pide otro numero entero
sumatoria = num1+num2+num3+num4+num5
print(f"La suma de: {num1}, {num2}, {num3}, {num4}, {num5} entre si es de: {sumatoria}")



# Ejercicio 11: Crea dos variables 'a = 5' y 'b = 3' y muestra su suma

print("------------------ Ejercicio 11 --------------------")

a = int(input("Ingresa el numero cinco: ")) # Pide el numero entero 5
b = int(input("Ingresa el numero tres: ")) # Pide el numero entero 3
sumatoria_total = a+b
print(f"La suma entre {a} y {b} es igual a: {sumatoria_total}")



# Ejercicio 12: Calcula la resta entre 'a' y 'b'

print("------------------ Ejercicio 12 --------------------")

a2 = int(input("Ingresa un numero: ")) # Pide un numero entero
b2 = int(input("Ingresa otro numero: ")) # Pide otro numero entero
resta_total = a2-b2
print(f"La resta entre {a2} y {b2} es igual a: {resta_total}")



# Ejercicio 13: Multiplica 'a' por 'b'

print("------------------ Ejercicio 13 --------------------")

a3 = int(input("Ingresa un numero: ")) # Pide un numero entero
b3 = int(input("Ingresa otro numero: ")) # Pide otro numero entero
multiplicacion = a3*b3
print(f"La multiplicacion entre {a3} y {b3} es de: {multiplicacion}")



# Ejercicio 14: Divide 'a' entre 'b' y muestra el resultado (asegurate de obtener un numero decimal)

print("------------------ Ejercicio 14 --------------------")

a4 = int(input("Ingrese un numero: ")) # Pide un numero entero
b4 = int(input("Ingrese otro numero: ")) # Pide otro numero entero
division = a4/b4
print(f"La division entre {a4} y {b4} es de: {division}")



# Ejercicio 15: Eleva 'a' a la potencia de 'b'

print("------------------ Ejercicio 15 --------------------")

a5 = int(input("Ingresa un numero: ")) # Pide un numero entero
b5 = int(input("Ingresa otro numero: ")) # Pide otro numero entero
potenciacion = a5**b5
print(f"La potenciacion de {a5} a la {b5} es {potenciacion}")



# Ejercicio 16: Usa 'input' para pedirle al usuario su edad y guardarla como numero entero

print("------------------ Ejercicio 16 --------------------")

edaddd = int(input("Ingresa tu edad: ")) # Pide la edad del usuario
print(f"Tu edad es de {edaddd} años")



# Ejercicio 17: Suma 10 a la edad ingresada y muestra cuantos años tendra

print("------------------ Ejercicio 17 --------------------")

edadddd = int(input("Ingresa tu edad actual: ")) # Pide la edad actual del usuario
año = int(input("Ingresa el año actual: ")) # Pide el año actual
proceso = edadddd + 10 # Suma 10 a la edad actual del usuario
proceso2 = año + 10 # Suma 10 al año actual
print(f"La edad que tendras en 10 años es {proceso} años en el año {proceso2}")



# Ejercicio 18: Pide dos numeros al usuario con input() y muestra su suma

print("------------------ Ejercicio 18 --------------------")

num111 = int(input("Ingresa un numero  entero: ")) # Pide un numero entero
num222 = int(input("Ingresa otro numero entero: ")) # Pide otro numero entero
proceso333 = num111 + num222
print(f"La suma de los dos numeros; {num111} y {num222} es de {proceso333}")



# Ejercicio 19: Calcula el modulo (residuo) de 'a % b'

print("------------------ Ejercicio 19 --------------------")

a = int(input("Ingresa un numero entero: ")) # Pide un numero entero
b = int(input("Ingresa otro numero entero: ")) # Pide otro numero entero
residuo = a%b # El residuo de la division entre los numeros dados por el usuario
print(f"El residuo entre {a} y {b} es de {residuo}")



# Ejercicio 20: Calcula el promedio de tres numeros que ingrese el usuario

print("------------------ Ejercicio 20 --------------------")

numero1111 = int(input("Ingresa el primer numero entero: ")) # Pide un numero entero
numero2222 = int(input("Ingresa el segundo numero entero: ")) # Pide otro numero entero
numero3333 = int(input("Ingresa el tercer numero entero: ")) # Pide otro numero entero
procedimiento1111 = numero1111 + numero2222 + numero3333
procedimiento2222 = procedimiento1111 / 3
print(f"El promedio entre los numeros {numero1111}, {numero2222}, {numero3333} es de: {procedimiento2222}")



# Ejercicio 21: Pide al usuario su nombre completo,guarda la respuesta

print("------------------ Ejercicio 21 --------------------")

names = input("Ingresa tu nombre completo por favor: ") # Pide el nombre completo al usuario
print(f"Tu nombre completo es {names},¡mucho gusto!")

# De la pregunta 22-27 del taller,dicho por el profesor, no se realizan.