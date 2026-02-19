# Ejercicios/Ejemplos de Indexacion. Ejemplos y Practicas

print("---- Ejercicios de indexacion en clase ----")

# Nombre

nombre = "Camila"
print(nombre[0])  # Imprime la primera letra que hay en la posicion 0 ('C')


# Ultima letra de una palabra

palabra = "computador"
print(palabra[-1]) # Imprime la ultima letra que hay en la posicion -1 ('r')


# Nombre

nombre = "Alejandro"
print(nombre[0:3]) # Imprime desde la primera letra hasta la de indice 2 ('Ale')


# Palabra

frase = "programar"
print(frase[2:6]) # Imprime desde la posicion 2 hasta la 5 ('ogra')


# Lista de numeros

numeros = [10, 20, 30, 40]
print(numeros[1]) # Imprime el valor de la posicion 1 (20)


# Frase

frase2 = "Amo Python"
print(frase2[4:10]) # Imprime desde la posicin 4 hasta la 9 ('Python')


# Frase

fras3 = "Gracias al SENA tengo muchas oportunidades"
print(fras3[11:15]) # Imprime desde la posicion 11 hasta la 14 ('SENA')


# Mitad de una palabra

palabras = input("Ingresa una palabra de 4 letras: ") # Para pedir una palabra de 4 letras al usuario
proceso = palabras[0:2] # Agarra la mitad de la palabra ingresada por el usuario desde 0:1
print(f"La mitad de la palabra {palabras} es {proceso}") # Imprime la mitad de la palabra ingresada por el usuario


# Sacar la ultima letra de una palabra

palabrass = input("Ingresa una palabra de 8 letras: ") # Para pedir una palabra de 8 letras al usuario
procesos = palabrass[-1] # Agarra la ultima letra de la palabra ingresada por el usuario
print(f"La ultima letra de la palabra {palabrass} es {procesos}") # Imprime la ultima letra de la palabra del usuario


# Palabra

palabra5 = "teléfono"
print(palabra5[2:6])  # Imprime desde la posicion 2 hasta 5 ('lefo')


# Palabra

palabra1 = "elefante"
print(palabra1[1:5]) # Imprime desde la posicion 1 hasta 4 ('lefa')