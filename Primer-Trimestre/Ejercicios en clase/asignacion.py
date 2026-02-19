# Asignacion ejercicios y practica

print("------------------ Ejercicios de asignacion en clase -------------------")

# Concatenar texto en una sola variable

mensaje = "Hola "
mensaje += "Colombia"  # Se suma texto a la variable 'mensaje' usando +=
print(mensaje)  


# Concatenar nombre completo en una sola variable

nombre = "Sergio "
nombre += "Andres "   # Se agregan partes del nombre usando +=
nombre += "Bustos "
nombre += "Mondragon "
print(nombre)  


# Asignación múltiple: define varias variables en una sola línea

x, y, z = 1, 2, 3
print(x, y, z)  # Muestra los valores de las variables una por una


# Concatenar texto progresivamente en una sola variable

mens = "El SENA "
mens += "da muchas oportunidades "
mens += "para los colombianos" # Se agregan partes del mensaje usando +=
print(mens)  


# Concatenar datos ingresados por el usuario

nombre_completo = ""
nombre_completo += input("Ingresa tus nombres: ")  # Agrega el nombre ingresado
nombre_completo += " "
nombre_completo += input("Ingresa tus apellidos: ")  # Agrega el apellido ingresado
print(f"Tu nombre completo es: {nombre_completo}")  


# Concatenar descripción de Python

texto = "Python"
texto += " es genial"  # Se añade más texto a la variable
print(texto) 


# Asignación con resta

contador = 100
contador -= 50  # Resta 50 al valor de 'contador' usando -=
print(contador) 


# Asignación con potenciación

x = 2
x **= 3  # Eleva 2 a la potencia de 3 (2^3 = 8) usando **=
print(x)


# Asignación con división

total = 20
total /= 4  # Divide el total entre 4 usando /=
print(total) 


# Asignación con suma

num1 = 2
num1 += 3  # Suma 3 al valor actual de num1 usando +=
print(num1) 


# Concatenar oración completa usando varias asignaciones

uno = "Python "
uno += "es un lenguaje "
uno += "de programacion "
uno += "versatil" # Se añaden para completar la frase usando +=
print(uno)  


# Concatenar dos frases dadas por el usuario

primer = input("Ingresa cualquier mensaje inicial: ")
primer += " "
primer += input("Ingresa el mensaje final: ")  # Une los dos mensajes del usuario usando +=
print(primer)  