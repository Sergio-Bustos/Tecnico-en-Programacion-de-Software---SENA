
<?php
// Ejercicio 1: Comprobar si un número es múltiplo de 2
$numero = 8;

// El operador % calcula el residuo de la división
if ($numero % 2 == 0) {
    echo $numero . " sí es múltiplo de 2";
} else {
    echo $numero . " NO es múltiplo de 2";
}
?>


<?php
// Ejercicio 2: Comprobar si un número es mayor que 100
$numero = 75;

if ($numero > 100) {
    echo $numero . " es mayor que 100";
} else {
    echo $numero . " NO es mayor que 100";
}
?>


<?php
// Ejercicio 3: Comprobar si una persona puede votar
$edad = 17;

if ($edad >= 18) {
    echo "Sí puede votar";
} else {
    // Calculamos cuántos años le faltan
    $falta = 18 - $edad;
    echo "No puede votar. Le faltan " . $falta . " año(s)";
}

?>

<?php
// Ejercicio 4: Determinar el menor entre tres números
$a = 15;
$b = 8;
$c = 22;

// Comparamos los tres valores entre sí
if ($a <= $b && $a <= $c) {
    echo "El menor es: " . $a;
} elseif ($b <= $a && $b <= $c) {
    echo "El menor es: " . $b;
} else {
    echo "El menor es: " . $c;
}

?>


<?php
// Ejercicio 5: Comprobar si un número es divisible entre 4
$numero = 16;

// Si el residuo de dividir entre 4 es 0, es divisible
if ($numero % 4 == 0) {
    echo $numero . " es divisible entre 4";
} else {
    echo $numero . " NO es divisible entre 4";
}
?>