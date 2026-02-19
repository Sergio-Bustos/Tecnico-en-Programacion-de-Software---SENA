# Ejercicios entre tuplas y listas y sus converiones. Ejercicios y practicas.

print("--- Ejercicios de tuplas,listas y conversiones en clase ---")

# De tupla a lista

mi_tupla = (1,2,3)
mi_nuevalista = list(mi_tupla) # Para pasar la tupla a lista para poder modificarla
print(mi_nuevalista)

# De lista a tupla

mi_lista = [4,5,6]
mi_nuevatupla = tuple(mi_lista) # Para pasar la lista a tupla
print(mi_nuevatupla)


# Ejercicios en clase de listas y tuplas

# Ejercicio 1: Tienes una tupla con dos frutas: 'manzana' y 'pera', convierte esa tupla a lista,permite al usuario ingresar una nueva fruta por teclado,agregaa a la lista y luego vuelve a convertir todo a una mi_tupla. Finalmente,muestra la tupla resultante


print("------------------ Ejercicio 1 --------------------")

tupla = ("Manzana","Pera")
print(tupla)
minuevatupla = list(tupla) # Para pasar la tupla a lista para poder modificarla
frutas = input("Ingrese una nueva fruta por favor: ") # Para que el usuario ingresa una fruta
minuevatupla.append(frutas) # Para añadir la fruta del usuario al final de la lista
milistaotravez = tuple(minuevatupla) # Para pasar la lista a una tupla final
print(f"Tu lista quedaria asi: {minuevatupla} y la tupla final y resultante asi: {milistaotravez}")

# Ejercicio 2: Calificaciones de un estudiante: Empiezas con una tupla que contenga de notas 4.2 y 3.8 y conviertela  a una lista para que el usuario pueda ingresar una tercera nota. Convierte esta tupla a una lista para que el usuario pueda ingresar una tercera nota. Agrega la nueva nota a la lista y luego transforma la lista de nuevo en una tupla. Muestra las calificaciones finales como tupla

print("------------------ Ejercicio 2 --------------------")


tuplaadenotas = (4.2,3.8)
print(tuplaadenotas)
terceranota = float(input("Ingresa tu tercera nota en programacion: ")) # Para pedirle la nota al usuario
listadenotas = list(tuplaadenotas)  # Para pasar la tupla a lista para poder modificarla
listadenotas.append(terceranota) # Para añadir la nota del usuario al final de la lista
mituplaotravez = tuple(listadenotas) # Para pasar la la  lista a una tula final
print(f"Tu tercera nota fue {terceranota},tu lista completa fue {listadenotas} y la tupla resultante: {mituplaotravez}")

# Ejercicio 3: Datos personales: Tienes una tupla con el nombre y apellido de una persona: 'Ana','Gomez'. Convierte esta tupla en lista para que el usuario pueda ingresar su numero de documento. Agrega el documento a la lista y conviertela nuevamente en una tupla. Muestra la tupla final con los tres datos

print("------------------ Ejercicio 3 --------------------")


tupla2 = ("Ana","Gomez")
lista2 = list(tupla2)  # Para pasar la tupla a lista para poder modificarla
identidad = int(input("Ingresa tu documento de identidad: ")) # Para pedirle el documento de identidad al usuario
lista2.append(identidad) # Para añadir el documento de identidad del usuario al final de la lista
finallista = tuple(lista2) # Para pasar la la  lista a una tupla final
print(f"Tu documento de identidad es: {lista2[2]} y en la lista finalmente seria asi: {finallista}")


