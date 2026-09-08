<?php
// Ejercicio 1: Contador regresivo de 10 a 1

$numero = 10;

while ($numero >= 1) {
    echo $numero . " ";
    $numero--; // Decrementamos para no ciclar infinitamente
}
?>


<?php
// Ejercicio 2: Sumar números hasta que la suma alcance o supere 50

$suma = 0;
$numero = 1;

while ($suma < 50) {
    $suma += $numero;
    $numero++;
}

echo "La suma llegó a: " . $suma;
echo "\nSe sumaron " . ($numero - 1) . " números";
?>

<?php
// Ejercicio 3: Leer números hasta que se ingrese un negativo
$numero = 0; // Valor inicial positivo para entrar al bucle

while ($numero >= 0) {
    $numero = (int) readline("Ingresa un número: ");

    if ($numero >= 0) {
        echo "Número válido: " . $numero . "\n";
    }
}

echo "Ingresaste un negativo. Fin del programa.";
?>


<?php
// Ejercicio 4: Contar cuántos números se ingresan hasta introducir un 0
$contador = 0;
$numero   = -1; // Valor inicial para entrar al bucle

while ($numero != 0) {
    $numero = (int) readline("Número (0 para salir): ");

    if ($numero != 0) {
        $contador++; // Contamos cada número válido
    }
}

echo "Ingresaste " . $contador . " número(s)";
?>


<?php
// Ejercicio 5: Mostrar múltiplos de 4 hasta 100 usando while

$numero = 4; // Empezamos desde el primer múltiplo

while ($numero <= 100) {
    echo $numero . " ";
    $numero += 4; // Saltamos de 4 en 4
}
?>