# Ejercicios de .append, .insert, .pop, etc. Ejercicios y Practicas

print("-------- Ejercicios de metodos de listas ----------")



# 1) Ejercicios de .append:

print("------------- Ejercicios de .append() -------------")

# Ejercicio 1: Crea una lista vacia y agrega el numero 7

print("------------------ Ejercicio 1 --------------------")


numeros = []
num = int(input("Ingresa el numero siete porfavor: ")) # Para pedirle el numero int 7 al usuario
numeros.append(num) # .append Agrega el numero al final de la lista
print(f"La lista resultante con el numero 7 es: {numeros}")

# Ejercicio 2: Agrega el nombre 'Carlos' al final de la lista nombres = ['Ana','Luis']

print("------------------- Ejercicio 2 --------------------")


nombres = ["Ana","Luis"]
nombre = input("¿Cual es tu primer nombre?: ") # Para pedir el nombre al usuario
nombres.append(nombre) # .append Agrega el nombre al final de la lista
print(f"La lista resultante con el nombre del usuario es: {nombres}")






# 2) Ejercicios de insert:

print("------------- Ejercicios de .insert() -------------")


# Ejercicio 1: Inserta el numero 99 en la posicion 0 de la lista [1,2,3]

print("------------------ Ejercicio 1 --------------------")


lista = [1,2,3]
insertar = int(input("Ingresa el numero 99 porfavor: ")) # Para pedir el numero int 99 al usuario
lista.insert(0,insertar) # .insert Inserta el numero en la lista en la posicion 0
print(f"La lista resultante con el numero 99 insertado en la posicion 0 es: {lista}")


# Ejercicio 2: En la lista colores = ["azul","verde"], inserta "rojo" en la posicion 1

print("------------------ Ejercicio 2 --------------------")


colores = ["Azul","Verde"]
color = input("Escribe el color rojo porfavor: ") # Para pedir el color al usuario
colores.insert(1,color) # .insert Inserta el color en la lista en la posicion 1
print(f"La lista de colores resultante al insertar el color 'rojo' en la posicion 1 es: {colores}")




# # 3) Ejercicios de extend:

print("------------- Ejercicios de .extend() -------------")


# Ejercicio 1: Agrega los elementos de la lista [4,5,6] a la lista [1,2,3] usando extend()

print("------------------ Ejercicio 1 --------------------")


lista1 = [1,2,3] 
lista2 = [4,5,6]
lista1.extend(lista2) # .extend Agrega otros iterables a la lista,como tuplas,diccionarios etc
print(f"La lista resultante extendida es: {lista1}")


# Ejercicio 2: Agrega los caracteres de la cadena 'ok'  a la lista de letras = ['a','b']

print("------------------ Ejercicio 2 --------------------")


letras = ["a","b"]
letras.extend("ok") # .extend Agrega otros iterables a la lista,como tuplas,diccionarios etc.
print(f"La lista de letras resultante extendida es: {letras}")






# 4) Ejercicios de remove(x)

print("------------- Ejercicios de .remove() -------------")

# Ejercicio 1: Elimina el valor 'uva' de la lista frutas = ['manzana','uva','pera']

print("------------------ Ejercicio 1 --------------------")


frutas = ["Manzana","Uva","Pera"]
eliminar = input("Escribe la fruta  'Uva' por favor: ")
frutas.remove(eliminar) #.remove elimina la primera aparacion de un valor de la lista
print(f"La lista de frutas removida la fruta 'Uva' es: {frutas}")

# Ejercicio 2: En la lista [1,2,3,2] elimina el primer 2 que aparezca

print("------------------ Ejercicio 2 --------------------")


numeross = [1,2,3,2]
numeross.remove(2) #.remove elimina la primera aparacion de un valor de la lista
print(f"La lista de numeros sin el primer 2 es: {numeross}")






# 5) Ejercicios de pop([i])

print("------------- Ejercicios de .pop([i]) -------------")

# Ejercicio 1: Usa pop() para eliminar el ultimo momento de la lista [1,2,3,4]

print("------------------ Ejercicio 1 --------------------")


listass = [1,2,3,4]
valor = listass.pop()   # .pop() Agarra y guarda el ultimo valor de la lista y lo elimina de la lista  (el numero cuatro)
print(valor)   # Imprime el ultimo valor de la lista previamente agarrado por el .pop (el numero cuatro)
print(f"La lista resultante sin el ultimo elemento de la lista es: {listass}")   # Imprime la lista sin el ultimo valor (el numero cuatro)

# Ejercicio 2: Elimina el elemento de la posicion 0 de la lista [uno,dos,tres]

print("------------------ Ejercicio 2 --------------------")


listassss = ["uno","dos","tres"]
valorr = listassss.pop(0) # .pop() agarra y guarda el valor que estaba en la posicion 0 de la lista y lo elimina de la lista ('uno')
print(valorr)    # Imprime el valor agarrado que estaba en la posicion 0 de la lista ('uno')
print(f"La lista resultante sin el elemento de la posicion 0 de la lista es: {listassss}") # Imprime la lista sin el valor de la posicion 0 ('uno')





# 6) Ejercicios de clear()

print("------------- Ejercicios de .clear() --------------")

# Ejercicio 1: Vacia completamente la lista [1,2,3] con clear()

print("------------------ Ejercicio 1 --------------------")


lista11 = []
num1 = int(input("Ingresa el numero 1 porfavor: ")) # Para pedirle el numero int 1 al usuario
num2 = int(input("Ingresa el numero 2 porfavor: ")) # Para pedirle el numero int 2 al usuario
num3 = int(input("Ingresa el numero 3 porfavor: ")) # Para pedirle el numero int 3 al usuario
lista11.append(num1) #.append() añade el numero 1 al final de la lista
lista11.append(num2) #.append() añade el numero 2 al final de la lista
lista11.append(num3) #.append() añade el numero 3 al final de la lista
print(lista11)
lista11.clear() #.clear() vacia la lista completa
print(f"La lista vacia seria asi: {lista11}")

# Ejercicio 2: Crear una lista con 5 elementos y eliminalos todos usando clear()

print("------------------ Ejercicio 2 --------------------")


listas11 = []
comida = input("Ingresa una comida favor: ") # Para pedirle al usuario una comida
comida2 = input("Ingresa otra comida por favor: ") # Para pedirle al usuario otra comida
SENA = input("Ingresa 'SENA' por favor: ") # Para pedirle al usuario el string
profesor = input("Ingresa el nombre del profesor de programacion: ") # Para pedirle al usuario el nombre del profesor
listas11.append(comida) #.append() agrega la primera comida al final de la lista
listas11.append(comida2) #.append() agrega la segunda comida al final de la lista
listas11.append(SENA) #.append() agrega el string al final de la lista
listas11.append(profesor) #.append() agrega el nombre del profesor al final de la lista
listas11.clear() #.clear() vacia la lista completa
print(f"La lista vacia seria asi: {listas11}")





# 7) Ejercicios de index(x)

print("------------- Ejercicios de .index() --------------")

# Ejercicio 1: Encuentra la posicion del valor 'pera' en la lista ['manzana','pera','uva']

print("------------------ Ejercicio 1 --------------------")


lista101 = ["Manzana","Pera","Uva"]
indexacion = lista101.index("Pera") #.index devuelve el indice/posicion de la primera aparicion de la palabra 'Pera' en la lista
print(f"La posicion de la palabra 'pera' en la lista es: {indexacion}")

# Ejercicio 2: Dado numeros = [4,5,6,7],encuentra el indice del numero 6

print("------------------ Ejercicio 2 --------------------")


listanum = [4,5,6,7]
indexacion = listanum.index(6) #.index devuelve el indice/posicion de la primera aparicion del numero 6 en la lista
print(f"La posicion del numero 6 en la lista es: {indexacion}")






# 8) Ejercicios de count(x)

print("------------ Ejercicios de .count(x) --------------")

# Ejercicio 1: Cuenta cuantas veces aparece el numero 3 en [3,1,3,5,3]

print("------------------ Ejercicio 1 --------------------")


listar = [3,1,3,5,3]
contadas = listar.count(3) #.count() devuelve el numero de veces que sale un valor en la lista,en este caso el numero de veces que sale 3
print(f"El numero de veces que sale el numero 3 en la lista es de: {contadas}")

# Ejercicio 2: En la lista ['a','b','c','a'], cuenta cuantas veces aparece 'a'

print("------------------ Ejercicio 2 --------------------")


listaletras = ["a","b","c","a"]
contadas2 = listaletras.count("a") #.count() devuelve el numero de veces que sale la letra 'a' en la lsita
print(f"El numero de veces que sale la letra 'a' en la lista es de: {contadas2}")






# 9) Ejercicios de sort()

print("------------ Ejercicios de .sort() ---------------")

# Ejercicio 1: Ordena la lista [5,1,4,2,3] de forma ascendente

print("------------------ Ejercicio 1 --------------------")


listadesordenada = [5,1,4,2,3]
listadesordenada.sort() #.sort() ordena de forma ascendente la lista
print(f"La lista previamente ordenada es asi: {listadesordenada}")

# Ejercicio 2: Dada la lista ["z","a","m","b"], ordenala alfabeticamente

print("------------------ Ejercicio 2 --------------------")


alfabetico = ["z","a","m","b"]
alfabetico.sort() #.sort() ordena de forma ascendente la lista,en este caso alfabeticamente
print(f"La lista previamente ordenada es asi: {alfabetico}")






# 10) Ejercicios de reverse()

print("----------- Ejercicios de .reverse() --------------")

# Ejercicio 1: Invierte el orden de lista [1,2,3,4]

print("------------------ Ejercicio 1 --------------------")


lis = [1,2,3,4]
lis.reverse() #.reverse() invierte el orden de la lista
print(f"La lista previamente invertida se ve asi: {lis}")

# Ejercicio 2:  Invierte la lista ['Inicio','medio','fin']

print("------------------ Ejercicio 2 --------------------")


listss = ["Inicio","Medio","Fin"]
reversaa = listss.reverse() #.reverse() invierte el orden de la lista
print(f"La lista previamente invertida se ve asi: {listss}")






# 11) Ejercicios de copy()

print("------------- Ejercicios de .copy() ---------------")

# Ejercicio 1: Copia la lista [1,2,3] en una nueva lista 'nueva lista'

print("------------------ Ejercicio 1 --------------------")


listauno = [1,2,3]
nuevalista = listauno.copy() #.copy() copia exactamente una copia a otra sin afectar la original
print(f"La lista copiada es exactamente asi: {nuevalista}")

# Ejercicio 2: Haz una copia de la lista ['a','b','c'],y luego agrega "d" a la nueva sin afectar la original

print("------------------ Ejercicio 2 --------------------")


listanumerouno = ["a","b","c"]
listanumerodos = listanumerouno.copy() #.copy() copia la lista ['a','b','c'] a otra sin afectarla
listanumerodos.append("d") #.append() agrega la letra 'd' a la lista copiada
print(f"La lista copiada y agregada la letra 'd' seria asi: {listanumerodos} y la lista original ilesa y sin afectar asi: {listanumerouno}")