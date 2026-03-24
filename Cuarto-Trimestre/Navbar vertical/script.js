const modal = document.getElementById("modal");
const abrir = document.getElementById("abrirModal");
const cerrar = document.getElementById("cerrarModal");

abrir.addEventListener("click", () => {
    modal.style.display = "flex";
});

cerrar.addEventListener("click", () => {
    modal.style.display = "none";
});

window.addEventListener("click", (e) => {
    if (e.target === modal) {
        modal.style.display = "none";
    }
});