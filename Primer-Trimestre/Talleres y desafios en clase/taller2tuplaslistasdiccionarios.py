# Taller de aplicacion: Listas tuplas diccionarios y operaciones matematicos en python.

print("----- Taller 2: Aplicacion de listas,tuplas y diccionarios -----")

# Ejercicios de practica

# Ejercicio 1: Calculadora de promedio: Solicita al usuario tres calificaciones,almacenalas en una lista y calcula el promedio

print("------------------ Ejercicio 1 --------------------")

lista = []
print(lista)
notanum1 = float(input("Ingresa tu primera nota en Programacion: ")) # Para pedir la primer nota al usuario
notanum2 = float(input("Ingresa tu segunda nota en Programacion: ")) # Para pedir la segunda nota al usuario
notanum3 = float(input("Ingresa tu tercera nota en Programacion: ")) # Para pedir la tercera nota al usuario
proceso = notanum1 + notanum2 + notanum3
proceso1 = proceso/3
lista.append(notanum1) # Para añadir la primer nota al final de la lista
lista.append(notanum2) # Para añadir la sgeunda nota al final de la lista
lista.append(notanum3) # Para añadir la tercera nota al final de la lista
print(f"Las tres notas ingresadas que tienes en programacion fueron: {notanum1}, {notanum2} {notanum3} y su promedio fue {proceso1} y en la lista se veria asi: {lista}")

# Ejercicio 2: Actualizar precios: Crea un diccionario con tres productos y sus precios. Luego,pide al usuario que aumente un porcentaje a cada precio

print("------------------ Ejercicio 2 --------------------")

precios = {
 "Uva": 1000,
    "Fresa": 2500,
      "Lulo": 3000
}
print(precios)
porcentaje = float(input("Ingresa el aumento porcentual al precio: ")) # Para pedirle el numero/porcentual que quiere aumentar a los precios
precios["Uva"] += precios["Uva"] * (porcentaje/100) # Para al precio actual de la uva sumarle (+=) el porcentaje que ingreso el usuario
precios["Fresa"] += precios["Fresa"] * (porcentaje/100)  # Para al precio actual de la fresa sumarle (+=) el porcentaje que ingreso el usuario
precios["Lulo"] += precios["Lulo"] * (porcentaje/100) # Para al precio actual del lulo sumarle (+=) el porcentaje que ingreso el usuario
print(f"El diccionario con los precios aumentados en un {porcentaje}% es:{precios}")


# Ejercicio 3:  Conversor de temperaturas: Guarda en una tupla las temperaturas en grado Celsius de 5 días. Convierte cada una a Fahrenheit y muéstralas.

print("------------------ Ejercicio 3 --------------------")

temperaturas = ()
temp1 = float(input("Ingresa la temperatura en grados celsius del lunes en palmira: ")) # Para pedirle la temperatura en grados celsius del lunes en Palmira al usuario
temp2 = float(input("Ingresa la temperatura en grados celsius del martes en palmira: ")) # Para pedirle la temperatura en grados celsius del martes en Palmira al usuario
temp3 = float(input("Ingresa la temperatura en grados celsius del miercoles en palmira:  ")) # Para pedirle la temperatura en grados celsius del miercoleses en Palmira al usuario
temp4 = float(input("Ingresa la temperatura en grados celsius del jueves en palmira:  ")) # Para pedirle la temperatura en grados celsius del jueves en Palmira al usuario
temp5 = float(input("Ingresa la temperatura en grados celsius del viernes en palmira:  ")) # Para pedirle la temperatura en grados celsius del viernes en Palmira al usuario
lista = list(temperaturas) # Para pasar a lista la tupla para modificarla
fahrenheit2 = temp1* 9/5 + 32 # Conversion de grados centigrados a fahrenheit del lunes en Palmira
fahrenheit22 = temp2* 9/5 + 32 # Conversion de grados centigrados a fahrenheit del martes en Palmira
fahrenheit222 = temp3 * 9/5 + 32 # Conversion de grados centigrados a fahrenheit del miercoles en Palmira
fahrenheit2222 = temp4 * 9/5 +32 # Conversion de grados centigrados a fahrenheit del jueves en Palmira
fahrenheit22222 = temp5 * 9/5 + 32 # Conversion de grados centigrados a fahrenheit del viernes en Palmira
lista.append(fahrenheit2) # Para añadir los grados fahrenheit finales convertidos del lunes en Palmira
lista.append(fahrenheit22) # Para añadir los grados fahrenheit finales convertidos del martes en Palmira
lista.append(fahrenheit222) # Para añadir los grados fahrenheit finales convertidos del miercoles en Palmira
lista.append(fahrenheit2222) # Para añadir los grados fahrenheit finales convertidos del jueves en Palmira
lista.append(fahrenheit22222) # Para añadir los grados fahrenheit finales convertidos del viernes en Palmira
tupla_final = tuple(lista) # Para convertir la lista a la tupla final
print(f"Las temperaturas en grados celsius convertidas a Fahrenheit de la semana en Palmira son: 'Lunes,Martes,Miercoles,Jueves,Viernes' y en la tupla final son asi: {tupla_final}")



# Ejercicio 4: Edad promedio con listas: Pide al usuario cinco edades, almacénalas en una lista y muestra cuál es la mayor, menor y el promedio.

print("------------------ Ejercicio 4 --------------------")

edades = []
edad1 = int(input("Ingresa la edad de tu primer hermano: ")) # Para pedirle la edad del primer hermano
edad2 = int(input("Ingresa la edad de tu segundo hermano: ")) # Para pedirle la edad del segundo hermano
edad3 = int(input("Ingresa la edad de tu tercer hermano: ")) # Para pedirle la edad del tercer hermano
edad4 = int(input("Ingresa la edad de tu cuarto hermano: ")) # Para pedirle la edad del cuarto hermano
edad5 = int(input("Ingresa la edad de tu quinto hermano: ")) # Para pedirle la edad del quinto hermano
edades.append(edad1) # Para añadir la edad del primer hermano al final de la lista
edades.append(edad2) # Para añadir la edad del segundo hermano al final de la lista
edades.append(edad3) # Para añadir la edad del tercer hermano al final de la lista
edades.append(edad4) # Para añadir la edad del cuarto hermano al final de la lista
edades.append(edad5) # Para añadir la edad del quinto hermano al final de la lista
proceso = (edad1 + edad2 + edad3 + edad4 + edad5) / 5
print(f"La lista resultante es: {edades},y el promedio de las edades es: {proceso} y la mayor edad de la lista es {max(edades)} y la edad menor es {min(edades)}")


# Ejercicio 5: Diccionario de frutas: Crea un diccionario con tres frutas y sus precios por kilo Luego, pide al usuario la cantidad en kilos que desea de cada una y calcula el total a pagar.

print("------------------ Ejercicio 5 --------------------")


frutas = {
    "papa": 5600,
    "tomate": 5000,
    "lechuga": 7000
}
cantidad1 = float(input("Ingresa la cantidad de kilos que deseas para la papa: ")) # Pedirle la cantidad de kilos de la papa
cantidad2 = float(input("Ingresa la cantidad de kilos que deseas para el tomate: ")) # Pedirle la cantidad de kilos del tomate
cantidad3 = float(input("Ingresa la cantidad de kilos que deseas para la lechuga: ")) # Pedirle la cantidad de kilos de la lechuga
pedido1 = cantidad1 * frutas["papa"] # Multiplicar la cantidad de papa por el precio de la papa actualmente
pedido2 = cantidad2 * frutas["tomate"] # Multiplicar la cantidad del tomate por el precio del tomate actualmente
pedido3 = cantidad3 * frutas["lechuga"] # Multiplicar la cantidad de lechuga por el precio de la lechuga actualmente
sumatoria = pedido1 + pedido2 + pedido3
print(f"El precio a pagar de papa por los {cantidad1} kilos es {pedido1},el precio a pagar de tomate por los {cantidad2} kilos es {pedido2} y el precio a pagar de lechuga de {cantidad3} de kilos es {pedido3} y el total a pagar completo entre todo es: {sumatoria} pesos")

# Ejercicio 6: Suma de elementos en tupla: Define una tupla con cinco números. Muestra la suma total de sus elementos


print("------------------ Ejercicio 6 --------------------")


numeros = ()
lista = list(numeros)
num1 = int(input("Ingresa el numero 1: ")) # Pedir el numero int 1 
num2 = int(input("Ingresa el numero 2: ")) # Pedir el numero int 2 
num3 = int(input("Ingresa el numero 3: ")) # Pedir el numero int 3
num4 = int(input("Ingresa el numero 4: ")) # Pedir el numero int 4 
num5 = int(input("Ingresa el numero 5: ")) # Pedir el numero int 5 
lista.append(num1) # Añadir el primer numero al final de la lista
lista.append(num2) # Añadir el segundo numero al final de la lista
lista.append(num3) # Añadir el tercer numero al final de la lista
lista.append(num4) # Añadir el cuarto numero al final de la lista
lista.append(num5) # Añadir el quinto numero al final de la lista
tupla_final = tuple(lista) # Pasar la lista a la tupla final
suma = num1+num2+num3+num4+num5
print(f"La tupla final con los 5 numeros dados por el usuario es: {tupla_final} y la suma de estos numeros es: {suma}")

# Ejercicio 7: Inventario con lista de diccionarios: Pide al usuario que ingrese nombre, cantidad y precio de tres productos. Almacénalos como diccionarios dentro de una lista y muestra el total del inventario.

print("------------------ Ejercicio 7 --------------------")


# Ingreso de datos de tres productos

producto1 = {
    "nombre": input("Nombre del producto 1: "), # Para pedir el nombre
    "cantidad": float(input("Cantidad del producto 1: ")), # Para pedir la cantidad
    "precio": float(input("Precio del producto 1: ")) # Para pedir el precio actual
}

producto2 = {
    "nombre": input("Nombre del producto 2: "), # Para pedir el nombre
    "cantidad": float(input("Cantidad del producto 2: ")), # Para pedir la cantidad
    "precio": float(input("Precio del producto 2: ")) # Para pedir el precio actual
}

producto3 = {
    "nombre": input("Nombre del producto 3: "), # Para pedir el nombre
    "cantidad": float(input("Cantidad del producto 3: ")), # Para pedir la cantidad
    "precio": float(input("Precio del producto 3: ")) # Para pedir el precio actual
}

# Lista de productos

inventario = [producto1, producto2, producto3] # Para crear la lista con todos los datos de cada producto

# Cálculo del total del inventario (cantidad × precio por cada producto)

total = (producto1["cantidad"] * producto1["precio"]) # Para multiplicar la cantidad por el precio del producto 1 y hallar el total
total1 = (producto2["cantidad"] * producto2["precio"]) # Para multiplicar la cantidad por el precio del producto 2 y hallar el total
total2 = (producto3["cantidad"] * producto3["precio"]) # Para multiplicar la cantidad por el precio del producto 3 y hallar el total

#  Mostrar el total

print(f"El valor total del inventario del producto 1 {producto1["nombre"]} es: ${total}")
print(f"El valor total del inventario del producto 2 {producto2["nombre"]} es: ${total1}")
print(f"El valor total del inventario del producto 3 {producto3["nombre"]} es: ${total2}")

# Ejercicio 8: Modificar una lista de precios: Crea una lista con cinco precios. Pide al usuario un descuento (en porcentaje) y aplícalo a todos los precios.

print("------------------ Ejercicio 8 --------------------")

# Lista original de precios

precios = [1000, 2500, 3500, 5000, 8000]

#  Solicitar descuento al usuario

descuento = float(input("Ingresa el descuento en porcentaje (por ejemplo, 10 para 10%): ")) # Pedir al usuario el numero porcentual de descuento 

#  Cálculo del factor de descuento

factor = 1 - (descuento / 100) # Para hallar el porcentaje que ingreso el usuario

#  Aplicar descuento a cada precio

precios_con_descuento = [
     precios[0] * factor,  # Para multiplicar el precio por el descuento 
     precios[1] * factor,  # Para multiplicar el precio por el descuento 
     precios[2] * factor,  # Para multiplicar el precio por el descuento 
     precios[3] * factor,  # Para multiplicar el precio por el descuento 
     precios[4] * factor  # Para multiplicar el precio por el descuento 
 ]

#  Mostrar precios con descuento

print(f"Precios originales: {precios}")
print(f"Precios con {descuento}% de descuento: {precios_con_descuento}")


# Ejercicio 9: Notas con tuplas: Solicita al usuario una tupla con cuatro notas. Muestra la nota más alta y la más baja.


print("------------------ Ejercicio 9 --------------------")

# Solicitar las notas al usuario en float

nota1 = float(input("Ingresa la nota 1: ")) # Pide la primera nota
nota2 = float(input("Ingresa la nota 2: ")) # Pide la segunda nota
nota3 = float(input("Ingresa la nota 3: ")) # Pide la tercera nota
nota4 = float(input("Ingresa la nota 4: ")) # Pide la cuarta nota

#  Crear tupla con las notas

notas = (nota1, nota2, nota3, nota4) # Para crear la tupla con todas las notas y no tener que pasarla a la lista para modificarla
print(notas)

# Obtener la nota más alta y más baja

mayor = max(notas) # Para hallar la nota mas alta 
menor = min(notas) # Para hallar la nota menos alta o mas baja

# Mostrar resultados

print(f"La nota más alta de la tupla es: {mayor}")
print(f"La nota más baja de la tupla es: {menor}")


# Ejercicio 10: Diccionario de conversiones: Crea un diccionario que tenga como claves "km","m", "cm" y como valores su equivalencia en metros. Permite al usuario convertir una cantidad desde alguna unidad a metros

print("------------------ Ejercicio 10 --------------------")


#  Diccionario de equivalencias a metros

conversiones = {
     "km": 1000, # Valor del km en metros
     "m": 1, # Valor del m en metros
     "cm": 0.01 # Valor del cm en metros
 }

#  Solicitar unidad y cantidad al usuario

unidad = input("Ingresa la unidad (km, m o cm) escribalo tal cual por favor: ") # Para pedir la unidad que desea convertir
cantidad = float(input("Ingresa la cantidad a convertir: ")) # Para pedir la cantidad de la unidad

# Calcular la conversión

resultado = cantidad * conversiones[unidad] # Para multiplicar la cantidad por la unidad,ya que [unidad] busca en el diccionario la unidad que escribio el usuario

# Mostrar resultado

print(f"{cantidad} {unidad} equivalen a {resultado} metros.")



# Ejercicio 11: Lista de productos más IVA: Pide al usuario una lista de precios. Luego crea una nueva lista con el precio más el 19% de IVA

print("------------------ Ejercicio 11 --------------------")

# Entrada de precios individuales

precio1 = float(input("Ingresa el precio del producto 1: ")) # Para pedir el precio del producto 1
precio2 = float(input("Ingresa el precio del producto 2: ")) # Para pedir el precio del producto 2
precio3 = float(input("Ingresa el precio del producto 3: ")) # Para pedir el precio del producto 3

# Lista original de precios

precios = [precio1, precio2, precio3] # Crear la lista con los precios dados por el usuario

# Cálculo del 19% de IVA por cada precio

precios_con_iva = [
    precios[0] * 1.19, # Para multiplicar el precio del producto 1 por el 19% de IVA
    precios[1] * 1.19, # Para multiplicar el precio del producto 2 por el 19% de IVA
    precios[2] * 1.19 # Para multiplicar el precio del producto 3 por el 19% de IVA
]

# Mostrar ambas listas

print(f"Precios originales: {precios}")
print(f"Precios con IVA (19%): {precios_con_iva}")


# Ejercicio 12: Tupla de operaciones matemáticas: Pide al usuario dos números. Guarda en una tupla la suma, resta, multiplicación y división entre ellos

print("------------------ Ejercicio 12 --------------------")

# Solicitar dos números al usuario

num1 = float(input("Ingresa el primer número: ")) # Para pedir el primer numero 
num2 = float(input("Ingresa el segundo número: ")) # Para pedir un segundo numero

# Crear una tupla con las operaciones básicas

operaciones = (
    num1 + num2,   # Suma
    num1 - num2,   # Resta
    num1 * num2,   # Multiplicación
    num1 / num2    # División
)

# Mostrar resultados

print(f"Resultados en tupla (suma, resta, multiplicación, división): {operaciones}")


# Ejercicio 13: . Diccionario de estudiantes: Crea un diccionario donde las claves sean nombres de estudiantes y los valores sus notas. Calcula el promedio general.

print("------------------ Ejercicio 13 --------------------")


# Ingreso de nombres y notas

estudiantes = {
    input("Nombre del estudiante 1: "): float(input("Nota del estudiante 1: ")), # Para pedir el nombre y la nota y que el nombre sea la clave y su nota el valor ya que la clave siempre va primero con los :
    input("Nombre del estudiante 2: "): float(input("Nota del estudiante 2: ")), # Para pedir el nombre y la nota y que el nombre sea la clave y su nota el valor ya que la clave siempre va primero con los :
    input("Nombre del estudiante 3: "): float(input("Nota del estudiante 3: ")) # Para pedir el nombre y la nota y que el nombre sea la clave y su nota el valor ya que la clave siempre va primero con los :
}

# Acceso directo a las notas

notas = list(estudiantes.values()) #.values() agarra el valor de las claves que estan

# Cálculo del promedio general

promedio = (notas[0] + notas[1] + notas[2]) / 3

# Mostrar resultados

print(f"Diccionario de estudiantes: {estudiantes}")
print(f"Promedio general: {promedio}")


# Ejercicio 14:  Lista de salarios: Pide al usuario cinco salarios. Aplícales un aumento del 10% y guarda los nuevos valores en otra lista.

print("------------------ Ejercicio 14 --------------------")



# Solicitar cinco salarios al usuario

sal1 = float(input("Ingresa el salario 1: ")) # Pedir el primer salario
sal2 = float(input("Ingresa el salario 2: ")) # Pedir el segundo salario
sal3 = float(input("Ingresa el salario 3: ")) # Pedir el tercer salario
sal4 = float(input("Ingresa el salario 4: ")) # Pedir el cuarto salario
sal5 = float(input("Ingresa el salario 5: ")) # Pedir el quinto salario

# Lista original de salarios

salarios = [sal1, sal2, sal3, sal4, sal5] # Para crear la lista con todos los salarios del usuario

# Lista de salarios con el 10% de aumento
aumentados = [
    salarios[0] * 1.10, # Para aumentar el salario 1 un 10%
    salarios[1] * 1.10, # Para aumentar el salario 2 un 10%
    salarios[2] * 1.10, # Para aumentar el salario 3 un 10%
    salarios[3] * 1.10, # Para aumentar el salario 4 un 10%
    salarios[4] * 1.10 # Para aumentar el salario 5 un 10%
]

# Mostrar resultados

print(f"Salarios originales: {salarios}")
print(f"Salarios con aumento del 10%: {aumentados}")


# Ejercicio 15: Diccionario de impuestos: Guarda productos con su precio sin impuesto. Pide al usuario el porcentaje de impuesto y calcula el precio final para cada uno.

print("------------------ Ejercicio 15 --------------------")

# Diccionario con productos y precios sin impuesto

productos = {
    "Manzanas": 3000,
    "Pan": 2500,
    "Leche": 4000
}

# Solicitar al usuario el porcentaje de impuesto

impuesto = float(input("Ingresa el porcentaje de impuesto (ejemplo: 19): ")) # Para pedir el porcentaje de impuesto 
factor = 1 + (impuesto / 100) # Para sumar 1 (precio original) al numero que dio el usuario dividido 100,osea el porcentaje; Sumar el precio original (1) mas el porcentaje (impuesto)

# Calcular precios finales

precios_finales = {
    "Manzanas": productos["Manzanas"] * factor, # Para multiplicar el valor actual de la manzana por el porcentaje (factor)
    "Pan": productos["Pan"] * factor, # Para multiplicar el valor actual del pan por el porcentaje (factor)
    "Leche": productos["Leche"] * factor # Para multiplicar el valor actual de la leche por el porcentaje (factor)
}

# Mostrar resultados

print(f"Precios sin impuesto: {productos}")
print(f"Precios con {impuesto}% de impuesto: {precios_finales}")


# Ejercicio 16: Análisis de lista de edades: Solicita al usuario una lista de edades. Luego indica cuántos son mayores de edad y cuántos no.

print("------------------ Ejercicio 16 --------------------")

# Solicitar edades una por una

e1 = int(input("Ingresa la edad 1: ")) # Para pedir la primera edad
e2 = int(input("Ingresa la edad 2: ")) # Para pedir la segunda edad
e3 = int(input("Ingresa la edad 3: ")) # Para pedir la tercera edad
e4 = int(input("Ingresa la edad 4: ")) # Para pedir la cuarta edad
e5 = int(input("Ingresa la edad 5: ")) # Para pedir la quinta edad

# Lista de edades

edades = [e1, e2, e3, e4, e5] # Para crear la lista con cada una de las edades

# Cálculo manual (1 si es mayor de edad, 0 si no)

mayores = (e1 >= 18) + (e2 >= 18) + (e3 >= 18) + (e4 >= 18) + (e5 >= 18) # Si es mayor o igual a 18 es 1 (True) pero si es menor edad es 0 (False)
menores = 5 - mayores # Se resta 5 (el total de edades) - la suma de los 1 (True)

# Mostrar resultados

print(f"Edades ingresadas: {edades}")
print(f"Mayores de edad: {mayores}")
print(f"Menores de edad: {menores}")


# Ejercicio 17: Tupla de conversiones de moneda: Crea una tupla con los valores de una cantidad en dólares convertida a euros, pesos y yenes, usando tasas fijas.

print("------------------ Ejercicio 17 --------------------")

# Solicitar cantidad en dólares

dolares = float(input("Ingresa la cantidad en dólares (USD): ")) # Para pedir la cantidad en dolares (USD)

# Tasas fijas de conversión

tasa_euro = 0.85     # 1 USD = 0.85 EUR
tasa_peso = 4000     # 1 USD = 4000 COP
tasa_yen = 110       # 1 USD = 110 JPY

# Crear la tupla con los valores convertidos

conversiones = (
    dolares * tasa_euro,  # Para convertir los dolares del usuario a Euros (EUR)
    dolares * tasa_peso,  # Para convertir los dolares del usuario a Pesos colombianos (COP)
    dolares * tasa_yen    # Para convertir los dolares del usuario a Yenes (JPY)
)

# Mostrar resultados

print(f"Tupla de conversiones desde ${dolares} USD:")
print(f"(Euros, Pesos Colombianos, Yenes): {conversiones}")


# Ejercicio 18:  Diccionario de ventas: Pide al usuario registrar la venta de tres productos (nombre y cantidad). Luego muestra el total de unidades vendidas.

print("------------------ Ejercicio 18 --------------------")

# Solicitar nombre y cantidad de tres productos

producto1 = input("Nombre del producto 1: ") # Para pedir el nombre del producto 1 
cantidad1 = int(input(f"Cantidad vendida de {producto1}: ")) # Para pedir la cantidad de unidades vendidas del producto 1

producto2 = input("Nombre del producto 2: ") # Para pedir el nombre del producto 2 
cantidad2 = int(input(f"Cantidad vendida de {producto2}: ")) # Para pedir la cantidad de unidades vendidas del producto 2

producto3 = input("Nombre del producto 3: ") # Para pedir el nombre del producto 3
cantidad3 = int(input(f"Cantidad vendida de {producto3}: ")) # Para pedir la cantidad de unidades vendidas del producto 3

# Crear diccionario con las ventas

ventas = {
    producto1: cantidad1, # Para que el producto 1 sea la clave y las unidades vendidas el valor 
    producto2: cantidad2, # Para que el producto 2 sea la clave y las unidades vendidas el valor 
    producto3: cantidad3 # Para que el producto 3 sea la clave y las unidades vendidas el valor 
}

# Calcular total de unidades vendidas

total_unidades = ventas[producto1] + ventas[producto2] + ventas[producto3] # Para sumar los valores de cada producto,osea las unidades vendidas de todos 

# Mostrar resultados

print(f"Ventas registradas: {ventas}")
print(f"Total de unidades vendidas: {total_unidades}")

# Ejercicio 19: Lista de temperaturas extremas: Crea una lista con diez temperaturas. Muestra cuáles superan los 30 grados y cuáles están por debajo de 10.

print("------------------ Ejercicio 19 --------------------")

# Ingreso de 10 temperaturas

t1 = float(input("Temperatura 1: ")) # Para pedir la temperatura 1
t2 = float(input("Temperatura 2: ")) # Para pedir la temperatura 2
t3 = float(input("Temperatura 3: ")) # Para pedir la temperatura 3
t4 = float(input("Temperatura 4: ")) # Para pedir la temperatura 4
t5 = float(input("Temperatura 5: ")) # Para pedir la temperatura 5
t6 = float(input("Temperatura 6: ")) # Para pedir la temperatura 6
t7 = float(input("Temperatura 7: ")) # Para pedir la temperatura 7
t8 = float(input("Temperatura 8: ")) # Para pedir la temperatura 8
t9 = float(input("Temperatura 9: ")) # Para pedir la temperatura 9
t10 = float(input("Temperatura 10: ")) # Para pedir la temperatura 10

# Lista original de temperaturas

temperaturas = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10] # Crear la lista con todas las temperaturas

# Crear listas separadas con comparaciones lógicas directas

mayores_30 = [
    t1 * (t1 > 30), # Si t1 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t1 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t2 * (t2 > 30), # Si t2 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t2 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t3 * (t3 > 30), # Si t3 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t3 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t4 * (t4 > 30), # Si t4 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t4 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t5 * (t5 > 30), # Si t5 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t5 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t6 * (t6 > 30), # Si t6 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t6 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t7 * (t7 > 30), # Si t7 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t7 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t8 * (t8 > 30), # Si t8 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t8 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t9 * (t9 > 30), # Si t9 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t9 dado por el usuario  pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
    t10 * (t10 > 30) # Si t10 es mayor a 30 mostrara 1 (True) lo que se multiplicara luego por el valor de t10 dado por el usuario pero si no lo es dara cero ya que t10 se multplicara por 0 (False)
]

menores_10 = [
    t1 * (t1 < 10), # Si t1 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t1 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t2 * (t2 < 10), # Si t2 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t2 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t3 * (t3 < 10), # Si t3 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t3 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t4 * (t4 < 10), # Si t4 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t4 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t5 * (t5 < 10), # Si t5 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t5 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t6 * (t6 < 10), # Si t6 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t6 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t7 * (t7 < 10), # Si t7 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t7 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t8 * (t8 < 10), # Si t8 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t8 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t9 * (t9 < 10), # Si t9 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t9 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
    t10 * (t10 < 10) # Si t10 es menor a 10 mostrara 1 (True) lo que se multplicara luego por el valor de t10 dado por el usuario y si no lo es dara cero ya que t1 se multiplicara por 0 (False)
]

# Filtrar ceros usando sumas (sin condicionales) o simplemente mostrar las listas

print(f"Temperaturas ingresadas: {temperaturas}")
print(f"Temperaturas mayores a 30°C: {mayores_30}")
print(f"Temperaturas menores a 10°C: {menores_10}")

# Ejercicio 20: Actualizar precios con métodos de listas: Crea una lista con cinco precios. Permite que el usuario elimine uno, agregue otro, y luego muestra la lista ordenada de menor a mayor.

print("------------------ Ejercicio 20 --------------------")

# Lista inicial de precios

precios = [1500, 3000, 2500, 4000, 1000] # Lista con los precios

# Mostrar lista original

print(f"Lista original: {precios}") # Para que el usuario vea cual precio quiere eliminar

# Eliminar un precio (el usuario ingresa cuál eliminar exactamente)

precio_a_eliminar = float(input("Ingresa el precio que deseas eliminar: ")) # Para que el usuario elimine ese precio de la lista
precios.remove(precio_a_eliminar) # Para remover la primera aparicion del precio que puso el usuario

# Agregar un nuevo precio

precio_nuevo = float(input("Ingresa el nuevo precio que deseas agregar: "))  # Para que el usuario luego decida cual precio quiere agregar a la lista
precios.append(precio_nuevo) # Para agregar al final de la lista el precio que dio el usuario

print(f"La lista con el precio eliminado y agregado seria asi: {precios}") # Para mostrar la lista sin el precio eliminado y con el precio agregado

# Ordenar la lista de menor a mayor

precios.sort() # Para ordenarla de menor a mayor

# Mostrar la lista final

print(f"Lista actualizada y ordenada de menor a mayor: {precios}")