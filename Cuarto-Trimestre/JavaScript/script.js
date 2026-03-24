function cambiarTexto () { 
    document.getElementById("texto").innerText = "Suspiro, vista, soy alto, ordenado, medio a qué. Enviado tarde, retenido, que establecido, por qué, esposa nuestra. Si una bendición, construyendo más empinado. Acuerdo desconfía, señora seis, afecto satisfecho. Día se sonroja, visitante, fin, compañía, viejo, prevenir capítulo. Considere declarado, gastos, sus preocupaciones. No en indulgencia, convicción, particular, insaciable, bullicioso, discreción. Directo, suficiente, otros dicen, mayor, puede, Exeter, ella. Posiblemente, todo ignorante, suministrado, conseguir, asentar, matrimonio, recurrió.";
}



function cambiarColor() {

    document.body.style.backgroundColor = "grey";

}

function cambiarImagen () {
    document.getElementById("foto").src = "https://cdn.prod.website-files.com/65ae46959867d80cb5186dcb/6666d283da34cb0248127062_BL014.jpg";
}

function ocultarImagen () {
    document.getElementById("foto").style.display = "none";
}


function agregarBoton () {
    const botonNuevo = document.createElement("button") 
    botonNuevo.innerText = "Nuevo boton"
    document.querySelector(".botonesconjs").appendChild(botonNuevo)
   
}

function modoOscuro () {
    document.body.style.backgroundColor = "black";
    document.getElementById("texto").style.color = "white";
    document.getElementsByTagName("h1")[0].style.color = "white";
    document.getElementsByClassName("h2")[0].style.color = "white";

}