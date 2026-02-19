# Ejercicio 9
# Crea una clase 'Producto' con precio y cantidad,y un metodo para calcular el valor total del inventario

# Definición de la clase Producto
class Producto():
    # Método constructor: recibe nombre, precio y cantidad y los guarda en atributos
    def __init__ (self,nombre,precio,cantidad):
        self.nombre = nombre       # Guarda el nombre del producto en el atributo 'nombre'
        self.precio = precio       # Guarda el precio unitario en el atributo 'precio'
        self.cantidad = cantidad   # Guarda la cantidad en el atributo 'cantidad'
    # Método comprar: imprime los datos ingresados y calcula el total
    def comprar(self):
        print(f"""
Has comprado:
El producto: {self.nombre}
Precio: {self.precio}
La cantidad: {self.cantidad}
Y el total a pagar por eso es: {self.precio* self.cantidad}$""")  # Multiplica precio * cantidad para mostrar el total


# Crea una instancia 'cliente1' pidiendo al usuario nombre, precio y cantidad
cliente1 = Producto(input("Ingresa el nombre del producto: "),float(input("Ingresa el precio del producto: ")),int(input(f"Ingresa la cantidad de ese producto que vas a comprar: ")))
# Crea una instancia 'cliente2' pidiendo al usuario nombre, precio y cantidad
cliente2 = Producto(input("Ingresa el nombre del producto: "),float(input("Ingresa el precio del producto: ")),int(input(f"Ingresa la cantidad de ese producto que vas a comprar: ")))
# Crea una instancia 'cliente3' pidiendo al usuario nombre, precio y cantidad
cliente3 = Producto(input("Ingresa el nombre del producto: "),float(input("Ingresa el precio del producto: ")),int(input(f"Ingresa la cantidad de ese producto que vas a comprar: ")))
# Crea una instancia 'cliente4' pidiendo al usuario nombre, precio y cantidad
cliente4 = Producto(input("Ingresa el nombre del producto: "),float(input("Ingresa el precio del producto: ")),int(input(f"Ingresa la cantidad de ese producto que vas a comprar: ")))
# Crea una instancia 'cliente5' pidiendo al usuario nombre, precio y cantidad
cliente5 = Producto(input("Ingresa el nombre del producto: "),float(input("Ingresa el precio del producto: ")),int(input(f"Ingresa la cantidad de ese producto que vas a comprar: ")))

# Llama al método comprar() de la instancia cliente1 para mostrar su información y total
cliente1.comprar()
# Llama al método comprar() de la instancia cliente2 para mostrar su información y total
cliente2.comprar()
# Llama al método comprar() de la instancia cliente3 para mostrar su información y total
cliente3.comprar()
# Llama al método comprar() de la instancia cliente4 para mostrar su información y total
cliente4.comprar()
# Llama al método comprar() de la instancia cliente5 para mostrar su información y total
cliente5.comprar()





# Ejercicio 10
# Diseña una clase 'Animal' con un metodo hablar() que se sobreescriba en clases hijas como 'Perro' y 'Gato'

# Definición de la clase base Animal
class Animal():
    # Constructor que inicializa nombre, genero y edad
    def __init__(self,nombre,genero,edad):
        self.nombre = nombre   # Guarda el nombre del animal
        self.genero = genero   # Guarda el género del animal
        self.edad = edad       # Guarda la edad del animal
    # Método hablar vacío que será sobreescrito por las subclases
    def hablar(self):
        pass

# Definición de la subclase Vaca que hereda de Animal
class Vaca(Animal):
    # Implementación del método hablar para las vacas
    def hablar(self):
        print(f"{self.nombre} hace Muuu!")

# Definición de la subclase Perro que hereda de Animal
class Perro(Animal):
    # Implementación del método hablar para los perros
    def hablar(self):
        print(f"{self.nombre} hace Guau")

# Definición de la subclase Gato que hereda de Animal
class Gato(Animal):
    # Implementación del método hablar para los gatos
    def hablar(self):
        print(f"{self.nombre} hace Miau")

# Definición de la subclase Pollito que hereda de Animal
class Pollito(Animal):
    # Implementación del método hablar para los pollitos
    def hablar(self):
        print(f"{self.nombre} hace Pio Pio!")

# Definición de la subclase Gallo que hereda de Animal
class Gallo(Animal):
    # Implementación del método hablar para los gallos
    def hablar(self):
        print(f"{self.nombre} hace Kikiriki!")

# Definición de la subclase Oveja que hereda de Animal
class Oveja(Animal):
    # Implementación del método hablar para las ovejas
    def hablar(self):
        print(f"{self.nombre} hace Mejejeje!")


# Creación de la instancia 'mascota1' de tipo Gato pidiendo nombre, genero y edad al usuario
mascota1 = Gato(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))
# Creación de la instancia 'mascota2' de tipo Perro pidiendo nombre, genero y edad al usuario
mascota2 = Perro(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))
# Creación de la instancia 'mascota3' de tipo Vaca pidiendo nombre, genero y edad al usuario
mascota3 = Vaca(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))
# Creación de la instancia 'mascota4' de tipo Pollito pidiendo nombre, genero y edad al usuario
mascota4 = Pollito(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))
# Creación de la instancia 'mascota5' de tipo Gallo pidiendo nombre, genero y edad al usuario
mascota5 = Gallo(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))
# Creación de la instancia 'mascota6' de tipo Oveja pidiendo nombre, genero y edad al usuario
mascota6 = Oveja(input("Ingresa un nombre: "),input("Ingresa su genero: "),int(input("Ingresa sus años de edad: ")))

# Llamadas a hablar() para cada mascota, mostrando el sonido correspondiente
mascota1.hablar()
mascota2.hablar()
mascota3.hablar()
mascota4.hablar()
mascota5.hablar()
mascota6.hablar()






# Ejercicio 13
# Diseña una clase ConversorTemperatura que convierta de Celsius a Fahrenheit y viceversa

# Definición de la clase base ConversorTemperatura
class ConversorTemperatura:
    # Constructor que recibe 'nombre' (tipo de escala) y 'cantidad' (valor numérico)
    def __init__(self, nombre, cantidad):
        self.nombre = nombre     # Guarda el nombre de la escala (por ejemplo "Celsius")
        self.cantidad = cantidad # Guarda el valor numérico a convertir


# Definición de la subclase PasarF_a_C para convertir Fahrenheit a Celsius
class PasarF_a_C(ConversorTemperatura):
    # Método convertir que aplica la fórmula para pasar de F a C
    def convertir(self):
        resultado = (self.cantidad - 32) / 1.8  # Calcula (F - 32) / 1.8
        print(f"{self.cantidad}° {self.nombre} equivalen a {resultado}° Celsius")  # Muestra el resultado


# Definición de la subclase PasarC_a_F para convertir Celsius a Fahrenheit
class PasarC_a_F(ConversorTemperatura):
    # Método convertir que aplica la fórmula para pasar de C a F
    def convertir(self):
        resultado = (self.cantidad * 1.8) + 32  # Calcula (C * 1.8) + 32
        print(f"{self.cantidad}° {self.nombre} equivalen a {resultado}° Fahrenheit")  # Muestra el resultado


# Primera ejecución: pide al usuario qué conversión desea realizar
opcion1 = int(input("Si deseas pasar de Fahrenheit a Celsius ingresa 1, y si deseas pasar de Celsius a Fahrenheit ingresa 2: "))

# Si elige 1 -> crea PasarF_a_C con el valor ingresado y llama a convertir()
if opcion1 == 1:
    temp = PasarF_a_C("Fahrenheit", float(input("Ingresa la cantidad de Fahrenheit: ")))
    temp.convertir()
# Si elige 2 -> crea PasarC_a_F con el valor ingresado y llama a convertir()
elif opcion1 == 2:
    temp = PasarC_a_F("Celsius", float(input("Ingresa la cantidad de Celsius: ")))
    temp.convertir()
# Si ingresa otra cosa -> muestra mensaje de error
else:
    print("Opción no válida, debes ingresar 1 o 2.")


# Segunda ejecución: se repite el mismo proceso pidiendo otra vez la opción al usuario
opcion2 = int(input("Si deseas pasar de Fahrenheit a Celsius ingresa 1, y si deseas pasar de Celsius a Fahrenheit ingresa 2: "))

if opcion2 == 1:
    temp = PasarF_a_C("Fahrenheit", float(input("Ingresa la cantidad de Fahrenheit: ")))
    temp.convertir()
elif opcion2 == 2:
    temp = PasarC_a_F("Celsius", float(input("Ingresa la cantidad de Celsius: ")))
    temp.convertir()
else:
    print("Opción no válida, debes ingresar 1 o 2.")


# Tercera ejecución: se repite nuevamente el mismo proceso
opcion3 = int(input("Si deseas pasar de Fahrenheit a Celsius ingresa 1, y si deseas pasar de Celsius a Fahrenheit ingresa 2: "))

if opcion3 == 1:
    temp = PasarF_a_C("Fahrenheit", float(input("Ingresa la cantidad de Fahrenheit: ")))
    temp.convertir()
elif opcion3 == 2:
    temp = PasarC_a_F("Celsius", float(input("Ingresa la cantidad de Celsius: ")))
    temp.convertir()
else:
    print("Opción no válida, debes ingresar 1 o 2.")
