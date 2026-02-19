//  EJERCICIO 10: Diseña una clase 'Animal' con un metodo hablar() que se sobreescriba en clases hijas como 'Perro' y 'Gato'


//  Clase base "Animal"
// Esta clase representa cualquier tipo de animal genérico.
// Las clases hijas heredarán sus atributos y redefinirán el método hablar().
class Animal {

    protected String nombre;  // Nombre del animal
    protected String genero;  // Género (macho o hembra)
    protected int edad;       // Edad en años

    // Constructor: inicializa los atributos comunes a todos los animales
    public Animal(String nombre, String genero, int edad) {
        this.nombre = nombre;
        this.genero = genero;
        this.edad = edad;
    }

    // Método que será sobrescrito por las clases hijas
    public void hablar() {
        System.out.println(nombre + " hace un sonido genérico.");
    }

    // Muestra los datos generales del animal
    public void mostrarInfo() {
        System.out.println("Nombre: " + nombre + " | Género: " + genero + " | Edad: " + edad + " años");
    }
}


//  Clase hija: Gato
// Sobrescribe el método hablar() para emitir el sonido propio de un gato.
class Gato extends Animal {
    public Gato(String nombre, String genero, int edad) {
        super(nombre, genero, edad); // Llama al constructor de la superclase Animal
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Miau!");
    }
}


//  Clase hija: Perro
class Perro extends Animal {
    public Perro(String nombre, String genero, int edad) {
        super(nombre, genero, edad);
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Guau!");
    }
}


//  Clase hija: Vaca
class Vaca extends Animal {
    public Vaca(String nombre, String genero, int edad) {
        super(nombre, genero, edad);
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Muuu!");
    }
}


//  Clase hija: Pollito
class Pollito extends Animal {
    public Pollito(String nombre, String genero, int edad) {
        super(nombre, genero, edad);
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Pío Pío!");
    }
}


//  Clase hija: Gallo
class Gallo extends Animal {
    public Gallo(String nombre, String genero, int edad) {
        super(nombre, genero, edad);
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Kikirikí!");
    }
}


//  Clase hija: Oveja
class Oveja extends Animal {
    public Oveja(String nombre, String genero, int edad) {
        super(nombre, genero, edad);
    }

    @Override
    public void hablar() {
        System.out.println(nombre + " dice: ¡Beee!");
    }
}

public class ejercicio10poo{
    public static void main(String[] args) {



        System.out.println(" EJERCICIO 10: ANIMALES ");

        // Se crean varios animales con valores definidos
        Gato gato = new Gato("Michi", "Hembra", 2);
        Perro perro = new Perro("Rocky", "Macho", 4);
        Vaca vaca = new Vaca("Lola", "Hembra", 5);
        Pollito pollito = new Pollito("Pepe", "Macho", 1);
        Gallo gallo = new Gallo("Claudio", "Macho", 3);
        Oveja oveja = new Oveja("Nube", "Hembra", 2);

        // Se muestran sus datos y su sonido característico
        gato.mostrarInfo(); gato.hablar();
        perro.mostrarInfo(); perro.hablar();
        vaca.mostrarInfo(); vaca.hablar();
        pollito.mostrarInfo(); pollito.hablar();
        gallo.mostrarInfo(); gallo.hablar();
        oveja.mostrarInfo(); oveja.hablar();
    }
} 
