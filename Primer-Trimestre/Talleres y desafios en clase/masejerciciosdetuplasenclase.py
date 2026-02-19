# Mas ejercicios de tuplas en clase

print("---------- Ejercicios de tuplas en clase ----------")

# Ejercicio 1: Crear una tupla con los numeros del 1 al 5

print("------------------ Ejercicio 1 --------------------")

tupla_num = ()
print(tupla_num)
nuevalista_de_num = list(tupla_num) # Pasar a lista la tupla para poder modificarla luego
numeros1 = int(input("Ingresa el numero 1: ")) # Para pedir al usuario ingresar el numero int 1
numeros2 = int(input("Ingresa el numero 2: ")) # Para pedir al usuario ingresar el numero int 2
numeros3 = int(input("Ingresa el numero 3: ")) # Para pedir al usuario ingresar el numero int 3
numeros4 = int(input("Ingresa el numero 4: ")) # Para pedir al usuario ingresar el numero int 4
numeros5 = int(input("Ingresa el numero 5: ")) # Para pedir al usuario ingresar el numero int 5
nuevalista_de_num.append(numeros1) # Para agregar el numero int 1 dado por el usuario
nuevalista_de_num.append(numeros2) # Para agregar el numero int 2 dado por el usuario
nuevalista_de_num.append(numeros3) # Para agregar el numero int 3 dado por el usuario
nuevalista_de_num.append(numeros4) # Para agregar el numero int 4 dado por el usuario
nuevalista_de_num.append(numeros5) # Para agregar el numero int 5 dado por el usuario
tupla_final = tuple(nuevalista_de_num) # Pasar a tupla nuevamente la anterior lista que hicimos para modificar la primera tupla
print(f"La tupla resultante es: {tupla_final}")




# Ejercicio 2: Acceder a un elemento y muestra el segundo valor de la tupla creada anteriormente

print("------------------ Ejercicio 2 --------------------")

tupla_num11 = ()
print(tupla_num11)
nuevalista_de_nume = list(tupla_num11) # Pasar a lista la tupla para modificarla
numeros11 = int(input("Ingresa el numero 1: ")) # Para pedir al usuario ingresar el numero int 1
numeros22 = int(input("Ingresa el numero 2: ")) # Para pedir al usuario ingresar el numero int 2
numeros33 = int(input("Ingresa el numero 3: ")) # Para pedir al usuario ingresar el numero int 3
numeros44 = int(input("Ingresa el numero 4: ")) # Para pedir al usuario ingresar el numero int 4
numeros55 = int(input("Ingresa el numero 5: ")) # Para pedir al usuario ingresar el numero int 5
nuevalista_de_nume.append(numeros11) # Para agregar el numero int 1 dado por el usuario al final de la lista
nuevalista_de_nume.append(numeros22) # Para agregar el numero int 2 dado por el usuario al final de la lista
nuevalista_de_nume.append(numeros33) # Para agregar el numero int 3 dado por el usuario al final de la lista
nuevalista_de_nume.append(numeros44) # Para agregar el numero int 4 dado por el usuario al final de la lista
nuevalista_de_nume.append(numeros55) # Para agregar el numero int 5 dado por el usuario al final de la lista
tupla_final2 = tuple(nuevalista_de_nume) # Pasar a tupla otra vez la anterior lista que hicimos para modificar la primera tupla
print(f"La tupla final es {tupla_final2}")
acceso = tupla_final2[1] # Para acceder al valor de la tupla del indice/posicion 1 (numero 2)
print(f"El segundo valor de la tupla {tupla_final2} es: {acceso}")



# Ejercicio 3: Obtener la longitud imprime cuantos elementos tiene la tupla

print("------------------ Ejercicio 3 --------------------")

tupla_num3 = ()
print(tupla_num3)
nuevalista_de_nume2 = list(tupla_num3) # Pasar a lista la tupla para modificarla
numeros111 = int(input("Ingresa el numero 1: ")) # Para pedir al usuario ingresar el numero int 1
numeros222 = int(input("Ingresa el numero 2: ")) # Para pedir al usuario ingresar el numero int 2
numeros333 = int(input("Ingresa el numero 3: ")) # Para pedir al usuario ingresar el numero int 3
numeros444 = int(input("Ingresa el numero 4: ")) # Para pedir al usuario ingresar el numero int 4
numeros555 = int(input("Ingresa el numero 5: ")) # Para pedir al usuario ingresar el numero int 5
nuevalista_de_nume2.append(numeros111) # Para agregar el numero int 1 dado por el usuario al final de la lista
nuevalista_de_nume2.append(numeros222) # Para agregar el numero int 2 dado por el usuario al final de la lista
nuevalista_de_nume2.append(numeros333) # Para agregar el numero int 3 dado por el usuario al final de la lista
nuevalista_de_nume2.append(numeros444) # Para agregar el numero int 4 dado por el usuario al final de la lista
nuevalista_de_nume2.append(numeros555) # Para agregar el numero int 5 dado por el usuario al final de la lista
tupla_final3 = tuple(nuevalista_de_nume2) # Pasar a tupla otra vez la anterior lista que hicimos para modificar la primera tupla
contar = len(tupla_final3) # Para contar cuantos elementos tiene la tupla
print(f"El numero de elementos que tiene la tupla es: {contar}")




# Ejercicio 4: Usar index() y encuentra la posicion del numero 4 en la tupla

print("------------------ Ejercicio 4 --------------------")

tupla_num4 = ()
print(tupla_num4)
nuevalista_de_nume3 = list(tupla_num4)
numeros1111 = int(input("Ingresa el numero 1: ")) # Para pedir al usuario ingresar el numero int 1
numeros2222 = int(input("Ingresa el numero 2: ")) # Para pedir al usuario ingresar el numero int 2
numeros3333 = int(input("Ingresa el numero 3: ")) # Para pedir al usuario ingresar el numero int 3
numeros4444 = int(input("Ingresa el numero 4: ")) # Para pedir al usuario ingresar el numero int 4
numeros5555 = int(input("Ingresa el numero 5: ")) # Para pedir al usuario ingresar el numero int 5
nuevalista_de_nume3.append(numeros1111) # Para agregar el numero int 1 dado por el usuario al final de la lista
nuevalista_de_nume3.append(numeros2222) # Para agregar el numero int 2 dado por el usuario al final de la lista
nuevalista_de_nume3.append(numeros3333) # Para agregar el numero int 3 dado por el usuario al final de la lista
nuevalista_de_nume3.append(numeros4444) # Para agregar el numero int 4 dado por el usuario al final de la lista
nuevalista_de_nume3.append(numeros5555) # Para agregar el numero int 5 dado por el usuario al final de la lista
tupla_final4 = tuple(nuevalista_de_nume3) # Pasar a tupla otra vez la anterior lista que hicimos para modificar la primera tupla
indice = tupla_final4.index(4) # Para hallar el indice/posicion del valor numero int 4 que esta en la tupla
print(f"La posicion o indice del numero 4 en la tupla es: {indice}")




# Ejercicio 5: Usar count() y cuenta cuantas veces aparece el numero 2 en la tupla

print("------------------ Ejercicio 5 --------------------")

tupla_num5 = ()
print(tupla_num5)
nuevalista_de_nume4 = list(tupla_num5) # Pasar a lista la tupla para modificarla
numeros11111 = int(input("Ingresa el numero 1: ")) # Para pedir al usuario ingresar el numero int 1
numeros22222 = int(input("Ingresa el numero 2: ")) # Para pedir al usuario ingresar el numero int 2
numeros33333 = int(input("Ingresa el numero 3: ")) # Para pedir al usuario ingresar el numero int 3
numeros44444 = int(input("Ingresa el numero 4: ")) # Para pedir al usuario ingresar el numero int 4
numeros55555 = int(input("Ingresa el numero 5: ")) # Para pedir al usuario ingresar el numero int 5
nuevalista_de_nume4.append(numeros11111) # Para agregar el numero int 1 dado por el usuario al final de la lista
nuevalista_de_nume4.append(numeros22222) # Para agregar el numero int 2 dado por el usuario al final de la lista
nuevalista_de_nume4.append(numeros33333) # Para agregar el numero int 3 dado por el usuario al final de la lista
nuevalista_de_nume4.append(numeros44444) # Para agregar el numero int 4 dado por el usuario al final de la lista
nuevalista_de_nume4.append(numeros55555) # Para agregar el numero int 5 dado por el usuario al final de la lista
tupla_final4 = tuple(nuevalista_de_nume4) # Pasar a tupla nuevamente la anterior lista que hicimos para modificar la primera tupla
indice = tupla_final4.count(2) # Para contar cuantas veces sale el valor int 2 en la tupla
print(f"El numero de veces que sale el 2 es: {indice}")




# Ejercicio 6: Tupla con tipos mezclados; Crea una tupla que contenga una cadena,un numero entero y un numero decimal

print("------------------ Ejercicio 6 --------------------")

tuplaaa = ()
print(tuplaaa)
nuevaa_listaa = list(tuplaaa) # Pasar a lista la tupla para modificarla
num1 = int(input("Ingresa un numero entero: ")) # Para pedir al usuario ingresar el numero int 1
num2 = input("Ingresa cualquier mensaje escrito: ") # Para pedir al usuario ingresar el numero int 2
num3 = float(input("Ingresa un numero decimal: ")) # Para pedir al usuario ingresar el numero int 3
nuevaa_listaa.append(num1) # Para agregar el numero int 1 dado por el usuario al final de la lista
nuevaa_listaa.append(num2) # Para agregar el numero int 2 dado por el usuario al final de la lista
nuevaa_listaa.append(num3) # Para agregar el numero int 3 dado por el usuario al final de la lista
tuplaaa_finaaal = tuple(nuevaa_listaa) # Pasar a tupla otra vez la anterior lista que hicimos para modificar la primera tupla
print(f"La tupla final con el numero entero,cadena de texto y numero decimal es: {tuplaaa_finaaal}")




# Ejercicio 7: Tuplas anidadas. Crea una tupla que contenga otro tupla en su interior. Luego accede al primer valor de la tupla interna

print("------------------ Ejercicio 7 --------------------")

miii_tuplaaa = (1,2, (10,20,30),4) # Crear una tupla que contenga otro tupla
primer_valor = miii_tuplaaa[2][0] # Para acceder al primer valor de la tupla interna (El indice 2 es la tupla interna,y el 0 es el primer valor de la tupla interna) (10)
print(f"El primer valor de la tupla interna es: {primer_valor}")


