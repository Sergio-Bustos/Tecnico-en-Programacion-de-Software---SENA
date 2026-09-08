
<?php
// Ejercicio 1: Calcular perímetro de un rectángulo
// Definimos las medidas del rectángulo
$base   = 10;
$altura = 5;

// Calculamos el perímetro con la fórmula
$perimetro = 2 * ($base + $altura);

echo "El perímetro es: " . $perimetro;

?>


<?php
// Ejercicio 2: Calcular promedio de cuatro números
// Los cuatro números a promediar
$n1 = 10;
$n2 = 20;
$n3 = 30;
$n4 = 40;

// Sumamos y dividimos entre la cantidad de números
$promedio = ($n1 + $n2 + $n3 + $n4) / 4;

echo "El promedio es: " . $promedio;
?>


<?php
// Ejercicio 3: Convertir kilómetros a metros
// Distancia en kilómetros
$kilometros = 5;

// Multiplicamos por 1000 para obtener metros
$metros = $kilometros * 1000;

echo $kilometros . " km equivalen a " . $metros . " metros";
?>
<?php
// Ejercicio 4: Calcular IVA (19%) y total a pagar
// Precio base del producto
$precio = 50000;

// Calculamos el valor del IVA (19%)
$iva = $precio * 0.19;

// Precio total con IVA incluido
$total = $precio + $iva;

echo "Precio sin IVA: $" . $precio . "\n";
echo "IVA (19%): $"    . $iva    . "\n";
echo "Total a pagar: $" . $total;
?>
echo "IVA (19%): $"    . $iva    . "
";
echo "Total a pagar: $" . $total;
?>

<?php
// Ejercicio 5: Elevar un número a la cuarta potencia
// Número que queremos elevar
$numero = 3;

// Elevamos a la cuarta potencia
$resultado = $numero ** 4;

echo $numero . " elevado a la 4 es: " . $resultado;
?>