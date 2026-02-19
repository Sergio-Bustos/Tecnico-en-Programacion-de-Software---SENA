# Ejercicios de POO individuales de manera autonoma en clases acronicas


# Ejemplo de ABSTRACCIÓN en Programación Orientada a Objetos (POO)
# Clase Auto con estados "apagado" y "encendido".
# Se muestran solo métodos simples (encender, conducir).


class Auto:
    def __init__(self):
        # Al crear un auto, inicia apagado
        self._estado = "apagado"
        print("El auto esta apagado por ahora")

    def encender(self):
        # Cambiamos el estado y mostramos mensaje
        self._estado = "encendido"
        print("El auto está encendido ahora")

    def conducir(self):
        # Verificamos si el auto está apagado o encendido
        if self._estado == "apagado":
            print("No puedes conducir, el auto está apagado")
        else:
            print("Conduciendo el auto")


# ------------------- PROGRAMA PRINCIPAL -------------------

mi_auto = Auto()          # Crear auto
mi_auto.conducir()        # Intentar conducir apagado
mi_auto.encender()        # Encender auto
mi_auto.conducir()        # Conducir encendido




# Ejemplo clasico: Perro ladrando

class Perro:
    def __init__(self,nombre,raza,edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        
    def ladrar(self):
        print(f"{self.nombre} estas ladrando,por que ladras tanto!!!")
    def caminar_lento(self):
        print(f"{self.nombre} ya estas vieja y estas caminando lento con esos {self.edad} años")

perro1 = Perro("Sussy","Beagle","15 años")
perro2 = Perro("Lolita","Pastor aleman","4")

perro1.ladrar()
perro2.caminar_lento()



# Otro ejemplo clasico: Gestion de notas
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
    

