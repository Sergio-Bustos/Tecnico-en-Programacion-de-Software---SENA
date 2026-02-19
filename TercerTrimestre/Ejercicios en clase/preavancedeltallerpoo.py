# Aqui por lo pronto se subiran los avances que haremos en el taller de POO;



# Parte 1: Teoria de POO; Ya hecha


# Parte 2 — Diagramas UML

# 7. Elige un mini-proyecto (ejemplo: biblioteca, gestión de cursos o tienda online) y responde:

# ¿Qué clases identificas en el problema? // - Se hace

# ¿Qué atributos y métodos tendría cada clase? // - Se hace

# ¿Qué relaciones existen entre ellas? // - Se hace 

# 8. Realiza un diagrama de clases para el problema elegido. // - Aun no ya que no lo hemos visto detalladamente

# 9. Crea un diagrama de objetos con instancias concretas de tus clases. // - Aun no ya que no lo hemos visto detalladamente

# 10. Dibuja un diagrama de secuencia que muestre cómo interactúan los objetos en un caso de uso (ej.: inscribir estudiante, prestar libro, hacer compra). // - Aun no ya que no lo hemos visto detalladamente

# 11. Dibuja un diagrama de actividad con el flujo de pasos del caso de uso elegido. // - Aun no ya que no lo hemos visto detalladamente

# Por ahora se hacen mini proyectos de POO,como;


# Simulador de inventario;



class Inventario:
    def __init__(self, producto, precio, fecha_de_compra, fecha_de_vencimiento, fecha_de_produccion, comprador):
        self.producto = producto
        self.precio = precio
        self.fecha_de_compra = fecha_de_compra
        self.fecha_de_vencimiento = fecha_de_vencimiento
        self.fecha_de_produccion = fecha_de_produccion
        self.comprador = comprador

    def mostrar_info(self):
        print("Nombre del producto: ", self.producto)
        print("Precio: ", self.precio)
        print("Fecha de compra: ", self.fecha_de_compra)
        print("Fecha de vencimiento: ", self.fecha_de_vencimiento)
        print("Fecha de producción: ", self.fecha_de_produccion)
        print("Nombre del comprador: ", self.comprador)


comprador1 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador2 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador3 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador4 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador5 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador6 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador7 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador8 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador9 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))
comprador10 = Inventario(input("Ingresa el producto: "), input("Ingresa el precio: "), input("Ingresa la fecha de compra: "), input("Ingresa la fecha de vencimiento: "), input("Ingresa la fecha de producción: "), input("Ingresa el comprador: "))

comprador1.mostrar_info()
comprador2.mostrar_info()
comprador3.mostrar_info()
comprador4.mostrar_info()
comprador5.mostrar_info()
comprador6.mostrar_info()
comprador7.mostrar_info()
comprador8.mostrar_info()
comprador9.mostrar_info()
comprador10.mostrar_info()



# ¿Qué clases identificas en el problema? 
print("La clase inventario que permite imprimir mediante un metodo mostrar la informacion de los productos ingresados y comprados por los 10 compradores")

# ¿Qué atributos y métodos tendría cada clase? 
print("""La unica y principal clase tendria;
      ------------- ATRIBUTOS: ----------------
       - producto; Que es el nombre del producto
       - precio; Su precio
       - fecha_de_compra; La fecha en el que el comprador la compro
       - fecha_de_vencimiento; La fecha en que el producto o se vence o empieza a por asi decirlo degradarse
       - fecha_de_produccion; La fecha en que cierta empresa fabricante fabrico el producto especifico que se va comprar
       - comprador; Nombre del comprador
      ------------- METOODOS: -----------------
       - mostrar_info(): permite mostrar todos los atributos de manera clara y concisa del inventario para un producto""")

# ¿Qué relaciones existen entre ellas? 
print("No hay relaciones entre clases porque solo hay una clase (Inventario) en todo el programa. Para que haya relaciones, debe haber al menos dos o más clases que interactúen entre sí.")









# Calculadora basica

class Calculadora:
    def __init__(self,numero_uno,numero_dos):
        self.numero_uno = numero_uno
        self.numero_dos = numero_dos
    def sumar(self):
        print(f"{self.numero_uno} + {self.numero_dos} = {self.numero_uno+self.numero_dos}")
    def restar(self):
        print(f"{self.numero_uno} - {self.numero_dos} = {self.numero_uno-self.numero_dos}")
    def multiplicacion(self):
        print(f"{self.numero_uno} * {self.numero_dos} = {self.numero_uno*self.numero_dos}")
    def division(self):
        print(f"{self.numero_uno} / {self.numero_dos} = {self.numero_uno/self.numero_dos}")


persona1 = Calculadora(int(input("Ingresa el primer numero: ")),int(input("Ingresa el segundo numero: ")))
persona2 = Calculadora(int(input("Ingresa el primer numero: ")),int(input("Ingresa el segundo numero: ")))
opcion = input("""Que opcion quieres hacer?
               1. SUMA
               2. RESTA
               3. MULTIPLICACION
               4. DIVISION
               : """)
if opcion == "1":
    persona1.sumar()
elif opcion == "2":
    persona1.restar()
elif opcion == "3":
    persona1.multiplicacion()
elif opcion == "4":
    persona1.division()
else:
    print("No se puede hacer ninguna operacion con ese numero...")


opcion2 = input("""Que opcion quieres hacer?
               1. SUMA
               2. RESTA
               3. MULTIPLICACION
               4. DIVISION
               : """)

if opcion2 == "1":
    persona2.sumar()
elif opcion2 == "2":
    persona2.restar()
elif opcion2 == "3":
    persona2.multiplicacion()
elif opcion2 == "4":
    persona2.division()
else:
    print("No se puede hacer ninguna operacion con ese numero...")


# ¿Qué clases identificas en el problema? 
print("La clase calculadora que es la base para que el usuario pueda realizar accciones como sumar restar etc")

# ¿Qué atributos y métodos tendría cada clase? 
print("""La unica y principal clase tendria;
      ------------- ATRIBUTOS: ----------------
       - numero_uno; Numero uno que el usuario ingresa
       - numero_dos; Numero dos que el usuario ingresa
      ------------- METOODOS: -----------------
       - sumar(); Permite sumar los dos numeros
      - restar(); Permite restar los dos numeros
      - multiplicacion(); Permite multiplicar los numeros
      - dvision(); Permite dividir los numeros""")

# ¿Qué relaciones existen entre ellas? 
print("Ninguna como la anterior,ya que no hay mas de una clase por lo tanto no se relacionan...")










# Gestor de productos

class Productos:
    def __init__(self,nombre,precio,marca,fechaenquesehizo,fechaenquesevence):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.fechaenquesehizo = fechaenquesehizo
        self.fechaenquesevence = fechaenquesevence
    def comprar(self):
        print(f"""Que buena eleccion de producto para comprar!!;
            nombre: {self.nombre},
            precio: {self.precio},
            marca: {self.marca},
            fecha en que se hizo: {self.fechaenquesehizo},
            fecha en que se vence: {self.fechaenquesevence}""")
    def registrar(self):
        print(f"""Que buena eleccion de producto!! para el registro;
            nombre: {self.nombre},
            precio: {self.precio},
            marca: {self.marca},
            fecha en que se hizo: {self.fechaenquesehizo},
            fecha en que se vence: {self.fechaenquesevence}""")
                
    def vender(self):
        print(f"""Que buena eleccion de producto!! para vender;
            nombre: {self.nombre},
            precio: {self.precio},
            marca: {self.marca},
            fecha en que se hizo: {self.fechaenquesehizo},
            fecha en que se vence: {self.fechaenquesevence}""")

cliente1 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))
cliente2 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))
cliente3 = Productos(input("Que producto vas a ingresar: "),input("Ingresa su precio: "),input("Ingresa su marca: "),input("Ingresa su fecha en que se hizo: "),input("Ingresa la fecha en que se vence: "))

opcion1 = input("""Ingresa una opcion:
                1. COMPRAR
                2. REGISTRAR PARA LA TIENDA
                3. VENDER
                : """)
if opcion1 == "1":
    cliente1.comprar()
elif opcion1 == "2":
    cliente1.registrar()
elif opcion1 == "3":
    cliente1.vender()
else:
    print("Esa opcion no existe para la gestion de nuestros productos")


opcion22 = input("""Ingresa una opcion:
                1. COMPRAR
                2. REGISTRAR PARA LA TIENDA
                3. VENDER
                : """)

if opcion22 == "1":
    cliente2.comprar()
elif opcion22 == "2":
    cliente2.registrar()
elif opcion22 == "3":
    cliente2.vender()
else:
    print("Esa opcion no existe para la gestion de nuestros productos")


opcion3 = input("""Ingresa una opcion:
                1. COMPRAR
                2. REGISTRAR PARA LA TIENDA
                3. VENDER
                : """)
if opcion3 == "1":
    cliente3.comprar()
elif opcion3 == "2":
    cliente3.registrar()
elif opcion3 == "3":
    cliente3.vender()
else:
    print("Esa opcion no existe para la gestion de nuestros productos")



# ¿Qué clases identificas en el problema? 
print("La clase Productos, que representa un producto con su información (nombre, precio, marca, fechas) y permite gestionarlo mediante métodos como comprar, registrar o vender.")

# ¿Qué atributos y métodos tendría cada clase? 
print("""La unica y principal clase tendria;
      ------------- ATRIBUTOS: ----------------
      - nombre: nombre del producto
      - precio: precio del producto
      - marca: marca del producto
      - fechaenquesehizo: cuándo fue producido
      - fechaenquesevence: cuándo vence
      ------------- METODOS: -----------------
      - comprar(): imprime los datos del producto cuando se va a comprar
      - registrar(): imprime los datos al registrar el producto en la tienda
      - vender(): imprime los datos al vender el producto""")

# ¿Qué relaciones existen entre ellas? 
print("No hay relaciones entre clases, ya que el programa solo define una clase (Productos). Todos los objetos (cliente1, cliente2) son instancias de esa misma clase.")







# Gestor de productos con herencia y polimorfismo

class Productos:
    def __init__(self, nombre, precio, marca, fechaenquesehizo, fechaenquesevence):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.fechaenquesehizo = fechaenquesehizo
        self.fechaenquesevence = fechaenquesevence

    def comprar(self):
        print(f"""
Que buena elección de producto para comprar!!
Nombre: {self.nombre}
Precio: {self.precio}
Marca: {self.marca}
Fecha en que se hizo: {self.fechaenquesehizo}
Fecha en que se vence: {self.fechaenquesevence}
        """)

    def registrar(self):
        print(f"""
Producto registrado correctamente:
Nombre: {self.nombre}
Precio: {self.precio}
Marca: {self.marca}
Fecha en que se hizo: {self.fechaenquesehizo}
Fecha en que se vence: {self.fechaenquesevence}
        """)

    def vender(self):
        print(f"""
Producto vendido:
Nombre: {self.nombre}
Precio: {self.precio}
Marca: {self.marca}
Fecha en que se hizo: {self.fechaenquesehizo}
Fecha en que se vence: {self.fechaenquesevence}
        """)


#  Clase hija que hereda de Productos
class ProductoAlimenticio(Productos):
    def __init__(self, nombre, precio, marca, fechaenquesehizo, fechaenquesevence, calorias):
        # Heredamos atributos del padre
        super().__init__(nombre, precio, marca, fechaenquesehizo, fechaenquesevence) # Super permite reutilizar el código de la clase padre sin volver a escribirlo.
        self.calorias = calorias  # Atributo nuevo de la clase hija

    # Polimorfismo: redefinimos el método comprar()
    def comprar(self):
        print(f"""
Has comprado un producto alimenticio:
Nombre: {self.nombre}
Precio: {self.precio}
Marca: {self.marca}
Calorías: {self.calorias}
Fecha de fabricación: {self.fechaenquesehizo}
Fecha de vencimiento: {self.fechaenquesevence}
        """)


# --- Ejemplos de instancias ---
cliente1 = Productos("Perfume", "45000", "Aromax", "10/09/2025", "10/09/2030")
cliente2 = ProductoAlimenticio("Yogurt", "2500", "Alpina", "20/10/2025", "27/10/2025", "120 kcal")
cliente3 = Productos("Iphone", "14.500.000","Apple","10/08/2024","10/08/2030")
cliente4 = ProductoAlimenticio("Leche","15.000","Alqueria","10/09/2005","10/06/2025","120 kcal")

# --- Ejemplo de polimorfismo --- 
# Cada cliente actua de diferente forma dependiendo del producto que compro; Si es alimenticio o si es un producto electronico
cliente1.comprar()
cliente2.comprar()
cliente3.comprar()
cliente4.comprar()








# Gestor de notas

class Notas:
  def __init__(self,nombre_completo,colegio,nota_uno,nota_dos,nota_tres):
        self.nombre_completo = nombre_completo
        self.colegio = colegio
        self.nota_uno = nota_uno
        self.nota_dos = nota_dos
        self.nota_tres = nota_tres
        self.promedio = (self.nota_uno+self.nota_dos+self.nota_tres) / 3

  def perder(self):
        print("Has perdido tienes un promedio menor de 3.0")
 
  def ganar(self):
        print("Has ganado,tu promedio es mayor a 3")

est1 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))
est2 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))
est3 = Notas(input("Ingresa tu nombre completo: "),input("Ingresa el nombre de tu colegio: "),float(input("Ingresa la nota uno: ")),float(input("Ingresa la nota dos: ")),float(input("Ingresa la nota tres: ")))


if est1.promedio >= 3.0:
    est1.ganar()
else:
    est1.perder()

if est2.promedio >= 3.0:
    est2.ganar()
else:
    est2.perder()

if est3.promedio >= 3.0:
    est3.ganar()
else:
    est3.perder()


# ¿Qué clases identificas en el problema? 
print("""En este programa se identifica una única clase, llamada Notas.
       Esta clase representa a un estudiante con sus notas y calcula su promedio para saber si gana o pierde el año o la materia.""")
    
# ¿Qué atributos y métodos tendría cada clase? 
print("""La unica y principal clase tendria;
      ------------- ATRIBUTOS: ----------------
      - nombre_completo: nombre del estudiante
      - colegio: nombre del colegio
      - nota_uno, nota_dos, nota_tres: las tres calificaciones
      - promedio: el promedio de las tres notas (calculado automáticamente)
      ------------- METOODOS: -----------------
      - ganar(): muestra un mensaje si el promedio es mayor o igual a 3.0
      - perder(): muestra un mensaje si el promedio es menor a 3.0""")

# ¿Qué relaciones existen entre ellas? 
print("""En este programa no hay relaciones entre clases, ya que solo existe una clase (Notas).
Todos los estudiantes (est1, est2, est3) son instancias (objetos) de la misma clase, pero no hay otra clase que se relacione con ella """)







