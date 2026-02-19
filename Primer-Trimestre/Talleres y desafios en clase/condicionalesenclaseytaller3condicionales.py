# Ejercicios de condicionales en clase

print("--- Ejercicios de condicionales en clase ---")

# Ejercicio 1: Verificar si un numero es positivo,negativo o es cero

print("------------------ Ejercicio 1 --------------------")

numero1 = float(input("Ingresa un numero: ")) # Para pedir el numero

if numero1 > 0: # Para saber si es positivo siendo mayor a cero
    print(f"El numero 1 ({numero1}) es mayor que cero osea es positivo ") 

elif numero1 < 0: # Para saber si es negativo siendo menor a cero
    print(f"El numero 1 ({numero1}) es menor que cero osea es negativo")

else: # Para saber si las anterios condiciones no se cumplen; Donde seria cero
    print(f"El numero 1 ({numero1}) es 0")

# Ejercicio 2: Calcula el mayor de dos numeros ingresados

print("------------------ Ejercicio 2 --------------------")

num1 = float(input("Ingresa un numero 1: ")) # Para pedir el numero 1
num2 = float(input("Ingresa un numero 2: ")) # Para pedir el numero 2

if num1 > num2: # Si el numero 1 es mayor al numero dos
    print(f"El numero 1 ({num1}) es mayor que el numero 2 ({num2})")

elif num2 > num1: # Si el numero 2 es mayor al numero uno
    print(f"El numero 2 ({num2}) es mayor que el numero 1 ({num1})")

else: # Si las dos condiciones no se cumplen; Donde ambos numeros serian iguales
    print(f"Los numeros ({num1}), ({num2}) son iguales")

# Ejercicio 3: Determina si un numero es par o impar

print("------------------ Ejercicio 3 --------------------")

num11 = float(input("Ingresa un numero 1: ")) # Para pedir el numero 
numero = 2 
if num11 % numero == 0: # Para saber si el residuo del numero al dividirlo por 2 es 0; Siendo par
    print(f"El numero ({num11}) es par")

else:  # Para saber si la condicion no se cumple y tiene residuo diferente a 0; Siendo impar
    print(f"El numero ({num11}) no es par")


# Ejercicio 4: Dado un numero verifica si esta entre 10 y 20

print("------------------ Ejercicio 4 --------------------")

num22 = float(input("Ingresa un numero: ")) # Para pedir el numero 

if num22 >= 10 and num22 <= 20: # Para saber si el numero esta entre 10 a 20,incluyendo esos dos numeros
    print(f"El numero ({num22}) esta entre 10 y 20")

else: # Para saber si la condicion no se cumple; Siendo un numero fuera del rango entre 10 a 20
    print(f"El numero ({num22}) no esta entre 10 y 20")

# Ejercicio 5: Dados tres numeros,encuentra el mayor usando condicionales

print("------------------ Ejercicio 5 --------------------")

num_uno = float(input("Ingresa un primer numero, no puede ser igual al otro: ")) # Para pedir el numero 
num_dos = float(input("Ingresa un segundo numero, no puede ser igual al otro: ")) # Para pedir un segundo numero
num_tres = float(input("Ingresa un tercer numero, no puede ser igual al otro: ")) # Para pedir un tercer y final numero

if num_uno > num_dos and num_uno > num_tres: # Para saber si el numero uno es mayor a los dos numeros
    print(f"El número mayor es: {num_uno}")

elif num_dos > num_uno and num_dos > num_tres: # Para saber si el numero dos es mayor a los dos numeros
    print(f"El número mayor es: {num_dos}")

elif num_tres > num_uno and num_tres > num_dos: # Para saber si el numero tres es mayor a los dos numeros
    print(f"El número mayor es: {num_tres}")

else: # Para saber si hay dos numeros iguales; Donde falla ya que se pide que no sean iguales
    print("Hay al menos dos números iguales,ingresa otra vez los numeros por favor")

# Ejercicio 6: Calcula el precio final con un 10% de descuento si el total es mayor a 100$

print("------------------ Ejercicio 6 --------------------")

precio = float(input("¿A cuanto esta el precio de la papa actualmente?: ")) # Para pedir el precio actual del producto

if precio > 100: # Para aplicarle un 10 % de descuento al producto si su precio es mayor que 100$
    prod = precio * 0.10
    preciofinal = precio - prod
    print(f"El precio final con el 10% de descuento de {precio}$ de la papa  es {preciofinal}$")

else:  # Para no dar ningun descuento al producto si su precio no es mayor que 100 $
    print(f"El producto esta en menos que 100$,es un buen precio y no se le hara descuento")

# Ejercicio 7: Verifica si una persona puede votar (mayor o igual a 18 años)

print("------------------ Ejercicio 7 --------------------")

edad = int(input("Ingresa tu edad actual: ")) # Pára pedir la edad del usuario

if edad >= 18: # Para saber si es mayor de edad; Que si podria votar
    print(f"Puedes votar ya que tienes {edad} años,que bueno!")

else: # Para saber si es menor de edad; Que no podria votar
    print(f"Aun no puedes votar ya que tienes {edad} años")

# Ejercicio 8: Dado el precio y tipo de cliente (VIP o normal),aplica un descuento del 20% solo a VIP

print("------------------ Ejercicio 8 --------------------")

cliente = input("Eres un cliente VIP o Normal,se sincero y ponlo exactamente igual,el precio de la entrada es 200: ") # Para pedir el tipo de cliente
precio = 200
if cliente == "VIP": # Para hacerle un 20% de descuento al cliente en caso de que sea un cliente VIP
    primero = precio * 0.20
    segundo = precio - primero
    print(f"El precio final con el 20% de descuento por ser VIP es: {segundo}$ teniendo en cuenta que el precio actual es: {precio}$")

else: # Para no aplicar ningun descuento al cliente ya que no es VIP
    print(f"No eres VIP,por lo tanto el total que debes pagar por entrar es: {precio}$")

# # Ejercicio 9: Determina si un numero es multiplo de 5 y de 3 al mismo tiempo

print("------------------ Ejercicio 9 --------------------")

numero = float(input("Ingresa un numero el cual creas que es multiplo de 5 y 3 al mismo tiempo: ")) # Para pedir un numero el cual sea multiplo de 5 y 3 al mismo tiempo

if numero % 3 == 0 and numero % 5 == 0: # Para saber si es multiplo de 5 y 3 al mismo tiempo si la division de ese numero entre 5 y 3 da como residuo 0
    print(f"El numero {numero} si es multiplo de 5 y 3")

else: # Si no es multiplo de 5  y 3 al mismo tiempo
    print(f"El numero {numero} no es multiplo de 5 y 3")

# Ejercicio 10: Dado un numero,verifica si es divisibe entre dos numeros dados 

print("------------------ Ejercicio 10 --------------------")

numero = int(input("Ingresa el número principal: ")) # Pedir un numero principal
div1 = int(input("Ingresa el primer divisor: ")) # Pedir un numero como divisior del numero principal
div2 = int(input("Ingresa el segundo divisor: ")) # Pedir otro numero como divisior del numero principal

if numero % div1 == 0 and numero % div2 == 0: # Para saber si el numero principal es divisible entre los dos divisores dados por el usuario
    print(f"{numero} es divisible entre {div1} y {div2}")

elif numero % div1 == 0: # Para saber si el numero principal es divisible entre el primer divisor dado por el usuario
    print(f"{numero} solo es divisible entre {div1}")

elif numero % div2 == 0: # Para saber si el numero principal es divisble entre el segundo divisor dado por el usuario
    print(f"{numero} solo es divisible entre {div2}")

else: # Por si no es divisible el numero principal entre los dos divisores dados por el usuario
    print(f"{numero} no es divisible entre ninguno de los dos")


# Taller de condicionales en clase

print("---- Taller numero 3: Condicionales en clase ------")

# 1 - Pide tu edad y muestra si eres menor de edad,mayor de edad o adulto mayor (65+)

print("------Ejercicio 1 ------")

edadd = int(input("Ingresa tu edad: ")) # Para pedir la edad al usuario

if edadd < 18: # Si el usuario es menor de edad
    print(f"Eres menor de edad por que tienes menos de 18 años")

elif edadd < 65: # Si el usuario es mayor de edad
    print(f"Eres mayor de edad por que tienes mas de 18 años,felicidades! :)")

else: # Si el usuario tiene mas de 65 años; Siendo 'adulto mayor'
    print(f"Eres un adulto mayor,estas ya viejo por que tienes mas de 65 años :(")

# 2 -  Solicita tu estatura en metros. Si mide menos de 1.5 m, eres considerado bajo; entre 1.5 y 1.8 m, estatura media; más de 1.8 m, alto

print("------Ejercicio 2 ------")

estatura = float(input("Ingresa tu estatura actual por favor: ")) # Pedir la estatura actual
if estatura < 1.5: # Si es menor a 1.5 metros
    print(f"Eres bajo,lo sentimos,en un años crecerás! :)")
elif estatura >= 1.5  and estatura <= 1.8: # Si esta entre 1.5 a 1.8 m
    print(f"Eres considera con una estatura media,felicidades estas en una altura promedia! :)")
else: # Si es mas de 1.8
    print(f"Eres considera alto,felicitaciones! :)")

# 3 - Ingresa un número y muestra si es múltiplo de 2, de 3, o de ninguno.

print("------Ejercicio 3 ------")

numero = int(input("Ingresa un numero por el cual creas que es multiplo de 2 y 3: "))


if numero % 2 == 0 and numero % 3 == 0: # Si el numero es divisible siendo multiplo por 2 y el 3
    print(f"El numero {numero} si es multiplo de 3 y de 2")
elif numero % 2 == 0: # Si solo es multiplo de 2
    print(f"El numero {numero} solo es multiplo de 2")
elif numero % 3 == 0: # Si solo es multiplo de 3
    print(f"El numero {numero} solo es multiplo de 3")
else: # Si no es multiplo de ninguno
    print(f"El numero {numero} no es multiplo ni de 3 ni de 2")

# 4 -Pide un número decimal y determina si tiene 1, 2 o más de 2 decimales (usa str() y split()).

print("------Ejercicio 4 ------")

numero = float(input("Ingresa un número: "))
if '.' in numero: # Si hay un punto (decimal)
    decimales = numero.split('.')[1] # Para contar cuantos numeros hay despues de la posicion 1 (el punto decimal)
    if len(decimales) == 1: # Si hay un solo numero decimal 
        print("El numero tiene 1 decimal")
    elif len(decimales) == 2: # Si hay dos numeros decimales
        print("El numero tiene 2 decimales")
    else: # Si hay mas de dos numeros decimales
        print("El numero tiene más de 2 decimales")
else: # Si no tiene decimales
    print("No tiene decimales")

# 5 - Solicita un país y muestra si está en la siguiente tupla: ("Colombia", "Perú", "Argentina", "México").

print("------Ejercicio 5 ------")

tupla = ("Colombia","Peru","Argentina","Mexico") # Tupla de los pais
pais = input("Ingresa el pais en el que vives,empiezalo por mayuscula por favor: ") # Pedir un pais
if pais in tupla: # Si el pais del usuario esta en la tupla
    print(f"{pais} si esta en la tupla {tupla}")
else:  # Si el pais del usuario no esta en la tupla
    print(f"{pais} no esta en la tupla {tupla}")

# 6 - Pide tu tipo de sangre (A, B, AB, O) y muestra tu compatibilidad según un diccionario predefinido.

print("------Ejercicio 6 ------")

compatibilidad = {
    "O": "Puede donar a todos (O, A, B, AB). Solo recibe de O.", # Caracteristicas de tipo O
    "A": "Puede donar a A y AB. Recibe de A y O.", # Caracteristicas de tipo A
    "B": "Puede donar a B y AB. Recibe de B y O.", # Caracteristicas de tipo B
    "AB": "Puede recibir de todos (donante universal). Solo dona a AB." # Caracteristicas de tipo AB
}

tipo = input("Ingresa tu tipo de sangre (A, B, AB, O) escribelo tal cual por favor: ") # Para pedir tipo de sangre

if tipo in compatibilidad: # Para saber si el tipo que ingreso esta
    print("Compatibilidad:", compatibilidad[tipo]) # Para que busque exactamente igual el valor del usuario en el diccionario e imprimirlo
else: # Si el ingresado no es valido
    print("Tipo de sangre no válido.")


# 7 - Ingresa una temperatura en °C. Si es menor de 10, hace frío. Si está entre 10 y 25, templado. Más de 25, hace calor.

print("------Ejercicio 7 ------")

temp = float(input("Ingresa la temperatura actual de Palmira en grados centigrados: ")) # Para pedir la temperatura de palmira en c°

if temp < 10: # Si es menor a 10
    print(f"Hace mucho frio en Palmira con esos {temp} °C como aguantas ese clima!")
elif temp >= 10 and temp <= 25: # Si esta entre 10 a 25
    print(f"La temperatura en Palmira es de {temp} °C lo que esta templado,que bonito dia y clima juntos!")
else: # Si es mayor a 25
    print(f"Con esos {temp} °C hace mucho calor en Palmira,como aguantas eso!")

# 8 - Crea un menú con opciones 1. Sumar, 2. Restar, 3. Multiplicar. Pide dos números y ejecuta la operación seleccionada.

print("------Ejercicio 8 ------")

print("1. Sumar") # Primera opcion
print("2. Restar") # Segunda opcion
print("3. Multiplicar") # Tercera opcion

opcion = input("Selecciona una opción (1-3): ") # Para que diga cual desea usar

num1 = float(input("Ingresa el primer número: ")) # Para pedir el primer numero
num2 = float(input("Ingresa el segundo número: ")) # Para pedir el segundo numero

if opcion == "1": # Si la opcion es suma,poder sumar los dos numeros
    resultado = num1 + num2
    print("La suma es:", resultado)
elif opcion == "2": # Si la opcion es resta,poder restar los dos numeros
    resultado = num1 - num2
    print("La resta es:", resultado)
elif opcion == "3": # Si la opcion es multiplicacion,poder multiplicar los numeros
    resultado = num1 * num2
    print("La multiplicación es:", resultado)
else: # Si la opcion no es la que dimos
    print("Opción no válida,no esta en la lista de operaciones que te dimos.")

# 9 - Pide un número entre 1 y 12 y muestra el mes correspondiente usando un diccionario.

print("------Ejercicio 9 ------")


numero = int(input("Ingresa un numero del 1 al 12: "))

meses = {
    "1": "Enero", # 1er Mes
    "2": "Febrero", # 2do Mes
    "3": "Marzo", # 3er Mes
    "4": "Abril", # 4to Mes
    "5": "Mayo", # 5to Mes
    "6": "Junio", # 6to Mes
    "7": "Julio", # 7mo Mes
    "8": "Agosto", # 8vo Mes
    "9": "Septiembre", # 9no Mes
    "10": "Octubre", # 10mo Mes
    "11": "Noviembre", # 11avo Mes
    "12": "Diciembre" # 12avo Mes
}

if numero == 1: # Si el numero ingresado es el 1er mes
    print(f"El numero {numero} corresponde al mes {meses['1']}")
elif numero ==2: # Si el numero ingresado es el 2do mes
    print(f"El numero {numero} corresponde al mes {meses['2']}")
elif numero ==3: # Si el numero ingresado es el 3ro mes
    print(f"El numero {numero} corresponde al mes {meses['3']}")
elif numero ==4: # Si el numero ingresado es el 4to mes
    print(f"El numero {numero} corresponde al mes {meses['4']}")
elif numero ==5: # Si el numero ingresado es el 5to mes
    print(f"El numero {numero} corresponde al mes {meses['5']}")
elif numero ==6: # Si el numero ingresado es el 6to mes
    print(f"El numero {numero} corresponde al mes {meses['6']}")
elif numero ==7: # Si el numero ingresado es el 7mo mes
    print(f"El numero {numero} corresponde al mes {meses['7']}")
elif numero ==8: # Si el numero ingresado es el 8vo mes
    print(f"El numero {numero} corresponde al mes {meses['8']}")
elif numero ==9: # Si el numero ingresado es el 9no mes
    print(f"El numero {numero} corresponde al mes {meses['9']}")
elif numero ==10: # Si el numero ingresado es el 10mo mes
    print(f"El numero {numero} corresponde al mes {meses['10']}")
elif numero ==11: # Si el numero ingresado es el 11avo mes
    print(f"El numero {numero} corresponde al mes {meses['11']}")
elif numero ==12: # Si el numero ingresado es el 12avo mes
    print(f"El numero {numero} corresponde al mes {meses['12']}")
else:  # Si el numero ingresado no corresponde a ningun mes (+12)
    print(f"El numero {numero} no corresponde a ningun mes,solo tenemos 12 meses")

# 10 - Solicita un número de 4 dígitos y determina si comienza con 1, 2 o cualquier otro

print("------Ejercicio 10 ------")


numeroo = input("Ingresa un numero de 4 digitos por favor: ")
if numeroo[0] ==  "1": # Si empieza por uno
    print(f"El numero de 4 digitos: {numeroo} comienza por el numero uno")
elif numeroo[0] == "2": # Si empieza por dos
    print(f"El numero de 4 digitos: {numeroo} comienza por el numero dos")
else: # Si empieza por cualquier otro numero que no es 1 ni 2
    print(f"El numero de 4 digitos: {numeroo} no comienza ni por el numero 2 ni por el numero 1, empieza por  cualquier otro")

# 11 - Ingresa una palabra. Muestra si su primera letra es vocal, consonante o un numero.

print("------Ejercicio 11 ------")


palabra = input("Ingresa una palabra cualquiera por favor: ") # Para pedir una palabra
if palabra [0] == "A":  # Si empieza por la vocal A
    print(f"La palabra {palabra} empieza por la vocal A")
elif palabra [0] == "E":  # Si empieza por la vocal E
    print(f"La palabra {palabra} empieza por la vocal E")
elif palabra [0] == "I":  # Si empieza por la vocal I
    print(f"La palabra {palabra} empieza por la vocal I")
elif palabra [0] == "O":  # Si empieza por la vocal O
    print(f"La palabra {palabra} empieza por la vocal O")
elif palabra [0] == "U":  # Si empieza por la vocal U
    print(f"La palabra {palabra} empieza por la vocal U")
elif palabra [0] == "B": # Si empieza por la consonante B
    print(f"La palabra {palabra} empieza por la consonante 'B'")
elif palabra [0] == "C": # Si empieza por la consonante C
    print(f"La palabra {palabra} empieza por la consonante 'C'")
elif palabra [0] == "D": # Si empieza por la consonante D
    print(f"La palabra {palabra} empieza por la consonante 'D'")
elif palabra [0] == "F": # Si empieza por la consonante F
    print(f"La palabra {palabra} empieza por la consonante 'F'")
elif palabra [0] == "G": # Si empieza por la consonante G
    print(f"La palabra {palabra} empieza por la consonante 'G'")
elif palabra [0] == "H": # Si empieza por la consonante H
    print(f"La palabra {palabra} empieza por la consonante 'H'")
elif palabra [0] == "J": # Si empieza por la consonante J
    print(f"La palabra {palabra} empieza por la consonante 'J'")
elif palabra [0] == "K": # Si empieza por la consonante K
    print(f"La palabra {palabra} empieza por la consonante 'K'")
elif palabra [0] == "L": # Si empieza por la consonante L
    print(f"La palabra {palabra} empieza por la consonante 'L'")
elif palabra [0] == "M": # Si empieza por la consonante M
    print(f"La palabra {palabra} empieza por la consonante 'M'")
elif palabra [0] == "N": # Si empieza por la consonante N
    print(f"La palabra {palabra} empieza por la consonante 'N'")
elif palabra[0] == "Ñ": # Si empieza por la consonante Ñ
    print(f"La palabra {palabra} empieza por la consonante 'Ñ'")
elif  palabra[0] == "P": # Si empieza por la consonante P
    print(f"La palabra {palabra} empieza por la consonante 'P'")
elif palabra[0] == "Q": # Si empieza por la consonante Q
    print(f"La palabra {palabra} empieza por la consonante 'Q'")
elif palabra[0] == "R": # Si empieza por la consonante R
    print(f"La palabra {palabra} empieza por la consonante 'R'")
elif palabra[0] == "S": # Si empieza por la consonante S
    print(f"La palabra {palabra} empieza por la consonante 'S'")
elif palabra[0] == "T": # Si empieza por la consonante T
    print(f"La palabra {palabra} empieza por la consonante 'T'")
elif palabra[0] == "V": # Si empieza por la consonante V
    print(f"La palabra {palabra} empieza por la consonante 'V'")
elif palabra[0] == "W": # Si empieza por la consonante W
    print(f"La palabra {palabra} empieza por la consonante 'W'")
elif palabra[0] == "X": # Si empieza por la consonante X
    print(f"La palabra {palabra} empieza por la consonante 'X'")
elif palabra[0] == "Y": # Si empieza por la consonante Y
    print(f"La palabra {palabra} empieza por la consonante 'Y'")
elif palabra[0] == "Z": # Si empieza por la consonante Z
    print(f"La palabra {palabra} empieza por la consonante 'Z'")
else: # Si no empieza por vocal o consonante,osea numero
    print(f"La palabra {palabra} empieza por un numero")

# 12 - Pide una fruta. Si está en la lista ["manzana", "pera", "piña"], muestra su precio. Si no, indica que no está disponible.

print("------Ejercicio 12 ------")


fruta = [
"Manzana","1300 Pesos", # Precio de la manzana
"Pera","1500 Pesos", # Precio de la pera
"Piña","1800 Pesos" # Precio de la piña
]

frutass = input("Ingresa una fruta para comprar,escribalo empezando por mayuscula por favor: ") # Pedir una fruta
if frutass in fruta: # Si la fruta que pidio esta en la lista
    posicion = fruta.index(frutass) # Para hallar la posicion de la fruta una vez buscada si esta en la lista fruta
    print(f"El precio de la {frutass} es {fruta[posicion +1]}") # Para sumarle 1 al indice de la fruta (osea el precio)
else: # Si la fruta no esta en la lista
    print(f"La fruta {frutass} no esta disponible en la lista {fruta}")


# 13 -  Pide tu calificación (0 a 5). Si es menor que 3, reprobado. Entre 3 y 4, aprobado. Mayor a 4, excelente.

print("------Ejercicio 13 ------")


calificacion =  float(input("Ingresa tu nota en Programacion: ")) # Para pedir la nota
if calificacion < 3:  # Si es menor a 3
    print("Tu calificacion es reprobado,te esperamos el otro año :)")
elif calificacion >= 3 and calificacion <= 4:  # Si esta entre 3 a 4
    print("Tu calificacion es aprobatoria pero regular,ve avanzando")
else:  # Si es superior a 4
    print("Tu nota es excelente,vas bien!")

# 14 - Pide un número y muestra si es divisible entre 4, entre 6, o no lo es.

print("------Ejercicio 14 ------")


num1 = int(input("Ingresa un numero por el cual creas que sea divisible por 4 o 6: ")) # Pedir un numero por el cual se crea que es divisible por 4 y 6
if num1 % 4 == 0 and num1 % 6 == 0: # Si es divisible por 4 y 6 del numero dado
    print(f"El numero {num1} si es divisble por 4 y 6")
elif num1 % 4 == 0:  # Si solo es divisible por 4
    print(f"El numero {num1} solo es divisible por el 4")
elif num1 % 6 == 0: # Si solo es divisible por 6
    print(f"El numero {num1} solo es divisible por 6")
else: # Si no es divisible ni por el 4 ni 6
    print(f"El numero {num1} no es divisible ni por 4 ni por 6")

# 15 - Crea un sistema de autenticación básico. Pide usuario y clave. Usa un diccionario para validar.

print("------Ejercicio 15 ------")

usuarios = {
    "juan": "1234", # Datos de juan
    "maria": "abcd", # Datos de maria
    "admin": "admin123" # Datos de admin
}


usuario = input("Ingrese su nombre de usuario: ") # Pedir el usuario
clave = input("Ingrese su clave: ") # Pedir la clave

if usuario in usuarios: # Si el usuario esta en el diccionario
    if usuarios[usuario] == clave: # Si el valor de la llave es igual a la clave accede
        print(f"Acceso concedido. Bienvenido {usuario} a nuestro sistema.")
    else: # Si el valor de la  llave es igual pero la clave no no accede
        print("Clave incorrecta.")
else: # Si no esta ni siquiera registrado
    print("Usuario no registrado en el sistema.")

# 16 - Solicita una edad y muestra a qué grupo pertenece: niño (0-12), adolescente (13-17), adulto (18-64), mayor (65+).

print("------Ejercicio 16 ------")

edad333 = int(input("Ingresa tu edad: ")) # Para pedir la edad
if edad333 > 0 and edad333 <= 12: # Si esta entre 0 a 12 años
    print(f"Eres un niño aun por tener {edad333} años")
elif edad333  >= 13 and edad333 <= 17: # Si esta entre 13 a 17 años
    print(f"Eres un adolescente por tener {edad333} años,que dura etapa!")
elif edad333 >= 18 and edad333 < 64: # Si esta entre 18 a 64 años
    print("Eres un adulto ya,felicidades") 
else: # Si no es ninguna de las anteriores edades
    print("Eres un adulto mayor lo sentimos")


# 17 - Pide el nombre de una ciudad. Si está en una tupla, muestra que es capital; si no, muestra “ciudad secundaria”.

print("------Ejercicio 17 ------")

tuplaaaa = ("Bogota", "Palmira", "Cali", "Washington D.C.", "Caracas") # Tupla
ciudaddd = input("Ingresa una ciudad, empezando por mayúscula por favor: ") # Pedir ciudad

if ciudaddd in tuplaaaa: # Para saber si la ciudad ingresada esta en la tupla
    if ciudaddd == "Bogota": # Para mostrar si es una capital
        print(f"La ciudad {ciudaddd} es capital de Colombia y está en la tupla: {tuplaaaa}")
    elif ciudaddd == "Washington D.C.": # Para mostrar si es una capital
        print(f"La ciudad {ciudaddd} es capital de Estados Unidos y está en la tupla: {tuplaaaa}")
    elif ciudaddd == "Caracas":# Para mostrar si es una capital
        print(f"La ciudad {ciudaddd} es capital de Venezuela y está en la tupla: {tuplaaaa}")
    else: # Para mostrar que no es una capital
        print(f"La ciudad {ciudaddd} está en la tupla, pero no es capital de país.")
else: # Para mostrar que no esta en la tupla
    print(f"La ciudad {ciudaddd} no está en la tupla")

# 18 -  Ingresa el valor de una compra. Si es mayor de $200.000 aplica un 15% de descuento. Entre $100.000 y $200.000 aplica 10%. Si es menor, no hay descuento.

print("------Ejercicio 18 ------")


compra = float(input("Ingresa el valor de una Television: ")) # El precio
if compra > 200000: # Si es mayor a 200000 aplicar un 15% de descuento
    descu = compra * 0.15
    descuento_final = compra - descu
    print(f"El precio final a pagar con un 15% de descuento del Televisor por un precio mayor a 200000$ es {descuento_final}$")
elif compra >= 100000 and compra <= 200000: # Si esta entre 100000 a 200000 aplicar un 10%
    descu2 = compra * 0.10
    descuento_final2 = compra - descu2
    print(f"El precio final a pagar con un 10% de descuento del televisor por un precio entre 100000 y 200000$ es: {descuento_final2}$")
else: # Si no aplica ningun descuento
    print("No aplica descuento para este precio")

# 19 - Pide el nombre y el número de horas trabajadas. Calcula el salario con tarifa de $10.000/hora. Si trabajó más de 40 horas, aplica un bono del 20%.

print("------Ejercicio 19 ------")

nombreeee = input("Ingresa tu nombre: ") # Pedir nombre
horas = int(input("Ingresa el numero de horas trabajadas: ")) # Pedir horas trabajadas
tarifa = 10000 # Precio que se paga
salario_base = horas * tarifa # Precio pagado por hora

if horas > 40: # Si trabajo mas de 40 horas aplicar un 20% de bono
    bono = salario_base * 0.20
    salario_total = salario_base + bono
    print(f"{nombreeee}, trabajaste más de 40 horas. Tu salario total con bono del 20% es: {salario_total}$")
else: # Si trabajo normal o menos de 40 horas no se aplica bono
    print(f"{nombreeee}, tu salario será de {salario_base}$ ya que no trabajaste más de 40 horas. Gracias por tu servicio.")


# 20 - Ingresa tu puntaje en una prueba (0 a 100). Si es menor a 50, insuficiente. De 50 a 79, aceptable. 80 a 100, sobresaliente.

print("------Ejercicio 20 ------") 

puntaje = int(input("Ingresa tu puntaje en las olimpiadas de 0 a 100: ")) # Pedir puntaje

if puntaje < 50: # Si es menor a  50
    print(f"Tu puntaje de {puntaje} puntos es un puntaje insuficiente, ¡sigue intentando!")
elif 50 <= puntaje <= 79: # Si esta entre 50 a 79
    print(f"Tu puntaje de {puntaje} puntos es un puntaje aceptable, ¡muy bien!")
elif 80 <= puntaje <= 100: # Si esta entre 80 a 100
    print(f"Tu puntaje de {puntaje} puntos es sobresaliente, ¡felicitaciones!")
else: # Si es mayor a 100
    print("Puntaje fuera del rango válido (0-100).")



