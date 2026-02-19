# Desafios de listas,y uso de .append(). Ejercicios y Practicas.

print("----- Desafios de listas y metodos en clase -------")

# Ejercicio 1: Crea una lista vacia llamada frutas. Luego pide al usuario que escriba 3 frutas diferentes y usa .append() para agregarlas a la lista

print("------------------ Ejercicio 1 --------------------")

lista = []
print(lista)

añadir = input("Añade una fruta: ") # Para pedirle la fruta al usuario
añadir2 = input("Añade otra segunda fruta: ") # Para pedirle otra fruta al usuario
añadir3 = input("Añade otra tercera fruta: ") # Para pedirle la fruta final al usuario

lista.append(añadir) # .append() añade la primera fruta al final de la lista
lista.append(añadir2) # .append() añade la segunda  fruta al final de la lista
lista.append(añadir3) # .append() añade la tercera fruta al final de la lista

print(f"Las frutas añadidas fueron {lista[0]}, {lista[1]},y {lista[2]} y en la lista finalmente se veria asi: {lista}")

# Ejercicio 2: Crea una lista vacia llamada edades. Pide al usuario que ingresa 2 edades (numeros enteros y usa .append() para añadirlo a esa lista

print("------------------ Ejercicio 2 --------------------")

edades = []
print(edades)

añadir_edad = int(input("Añade la edad de tu mama: ")) # Para pedirle un numero tipo int al usuario,en este caso la edad de la mama
añadir_edad2 = int(input("Añade la edad de tu abuela: ")) # Para pedirle otro numero tipo int al usuario,en este caso la edad de la abuela

edades.append(añadir_edad) # .append() añade la edad de la mama al final de la lista
edades.append(añadir_edad2) # .append() añade la edad de la abuela al final de la lista

print(f"La edad de tu mama es {edades[0]} años, y la de tu abuela es {edades[1]} años y en la lista final se veria asi: {edades}")

# Ejercicio 3: Pide al usuario que ingrese dos notas (con decimales), guardalas en una lista llamada notas usando .append y muestra el promedio de notas

print("------------------ Ejercicio 3 --------------------")

notas = []
print(notas)

añadir_nota = float(input("Ingresa tu primer nota en matematicas: ")) # Para pedirle un numero tipo float al usuario,en este caso una nota
añadir_nota2 = float(input("Ingresa tu segunda nota en matematicas: ")) # Para pedirle otro numero tipo float al usuario,en este caso una nota

notas.append(añadir_nota) # .append() añade la primera nota de matematicas al final de la lista
notas.append(añadir_nota2) # .append() añade la segunda nota de matematicas al final de la lista

promedio = añadir_nota + añadir_nota2
prom = promedio / 2
notas.append(prom) # .append() añade el promedio de las notas al final de la lista

print(f"Tu primer nota en matematicas es: {notas[0]} y tu segunda tu nota en matematicas es: {notas[1]} y el promedio de tus dos notas es {notas[2]} y en la lista final se veria asi: {notas}")

# Ejercicio 4: Crea una lista llamada productos. Pide al usuario 4 nombres de productos y guardalos con .append(). Imprime tu lista completa

print("------------------ Ejercicio 4 --------------------")

productos = []
print(productos)

añadir_producto = input("Añade un producto: ") # Para pedirle un producto al usuario
añadir_producto2 = input("Añade otro producto: ") # Para pedirle otro producto al usuario
añadir_producto3 = input("Añade otro tercer producto: ") # Para pedirle otro producto al usuario
añadir_producto4 = input("Añade otro cuarto producto: ") # Para pedirle otro producto final al usuario

productos.append(añadir_producto) # .append() añade el primer producto al final de la lista
productos.append(añadir_producto2) # .append() añade el segundo producto  al final de la lista
productos.append(añadir_producto3) # .append() añade el tercer producto al final de la lista
productos.append(añadir_producto4) # .append() añade el cuarto producto  al final de la lista

print(f"Los productos dados por el usuario son {productos[0]},{productos[1]},{productos[2]}, y {productos[3]} y en la lista finalmente seria asi: {productos}")

# Ejercicio 5: Pide al usuario el precio de 3 articulos diferentes (usar float), guardalos en una lista llamada precios, luego imprime la suma total

print("------------------ Ejercicio 5 --------------------")

precios = []
print(precios)

precio1 = float(input("¿Cuanto vale la libra de arroz?: ")) # Para pedirle el precio de la libra de arroz 
precio2 = float(input("¿Cuanto vale una libra de frijoles?:  ")) # Para pedirle el precio de la libra de frijoles 
precio3 = float(input("¿Cuanto vale una salchipapa?: ")) # Para pedirle el precio de la salchipapa
precios.append(precio1) #.append añade el precio de la libra de arroz al final de la lista
precios.append(precio2) #.append añade el precio de la libra de frijoles al final de la lista
precios.append(precio3) #.append añade el precio de la salchipapa al final de la lista
proceso = precio1 + precio2 + precio3

print(f"El precio de la libra de arroz es de: {precios[0]} pesos, el de la libra de frijoles: {precios[1]} pesos y el de la salchipapa es de: {precios[2]} pesos y el valor total de todos los productos es {proceso} pesos y los precios en la lista final se verian asi: {precios} ")

# Ejercicio 6: Pide al usuario que ingrese 4 numeros uno por uno, guardalos con .append() en una lista llamada numeros y luego imprime cual fue el mayor y el menor (usando max() y min())

print("------------------ Ejercicio 6 --------------------")

numeros = []

num1 = int(input("Ingrese un primer numero: ")) # Para pedirle un numero int al usuario
num2 = int(input("Ingrese un segundo numero: ")) # Para pedirle otro numero int al usuario
num3 = int(input("Ingrese el tercer numero: ")) # Para pedirle otro numero int al usuario
num4 = int(input("Ingrese un cuarto numero: ")) # Para pedirle otro numero int al usuario

numeros.append(num1) #.append añade el primer numero al final de la lista
numeros.append(num2) #.append añade el segundo numero al final de la lista
numeros.append(num3) #.append añade el tercer numero al final de la lista
numeros.append(num4) #.append añade el cuarto numero al final de la lista

print(f"el numero mas grande es:  {max(numeros)} y el numero mas chico es:  {min(numeros)}")

# Ejercicio 7: Crea una lista vacia llamada nombres. Pide al usuario que ingrese 2 nombres completos y guardalos con .append(). Luego muestra los nombres con un saludo personalizado, por ejemplo: 'Hola, Juan Perez'.

print("------------------ Ejercicio 7 --------------------")

nombre = []

nombre1 = input("Ingrese un nombre: ") # Para pedirle un nombre al usuario
nombre2 = input("Ingrese otro nombre cualquiera: ") # Para pedirle otro nombre al usuario

nombre.append(nombre1) #.append() agrega el primer nombre al final de la lista
nombre.append(nombre2) #.append() agrega el segundo nombre al final de la lista

print(f"Hola {nombre[0]} y {nombre[1]} mucho gusto conocerlos de mi parte!")

# Ejercicio 8: Crea una lista vacia llamada temperaturas. Pide dos temperaturas y guardalas en la lista con .append(). Luego convierte cada una a Fahrenheit y muestralas.

print("------------------ Ejercicio 8 --------------------")

temperaturas = [] # Lista para los grados centigrados

temp1 = float(input("Ingrese la temperatura exacta actual de Palmira en grados centigrados: ")) # Para pedirle la temperatura en grados centigrados de Palmira
temp2 = float(input("Ingrese la temperatura exacta actual de Cali en grados centigrados: ")) # Para pedirle la temperatura en grados centigrados de Cali

temperaturas.append(temp1) #.append() agrega la temperatura en grados centigrados de Palmira al final de la lista
temperaturas.append(temp2) #.append() agrega la temperatura en grados centigrados de Cali al final de la lista
print(temperaturas)

fahrenheit = temp1 * 1.8 + 32 # Formula para conversion
fahrenheit2 = temp2 * 1.8 + 32 # Formula para conversion

fahrenheits = [] # Lista para los grados centigrados convertidos a Fahrenheit,osea para los grados Fahrenheit

fahrenheits.append(fahrenheit) #.append() agrega los grados centigrados de Palmira convertidos a Fahrenheit al final de la lista Fahrenheit
fahrenheits.append(fahrenheit2)  #.append() agrega los grados centigrados de Cali convertidos a Fahrenheit al final de la lista Fahrenheit

print(fahrenheits)
print(f"La temperatura de Palmira en grados centigrados es de {temperaturas[0]}, pero en Fahrenheit es de {fahrenheits[0]}, y la temperatura de Cali en grados centigrados es de {temperaturas[1]} y en grados Fahrenheit es de {fahrenheits[1]}")