const btnLike = document.querySelector(".Btn");
const contadorLike = document.querySelector(".likeCount");

btnLike.addEventListener("click", e => {
    // Busca el contenedor con el atributo id-evento, desde el elemento clickeado hacia arriba
    const leftContainer = e.target.closest(".leftContainer");
    if (!leftContainer) return; // Solo ejecuta si se hace click en la parte izquierda

    fetch("/like/", {
        method: "POST",
        body: JSON.stringify({ "id": leftContainer.getAttribute("id-evento") }),
        headers: {
            "X-CSRFToken": document.querySelector('input[name="csrfmiddlewaretoken"]').value,
        },
    })
        .then(response => response.json())
        .then(data => {
            if(data.error == "Error"){
                //Eliminar like
                 contadorLike.textContent = data.total_like;
            }else{
                //Agregar like
                contadorLike.textContent = data.total_like;
            }
           
        });
});
document.querySelectorAll(".salir").forEach(e => {
    e.addEventListener("click", e => {
        window.location.href = "/eventos/"
    })

})