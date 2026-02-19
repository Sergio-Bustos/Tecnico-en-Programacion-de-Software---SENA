# Conversor de monedas

class Conversor:
    def __init__(self, valor1):
        self.valor1 = valor1
        self.valor2 = valor1 / 4000  # tasa fija de cambio

    def pasar(self):
        print(f"COP {self.valor1} es un total de USD {self.valor2}")


persona1 = Conversor(float(input("Ingresa la cantidad de COP: ")))

print("Pasando de COP a USD, danos un momento ;)\n")
persona1.pasar()

print("""Solo se identifica una clase, llamada Conversor.
Esta clase se encarga de convertir una cantidad en pesos colombianos (COP) a dólares estadounidenses (USD) utilizando una tasa fija de cambio (1 USD = 4000 COP).""")
    
# ¿Qué atributos y métodos tendría cada clase? 
print("""La unica y principal clase tendria;
      ------------- ATRIBUTOS: ----------------
      - valor1: cantidad en pesos colombianos (COP)
      - valor2: cantidad convertida a dólares (USD), calculada automáticamente al crear el objeto
      ------------- METOODOS: -----------------
      - pasar(): imprime en pantalla el resultado de la conversión de COP a USD""")

# ¿Qué relaciones existen entre ellas? 
print("""No existen relaciones entre clases, porque el programa solo utiliza una clase (Conversor).
Todos los datos y la lógica están contenidos dentro de esa única clase, y no hay ninguna interacción con otras clases como Usuario, Moneda, o Transacción.""")


# Del curso de POO:
# Crea una clase llamada “Automovil”.
# Declara al menos tres atributos y tres métodos dentro.
# Usa los atributos en por lo menos un método
# Usa parámetros especiales en alguno de los métodos
# Crea dos instancias y llama a alguno de sus métodos.

class Automovil:
    def __init__(self,marca,precio,año_de_fabricacion):
        self.marca = marca
        self.precio = precio
        self.año_de_fabricacion = año_de_fabricacion
    def conducir(self):
        print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} esta conduciendo actualmente")
    def frenar(self):
        print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} acabó de frenar")
    def acelerar(self):
        print(f" Carro: {self.marca}, Precio: {self.precio}, Año de fabricacion: {self.año_de_fabricacion} acabó de acelerar")

carro1 = Automovil("BMW","1.200.000","2024")
carro1.frenar()
carro2 = Automovil("Chevrolet","1.200.000","2024")
carro2.conducir()
carro3 = Automovil("Audi","1.400.000.000","2009")
carro3.acelerar()


# Maestro del curso de POO:
class Maestro:
    def __init__(self,nombre,edad,escuela):
        self.nombre = nombre
        self.edad = edad
        self.escuela = escuela
    def comer(self):
        print(f"""
El profesor: {self.nombre}
de edad: {self.edad} 
en la escuela: {self.escuela} esta comiendo su desayuno
""")
    def enseñar(self):
        print(f"""
El profesor: {self.nombre}
de edad: {self.edad} 
en la escuela: {self.escuela} esta enseñando su materia
""")
    def enseñar(self):
        print(f"""
El profesor: {self.nombre}
de edad: {self.edad} 
en la escuela: {self.escuela} esta enseñando su materia
""")
    
maestro1 = Maestro("Luis","15","La Milagrosa")
maestro1.comer()
maestro2 = Maestro("Carlos","27","Nuestra señora del palmar")
maestro2.enseñar()
        

         



# Ejemplo de herencia y explicacion de encapsulamiento en la documentacion

class Animal:
    def __init__(self, animal, edad, color):
        self.animal = animal
        self.edad = edad
        self.color = color

# Clase hija que hereda de Animal
class Gato(Animal):
    def __init__(self, animal, edad, color, nombre):
        # Llama al constructor de la clase padre
        super().__init__(animal, edad, color)
        self.nombre = nombre # Atributo propio de la clase hija

    def maullar(self):
        print(f"El {self.animal} llamado {self.nombre} está maullando y dice: ¡Miau!")

#  Clase hija que hereda de Animal
class Perro(Animal):
    def __init__(self, animal, edad, color, nombre):
        super().__init__(animal, edad, color)
        self.nombre = nombre # Se puede ocutlar informacion de encapsulamiento mediante self.__nombre = nombre
        # Y para acceder a este se podria hacer asi:
        # def verMinombre(self):
        # return self.__nombre;

    def ladrar(self):
        print(f"El {self.animal} llamado {self.nombre} está ladrando y dice: ¡Guau guau!")

#  Crear objetos
masc1 = Gato("Gato", "15 años", "Rojo", "Stuart")
masc1.maullar()

masc2 = Perro("Perro", "10 años", "Negro", "Toby")
masc2.ladrar()


# Ejemplo con encapsulamiento

class Carro:
    def __init__(self,marca,precio,añodefab):
        self.__marca = marca
        self.precio = precio
        self.añodefab = añodefab

    def conducir(self):
        print(f""" El carro:
              de marca {self.__marca},
              de precio: {self.precio},
              fabricado en el año: {self.añodefab} esta conduciendo actualmente en la carretera""")
    def frenar(self):
        print(f""" El carro:
              de marca {self.__marca},
              de precio: {self.precio},
              fabricado en el año: {self.añodefab} esta frenando actualmente en la carretera""")
    def verLamarca(self):
        return self.__marca

carro1 = Carro("BMW","18.000.000","2025")
carro1.frenar()
print(f"Marca del primer carro: {carro1.verLamarca()}")

carro2 = Carro("BMW","18.000.000","2020")
carro2.conducir()
print(f"Marca del segundo carro: {carro2.verLamarca()}")




class Pastel:
    def __init__(self,precio,ingredienteprincipal,cocinero):
        self.precio = precio
        self.ingredienteprincipal = ingredienteprincipal
        self.cocinero = cocinero





# Clase abstracta

from abc import ABC, abstractmethod # Se importan algunas librerias

class Persona(ABC): # Se crea la clase basada en una libreria
    def __init__(self, edad, nombre): # Constructor de la clase
        self.edad = edad # Atributo edad
        self.nombre = nombre # Atributo nombre
        print("Se ha creado a", self.nombre, "de", self.edad) # Mensaje de creacion de la persona

    @abstractmethod # Metodo abstracto

    def hablar(self, mensaje): # Constructor del metodo hablar
        pass

class Deportista(Persona): # Clase hija que hereda de Persona
    def __init__(self, edad, nombre, deporte): # Constructor de la clase hija
        super().__init__(edad, nombre) # Llama al constructor de la clase padre
        self.deporte = deporte # Atributo deporte; Llama los atributos de la clase padre para sobreescribir otro en Deportista
        print("Se ha creado a", self.nombre, "de", self.edad) # Mensaje de creacion de la persona deportista

    def practicarDeporte(self): # Metodo practicarDeporte
        print(self.nombre, ": voy a practicar", self.deporte) # Mensaje de practica de deporte

    def verMiDeporte(self): # Metodo verMiDeporte
        return self.deporte # Retorna el deporte del deportista

    def hablar(self, mensaje): # Implementacion del metodo hablar
        print(f"{self.nombre} dice: {mensaje}")     # Mensaje de habla del deportista

luis = Deportista("18", "Luis", "natacion")     # Creacion de un objeto de la clase Deportista
luis.hablar("Hola soy Sergio el amigo de Luis")    # Llamada al metodo hablar
luis.practicarDeporte() # Llamada al metodo practicarDeporte
print("Luis practica", luis.verMiDeporte()) # Llamada al metodo verMiDeporte





# III.	Usa tu IDE para crear dos subclases de la siguiente clase :

class Animal: # Clase base Animal
    def __init__(self): # Constructor de la clase Animal
        print("Ha nacido un animal!") # Mensaje de creacion del animal
    def rugir(self): # Metodo rugir
        print ("Y hace un ruido") # Mensaje de rugido del animal


class Perro(Animal): # Clase hija Perro que hereda de Animal
    def __init__(self): # Constructor de la clase Perro
        super().__init__() # Llama al constructor de la clase padre
        print("Ha nacido un perro") # Mensaje de creacion del perro
    def rugir(self): # Metodo rugir sobreescrito
        print("El perro ladra: ¡Guau guau!")   # Mensaje de ladrido del perro





# IV.	Crea dos subclases de	“FiguraRegular” que definan el método para calcular su área respectiva según el número de lados, y almacenarla en el atributo “area”. Crea una instancia de cada una.

class FiguraRegular(ABC): # Clase base FiguraRegular
    def __init__(self, num_lados): # Constructor de la clase FiguraRegular
        self.num_lados = num_lados # Atributo num_lados
        self.area = 0 # Atributo area inicializado en 0

    @abstractmethod # Metodo abstracto para calcular el area
    def calcular_area(self):
        pass
class Cuadrado(FiguraRegular): # Clase hija Cuadrado que hereda de FiguraRegular
    def __init__(self, lado): # Constructor de la clase Cuadrado
        super().__init__(4) # Llama al constructor de la clase padre con 4 lados
        self.lado = lado # Atributo lado

    def calcular_area(self): # Metodo para calcular el area del cuadrado
        self.area = self.lado ** 2 # Calcula el area del cuadrado
        return self.area # Retorna el area calculada
class Triangulo(FiguraRegular): # Clase hija Triangulo que hereda de FiguraRegular
    def __init__(self, base, altura): # Constructor de la clase Triangulo
        super().__init__(3) # Llama al constructor de la clase padre con 3 lados
        self.base = base # Atributo base
        self.altura = altura # Atributo altura

    def calcular_area(self): # Metodo para calcular el area del triangulo
        self.area = (self.base * self.altura) / 2 # Calcula el area del triangulo
        return self.area # Retorna el area calculada    
# Crear instancias y calcular areas
cuadrado = Cuadrado(5) # Instancia de Cuadrado con lado 5
print("Área del cuadrado:", cuadrado.calcular_area()) # Imprime el area del cuadrado        
triangulo = Triangulo(4, 6) # Instancia de Triangulo con base 4 y altura 6
print("Área del triángulo:", triangulo.calcular_area()) # Imprime el area del triangulo




# V.	Crea dos implementaciones de la siguiente clase abstracta:

from abc import ABCMeta, abstractmethod # Se importan algunas librerias
class Transporte:       # Clase base Transporte
 metaclass  = ABCMeta   # Define la metaclase para Transporte
def  init (self, medio): self.medio = medio         # Constructor de la clase Transporte
#Usar el atributo "medio" para definir como avanza
@abstractmethod
def avanzar(self, frase): pass   # Metodo abstracto avanzar
def giraIzquierda(self): # Metodo giraIzquierda
   print("Gira a la izquierda")
def giraDerecha(self):  # Metodo giraDerecha
   print("Gira a la derecha")

#De acuerdo al "medio" especificar que hace para frenar
@abstractmethod
def detener(self): pass       # Clase hija Bicicleta que hereda de Transporte
class Bicicleta(Transporte): # Clase hija Bicicleta que hereda de Transporte
 def  init (self): # Constructor de la clase Bicicleta
   super(). init ("terrestre") # Llama al constructor de la clase padre con medio "terrestre"
 def avanzar(self, frase): # Metodo para avanzar la bicicleta
   print (f"La bicicleta avanza pedaleando: {frase}")# Mensaje de avance de la bicicleta
 def detener(self): #    Metodo para detener la bicicleta
   print ("La bicicleta frena con los frenos de mano") # Mensaje de detencion de la bicicleta
class Barco(Transporte): # Clase hija Barco que hereda de Transporte
 def  init (self): # Constructor de la clase Barco
   super(). init ("acuático") # Llama al constructor de la clase padre con medio "acuático"
 def avanzar(self, frase): # Metodo para avanzar el barco
   print (f"El barco avanza navegando: {frase}") # Mensaje de avance del barco
 def detener(self): # Metodo para detener el barco
   print ("El barco frena con anclas")      # Mensaje de detencion del barco
# Crear instancias y probar métodos
bicicleta = Bicicleta()         
bicicleta.avanzar("Pedaleando fuerte")
bicicleta.detener()
barco = Barco()
barco.avanzar("Remando con fuerza") 
barco.detener()


# CLASE PADRE
class Animal:
    def __init__(self,nombre,edad): # Constructor de la clase con sus atributos
        self.nombre = nombre # Atributo 1
        self.edad = edad # Atributo 2

# PRIMERA CLASE QUE HEREDA

class Felino(Animal): # Clase Felino que hereda de padre (Animal)
    def __init__(self,nombre,edad,raza): # Constructor de la clase
        super().__init__(nombre,edad) # super().__init__ ayuda a conservar los mismos atributos que la clas padre
         # Es como pedir ayuda a la clase padre al crear un nuevo objeto en la clase hija. Garantiza que tanto el código de configuración de la clase padre como el de la hija se ejecuten correctamente, garantizando así un inicio perfecto
        self.raza = raza # Atributo de la propia clase; polimorfismo

    def maullar(self): # Metodo maullar propio de la clase Felino
        print(f"El gato de nombre: {self.nombre},de edad: {self.edad} años de raza {self.raza} esta maullando") # Mensaje
# Instancias de la clase Felino
gato1 = Felino("Stuart",15,"Negro")
gato1.maullar()



# SEGUNDA CLASE QUE HEREDA

class Canino(Animal): # Clase hija que hereda
    def __init__(self,nombre,edad,raza): # Constructor de la clase  con los atributos
        super().__init__(nombre,edad) # Super init nos ayuda a guardar los atributos 
        self.raza = raza # Atributo propio de la clase canino
    def ladrar(self): # Metodo ladrar
        print(f""" El perro 
              de nombre: {self.nombre}
              de edad: {self.edad}
              de raza: {self.raza}
""")    # Mensaje

# INSTANCIAS DE LA CLASE
canino1 = Canino("Sussy",16,"Beagle")
canino1.ladrar()


# TKINTER

import tkinter as tk

# Crear ventana
ventana = tk.Tk()
ventana.title("Ejemplo 1 - Ventana básica")
ventana.geometry("300x200")  # Ancho x Alto

# Mostrar ventana
ventana.mainloop()

# ===============================================

import tkinter as tk

ventana = tk.Tk()
ventana.title("Etiqueta")

# Crear etiqueta
etiqueta = tk.Label(ventana, text="Hola, Tkinter!")
etiqueta.pack()

ventana.mainloop()

# ===============================================

import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "Diste clic en el botón.")

ventana = tk.Tk()
ventana.title("Botón con acción")

boton = tk.Button(ventana, text="Haz clic", command=mostrar_mensaje)
boton.pack()

ventana.mainloop()

# ===============================================

import tkinter as tk

ventana = tk.Tk()
ventana.title("Entrada de texto")

entrada = tk.Entry(ventana, width=30)
entrada.pack()

ventana.mainloop()

# ===============================================

import tkinter as tk

def mostrar():
    texto = entrada.get()  # Obtener texto del Entry
    etiqueta.config(text=f"Escribiste: {texto}")

ventana = tk.Tk()
ventana.title("Leer Entry")

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar)
boton.pack()

etiqueta = tk.Label(ventana, text="")
etiqueta.pack()

ventana.mainloop()

# ===============================================

import tkinter as tk

def cambiar():
    etiqueta.config(text="Texto cambiado!")

ventana = tk.Tk()
ventana.title("Cambiar Label")

etiqueta = tk.Label(ventana, text="Texto original")
etiqueta.pack()

boton = tk.Button(ventana, text="Cambiar", command=cambiar)
boton.pack()

ventana.mainloop()

# ==============================

# CODIGO SIN REFACTORIZAR
# Este código calcula el precio final con IVA y hace un print.
# Pero está repetido, con variables malas y lógica duplicada.

producto1 = 50
producto2 = 80

iva = 0.19

precio_final1 = producto1 + (producto1 * iva)
print("Precio final del producto 1:", precio_final1)

precio_final2 = producto2 + (producto2 * iva)
print("Precio final del producto 2:", precio_final2)



# CODIGO REFACTORIZADO
# Función simple para calcular precio final
def calcular_iva(precio):
    iva = 0.19
    return precio + (precio * iva) # ej: 100 + (100 * 0.19)

# Usar la función
precio1 = calcular_iva(100)
precio2 = calcular_iva(70)

print("El precio final 1 es:", precio1)
print("El precio final 2 es:", precio2)

# ==============================

# CODIGO SIN REFACTORIZAR
# Determinar si alguien es mayor de edad

edad1 = 15
if edad1 >= 18:
    print("Persona 1: Es mayor de edad")
else:
    print("Persona 1: Es menor de edad")

edad2 = 22
if edad2 >= 18:
    print("Persona 2: Es mayor de edad")
else:
    print("Persona 2: Es menor de edad")



# CODIGO REFACTORIZADO
# Función sencilla para verificar mayoría de edad

def mayor_edad(edad):
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

# Usar la función
mayor_edad(15)
mayor_edad(22)

# ==============================