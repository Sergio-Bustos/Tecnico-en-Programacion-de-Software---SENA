//  EJERCICIO 13: Diseña una clase ConversorTemperatura que convierta de Celsius a Fahrenheit y viceversa


//  Clase base para conversión
// Representa un conversor genérico que se especializa en clases hijas.
class ConversorTemperatura {

    protected String nombre;   // Escala (Celsius o Fahrenheit)
    protected double cantidad; // Valor numérico a convertir

    public ConversorTemperatura(String nombre, double cantidad) {
        this.nombre = nombre;
        this.cantidad = cantidad;
    }

    // Método que será sobrescrito por las clases hijas
    public void convertir() {}
}


//  Fahrenheit → Celsius
class PasarF_a_C extends ConversorTemperatura {

    public PasarF_a_C(String nombre, double cantidad) {
        super(nombre, cantidad);
    }

    @Override
    public void convertir() {
        double resultado = (cantidad - 32) / 1.8;
        System.out.println(cantidad + "° " + nombre + " equivalen a " + resultado + "° Celsius.");
    }
}


//  Celsius → Fahrenheit
class PasarC_a_F extends ConversorTemperatura {

    public PasarC_a_F(String nombre, double cantidad) {
        super(nombre, cantidad);
    }

    @Override
    public void convertir() {
        double resultado = (cantidad * 1.8) + 32;
        System.out.println(cantidad + "° " + nombre + " equivalen a " + resultado + "° Fahrenheit.");
    }
}

public class ejercicio13poo {
    public static void main(String[] args) {
        System.out.println(" EJERCICIO 13: CONVERSOR DE TEMPERATURA ");

        PasarF_a_C conversion1 = new PasarF_a_C("Fahrenheit", 212);
        PasarC_a_F conversion2 = new PasarC_a_F("Celsius", 100);
        PasarF_a_C conversion3 = new PasarF_a_C("Fahrenheit", 50);
        PasarC_a_F conversion4 = new PasarC_a_F("Celsius", 0);

        conversion1.convertir();
        conversion2.convertir();
        conversion3.convertir();
        conversion4.convertir();
    }
}






