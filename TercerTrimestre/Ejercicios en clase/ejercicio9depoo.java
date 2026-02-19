//  EJERCICIO 9: Crea una clase 'Producto' con precio y cantidad,y un metodo para calcular el valor total del inventario

class Producto {

    // ----- Atributos -----
    private String nombre;   // Nombre del producto
    private double precio;   // Precio unitario
    private int cantidad;    // Cantidad en inventario

    // ----- Constructor -----
    // Inicializa los valores del producto
    public Producto(String nombre, double precio, int cantidad) {
        this.nombre = nombre;
        this.precio = precio;
        this.cantidad = cantidad;
    }

    // ----- Método para calcular el valor total -----
    public void mostrarInformacion() {
        double total = precio * cantidad;  // Calcula total
        System.out.println("Producto: " + nombre);
        System.out.println("Precio unitario: $" + precio);
        System.out.println("Cantidad disponible: " + cantidad);
        System.out.println("Valor total del inventario: $" + total);
        System.out.println("---------------------------------------");
    }
}

public class ejercicio9depoo {
    public static void main(String[] args) {
        System.out.println(" EJERCICIO 9: PRODUCTO ");
        Producto p1 = new Producto("Laptop", 2500.0, 3);
        Producto p2 = new Producto("Teléfono", 1200.5, 5);
        Producto p3 = new Producto("Mouse", 80.75, 10);

        p1.mostrarInformacion();
        p2.mostrarInformacion();
        p3.mostrarInformacion();
    }
}