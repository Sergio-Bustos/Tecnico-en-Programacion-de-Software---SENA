# Actividad 2 


# Pedir cantidad

cantidad = int(input("Ingrese la cantidad de estudiantes (Máximo 5 estudiantes): "))

# Lista donde guardaremos todos los estudiantes

estudiantes = []


# Si es solo un estudiante:

if cantidad == 1:
    nombre1 = input("Ingresa el nombre del único estudiante: ")
    notas1 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio1 = sum(notas1) / len(notas1)
    if promedio1 >= 3.5:
        situacion1 = "Aprobado"
    elif promedio1 >= 2.5:
        situacion1 = "En recuperación"
    else:
        situacion1 = "Reprobado"
    estudiante1 = {"nombre": nombre1, "notas": notas1, "promedio": promedio1, "situacion": situacion1}
    estudiantes.append(estudiante1)


# Si es dos estudiantes:

elif cantidad == 2:


    # Estudiante 1
    nombre1 = input("Ingresa el nombre del primer estudiante: ")
    notas1 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio1 = sum(notas1) / len(notas1)
    if promedio1 >= 3.5:
        situacion1 = "Aprobado"
    elif promedio1 >= 2.5:
        situacion1 = "En recuperación"
    else:
        situacion1 = "Reprobado"
    estudiante1 = {"nombre": nombre1, "notas": notas1, "promedio": promedio1, "situacion": situacion1}
    estudiantes.append(estudiante1)



    # Estudiante 2
    nombre2 = input("Ingresa el nombre del segundo estudiante: ")
    notas2 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio2 = sum(notas2) / len(notas2)
    if promedio2 >= 3.5:
        situacion2 = "Aprobado"
    elif promedio2 >= 2.5:
        situacion2 = "En recuperación"
    else:
        situacion2 = "Reprobado"
    estudiante2 = {"nombre": nombre2, "notas": notas2, "promedio": promedio2, "situacion": situacion2}
    estudiantes.append(estudiante2)

# Si es 3 estudiantes:

elif cantidad == 3:

    # Estudiante 1
    nombre1 = input("Ingresa el nombre del primer estudiante: ")
    notas1 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio1 = sum(notas1) / len(notas1)
    if promedio1 >= 3.5:
        situacion1 = "Aprobado"
    elif promedio1 >= 2.5:
        situacion1 = "En recuperación"
    else:
        situacion1 = "Reprobado"
    estudiante1 = {"nombre": nombre1, "notas": notas1, "promedio": promedio1, "situacion": situacion1}
    estudiantes.append(estudiante1)

    # Estudiante 2


    nombre2 = input("Ingresa el nombre del segundo estudiante: ")
    notas2 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio2 = sum(notas2) / len(notas2)
    if promedio2 >= 3.5:
        situacion2 = "Aprobado"
    elif promedio2 >= 2.5:
        situacion2 = "En recuperación"
    else:
        situacion2 = "Reprobado"
    estudiante2 = {"nombre": nombre2, "notas": notas2, "promedio": promedio2, "situacion": situacion2}
    estudiantes.append(estudiante2)

    # Estudiante 3


    nombre3 = input("Ingresa el nombre del tercer estudiante: ")
    notas3 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio3 = sum(notas3) / len(notas3)
    if promedio3 >= 3.5:
        situacion3 = "Aprobado"
    elif promedio3 >= 2.5:
        situacion3 = "En recuperación"
    else:
        situacion3 = "Reprobado"
    estudiante3 = {"nombre": nombre3, "notas": notas3, "promedio": promedio3, "situacion": situacion3}
    estudiantes.append(estudiante3)

# Si son 4 estudiantes:

elif cantidad == 4:
    # Estudiante 1

    nombre1 = input("Ingresa el nombre del primer estudiante: ")
    notas1 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio1 = sum(notas1) / len(notas1)
    if promedio1 >= 3.5:
        situacion1 = "Aprobado"
    elif promedio1 >= 2.5:
        situacion1 = "En recuperación"
    else:
        situacion1 = "Reprobado"
    estudiante1 = {"nombre": nombre1, "notas": notas1, "promedio": promedio1, "situacion": situacion1}
    estudiantes.append(estudiante1)

    # Estudiante 2

    nombre2 = input("Ingresa el nombre del segundo estudiante: ")
    notas2 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio2 = sum(notas2) / len(notas2)
    if promedio2 >= 3.5:
        situacion2 = "Aprobado"
    elif promedio2 >= 2.5:
        situacion2 = "En recuperación"
    else:
        situacion2 = "Reprobado"
    estudiante2 = {"nombre": nombre2, "notas": notas2, "promedio": promedio2, "situacion": situacion2}
    estudiantes.append(estudiante2)

    # Estudiante 3

    nombre3 = input("Ingresa el nombre del tercer estudiante: ")
    notas3 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio3 = sum(notas3) / len(notas3)
    if promedio3 >= 3.5:
        situacion3 = "Aprobado"
    elif promedio3 >= 2.5:
        situacion3 = "En recuperación"
    else:
        situacion3 = "Reprobado"
    estudiante3 = {"nombre": nombre3, "notas": notas3, "promedio": promedio3, "situacion": situacion3}
    estudiantes.append(estudiante3)

    # Estudiante 4

    nombre4 = input("Ingresa el nombre del cuarto estudiante: ")
    notas4 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio4 = sum(notas4) / len(notas4)
    if promedio4 >= 3.5:
        situacion4 = "Aprobado"
    elif promedio4 >= 2.5:
        situacion4 = "En recuperación"
    else:
        situacion4 = "Reprobado"
    estudiante4 = {"nombre": nombre4, "notas": notas4, "promedio": promedio4, "situacion": situacion4}
    estudiantes.append(estudiante4)

# Si son 5 estudiantes:

elif cantidad == 5:

    # Estudiante 1

    nombre1 = input("Ingresa el nombre del primer estudiante: ")
    notas1 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio1 = sum(notas1) / len(notas1)
    if promedio1 >= 3.5:
        situacion1 = "Aprobado"
    elif promedio1 >= 2.5:
        situacion1 = "En recuperación"
    else:
        situacion1 = "Reprobado"
    estudiante1 = {"nombre": nombre1, "notas": notas1, "promedio": promedio1, "situacion": situacion1}
    estudiantes.append(estudiante1)

    # Estudiante 2

    nombre2 = input("Ingresa el nombre del segundo estudiante: ")
    notas2 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio2 = sum(notas2) / len(notas2)
    if promedio2 >= 3.5:
        situacion2 = "Aprobado"
    elif promedio2 >= 2.5:
        situacion2 = "En recuperación"
    else:
        situacion2 = "Reprobado"
    estudiante2 = {"nombre": nombre2, "notas": notas2, "promedio": promedio2, "situacion": situacion2}
    estudiantes.append(estudiante2)

    # Estudiante 3

    nombre3 = input("Ingresa el nombre del tercer estudiante: ")
    notas3 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio3 = sum(notas3) / len(notas3)
    if promedio3 >= 3.5:
        situacion3 = "Aprobado"
    elif promedio3 >= 2.5:
        situacion3 = "En recuperación"
    else:
        situacion3 = "Reprobado"
    estudiante3 = {"nombre": nombre3, "notas": notas3, "promedio": promedio3, "situacion": situacion3}
    estudiantes.append(estudiante3)

    # Estudiante 4

    nombre4 = input("Ingresa el nombre del cuarto estudiante: ")
    notas4 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio4 = sum(notas4) / len(notas4)
    if promedio4 >= 3.5:
        situacion4 = "Aprobado"
    elif promedio4 >= 2.5:
        situacion4 = "En recuperación"
    else:
        situacion4 = "Reprobado"
    estudiante4 = {"nombre": nombre4, "notas": notas4, "promedio": promedio4, "situacion": situacion4}
    estudiantes.append(estudiante4)

    # Estudiante 5

    nombre5 = input("Ingresa el nombre del quinto estudiante: ")
    notas5 = (float(input("Ingresa la primer nota: ")),float(input("Ingresa la segunda nota: ")),float(input("Ingresa la tercer nota: ")))
    promedio5 = sum(notas5) / len(notas5)
    if promedio5 >= 3.5:
        situacion5 = "Aprobado"
    elif promedio5 >= 2.5:
        situacion5 = "En recuperación"
    else:
        situacion5 = "Reprobado"
    estudiante5 = {"nombre": nombre5, "notas": notas5, "promedio": promedio5, "situacion": situacion5}
    estudiantes.append(estudiante5)

else:
    print("Cantidad inválida")

# Imprimir resultado final
print(estudiantes)