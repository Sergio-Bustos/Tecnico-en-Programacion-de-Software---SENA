# En esta actividad podras poner en practica todo lo aprendido durante la sesion


# Ejercicios de listas previamente enseñados en clase

# Dadas dos listas iniciales LISTA1 y LISTA2 debes realizar las siguientes tareas:
# Añade a la LISTA1 el int 100 y luego el string "Hola Mundo"
# Luego añade a la LISTA2 el string "Hola y Adios" y luego el int 300
# Genera una LISTA3 con todos los elementos de la LISTA1 sin considerar el último elemento
# Genera una LISTA4 con todos los elementos de la LISTA2 menos el primero y el último elemento
# Finalmente, genera una LISTA5 con los elementos de la LISTA4 y de la LISTA3


print("------------------ Ejercicio de listas en clase -------------------")  

LISTA1 = []  
LISTA2 = []  

num1 = int(input("Ingresa el numero 100 por favor: "))  # Para pedirle el numero tipo int al usuario

texto1 = input("Ingresa 'Hola Mundo' por favor: ")  # Para pedirle el string al usuario

LISTA1.append(num1)  # .append() agrega el numero 100 al final de la lista
LISTA1.append(texto1)  # .append() agrega el string 'Hola Mundo' al final de la lista

texto2 = input("Ingresa 'Hola y Adios' por favor: ")  # Para pedirle un string al usuario
num2 = int(input("Ingresa el numero 300 por favor: "))  # Para pedirle un numero tipo int al usuario

LISTA2.append(texto2)   # .append() agrega el string 'Hola y Adios' al final de la lista
LISTA2.append(num2)   # .append() agrega el numero 300 al final de la lista

LISTA3 = LISTA1.copy()  # .copy() crea una copia de la lista sin afectar la original

LISTA3.remove("Hola Mundo")  # .remove() elimina la primera aparicion del elemento o valor en la lista

LISTA4 = LISTA2.copy()  # .copy() crea una copia de la lista

LISTA4.remove("Hola y Adios")  # .remove() elimina la primera aparicion del elemento o valor en la lista
LISTA4.remove(300)  # .remove() elimina la primera aparicion del elemento o valor en la lista
LISTA5 = []  

LISTA5.extend(LISTA4)  # .extend() agrega todos los elementos de otra lista o iterable,en este caso la lista 4
LISTA5.extend(LISTA3)  # .extend() agrega todos los elementos de otra lista o iterable,en este caso la lista 3

print(LISTA1)  
print(LISTA2)  
print(LISTA3)  
print(LISTA4)  
print(LISTA5)  