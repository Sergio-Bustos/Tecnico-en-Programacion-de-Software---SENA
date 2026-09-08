<?php
// Ejercicio 1: Mostrar múltiplos de 5 del 5 al 50
for ($i = 5; $i <= 50; $i += 5) {
    echo $i . " ";
}
?>
<?php
// Ejercicio 2: Tabla de multiplicar del 5
$numero = 5;

for ($i = 1; $i <= 10; $i++) {
    $resultado = $numero * $i;
    echo $numero . " x " . $i . " = " . $resultado . "\n";
}
?>
<?php
// Ejercicio 3: Sumar los números pares del 1 al 50
$suma = 0; // Acumulador empieza en 0

for ($i = 1; $i <= 50; $i++) {
    // Solo sumamos si el número es par
    if ($i % 2 == 0) {
        $suma += $i;
    }
}

echo "Suma de pares del 1 al 50: " . $suma;
?>
<?php
// Ejercicio 4: Mostrar los cuadrados del 1 al 10
for ($i = 1; $i <= 10; $i++) {
    $cuadrado = $i ** 2; // ** es el operador potencia
    echo $i . "² = " . $cuadrado . "\n";
}
?>
<?php
// Ejercicio 5: Contar múltiplos de 3 entre 1 y 100
$contador = 0; // Contador inicia en 0

for ($i = 1; $i <= 100; $i++) {
    if ($i % 3 == 0) {
        $contador++; // Sumamos 1 al contador
    }
}

echo "Hay " . $contador . " múltiplos de 3 entre 1 y 100";
?>
<?php

for ($i = 5; $i <= 50; $i += 5) {
    echo $i . " ";
}
?>


<?php
$numero = 5;

for ($i = 1; $i <= 10; $i++) {
    $resultado = $numero * $i;
    echo $numero . " x " . $i . " = " . $resultado . "
";
}
?>


<?php
$suma = 0; // Acumulador empieza en 0

for ($i = 1; $i <= 50; $i++) {
    // Solo sumamos si el número es par
    if ($i % 2 == 0) {
        $suma += $i;
    }
}

echo "Suma de pares del 1 al 50: " . $suma;
?>




<?php

for ($i = 1; $i <= 10; $i++) {
    $cuadrado = $i ** 2; // ** es el operador potencia
    echo $i . "² = " . $cuadrado . "
";
}
?>



<?php
$contador = 0; // Contador inicia en 0

for ($i = 1; $i <= 100; $i++) {
    if ($i % 3 == 0) {
        $contador++; // Sumamos 1 al contador
    }
}

echo "Hay " . $contador . " múltiplos de 3 entre 1 y 100";
?>