# Uso de listas y .remove en listas. Ejercicios y practicas

print("------------ Ejercicios de .remove en listas en clase -----------")

# Quitar un elemento de la lista

frutas = ["Manzana","Banana","Naranja","Banana"]
frutas.remove("Banana") # Para eliminar la primera aparicion del valor 'Banana' en la lista
print(frutas)



# Quitar un elemento de la lista

futbol = ["Cali","America","Nacional","Pasto","Medellin"]
futbol.remove("Pasto") # Para eliminar la primera y unica aparicion del valor 'Pasto' en la lista
print(futbol)



# Dejar la lista vacia o eliminar todo

frutas1 = ["Manzana","Banana","Naranja","Banana"]
frutas1 = [] # Para vaciarla sin tener que usar .clear()
print(frutas1)



# Eliminar una opcion de aperitivo para fiesta

aperitivos = ["Camarones","Empanadas","Papitas"]
print(aperitivos)
eliminar = input("De las empanadas,camarones,papitas que no te gusta para un aperitivo? Escribelo empezando en mayuscula de forma clara por favor: ") # Para preguntar al usuario que aperitivo de la lista no le gusta
aperitivos.remove(eliminar)
print(f"El aperitivo que no le gusto al usuario fue: {eliminar},quedando la lista de los aperitivos asi: {aperitivos}")



# Eliminar un numero de la lista

numeros = [1,2,3,4]
print(numeros)
eliminarr = int(input("Del 1 al 4,que numero no te gusta?: ")) # Para preguntar al usuario que numero del 1 al 4 no le gusta
numeros.remove(eliminarr) # Para remover el numero que dijo el usuario que no le gusta
print(f"El numero que no le gusta al usuario es el {eliminarr}, quedando eliminado de la lista y quedando la lista asi: {numeros}")



# Quitar un equipo que no le gusta al usuario

futbol = ["Cali","Boca J","Ajax","Leon"]
equi = input("De la siguiente lista de equipos: ['Cali','Boca J','Ajax','Leon'], cual no quieres que clasifique para removerlo de la lista? Escribelo tal cual: ") # Para preguntar al usuario que equipo desea remover de la lista
futbol.remove(equi) # Elimina la primera aparicion del valor que dio el usuario de la lista
print(f"El equipo que el usuario no quiere que clasifique es el: {equi} y en la lista sin ese equipo seria asi: {futbol}")