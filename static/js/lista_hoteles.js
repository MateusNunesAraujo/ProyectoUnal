console.log("Hola pequitas")
document.querySelector(".cssbuttons-io-button").addEventListener("click", () => {
    console.log("creando")
    window.location.href = "/create_hotel"
})

document.querySelector("#close").addEventListener("click", () => {
    document.querySelector(".modal-oculto").classList.remove('modal-activado')
    document.querySelector(".main-activado").classList.remove('main-activado')
})

/* Mostrar datos del hotel */
document.querySelectorAll(".btn-informacion").forEach(e => {
    e.addEventListener("click", () => {
        fetch("/mostrar_hotel/", {
            method: "POST",
            body: JSON.stringify({ "id": e.getAttribute("id-hotel") }),
            headers: {
                "X-CSRFToken": document.querySelector('input[name = "csrfmiddlewaretoken"]').value, // Asegúrate de incluir el token CSRF
            },
        }).then(response => response.json())
            .then((data) => {
                template = ''
                estrellas = ''
                document.querySelector('.main-oculto header h1').textContent = "Hotel " + data.nombre
                document.querySelector('#precio_noche').textContent = "Precio por noche: " + data.precio_noche + "$"
                document.querySelector('.informacion-1').innerHTML = `<p>${data.descripcion}</p>`
                console.log(data.estrellas)
                for (let i = 1; i <= data.estrellas; i++) {
                    estrellas += `<img class="img-estrellas" src="/static/img/iconos/estrella.png" alt="">`
                }
                document.querySelector('.cont-estrellas').innerHTML = estrellas
                document.querySelector('#ubicacion').textContent = "Ubicación: " + data.ubicacion
                document.querySelector('#resenas').textContent = "Reseñas: " + data.resenas
                document.querySelector('#habitaciones').textContent = "Habitaciones: " + data.habitaciones
                document.querySelector('#habitaciones_libres').textContent = "Habitaciones libres: " + data.habitaciones_libres
                data.img_urls.forEach(element => {
                    template += `<img class="img-hoteles" src="${element}" alt="">`
                });
                document.querySelector(".cont-imgs").innerHTML = template


            })
        document.querySelector(".modal-oculto").classList.add('modal-activado')
        document.querySelector(".modal-activado main").classList.add('main-activado')
    }
    )
})

document.querySelectorAll(".btn-actualizar").forEach(e => {
        e.addEventListener("click", () => {
            window.location.href = "/update_hotel/" + e.getAttribute("id-hotel") + "/";
        });
})

document.querySelectorAll(".btn-eliminar").forEach(e => {
        e.addEventListener("click", () => {
            window.location.href = "/delete_hotel/" + e.getAttribute("id-hotel") + "/";
        });
})