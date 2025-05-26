let info = { "estrella": "todos", "precio_rango": "todos" }

function filtrar(informacion) {
    console.log(informacion)
    fetch('/filtrar/', {
        method: 'POST',
        body: JSON.stringify(informacion),
        headers: {
            "X-CSRFToken": document.querySelector('input[name = "csrfmiddlewaretoken"]').value, // Asegúrate de incluir el token CSRF
        },
    }).then(response => response.json())
        .then(data => {
            let template = ''
            console.log(data)
            data["informacion"].forEach(element => {
                let estrellas = '';
                for (let i = 0; i < element.estrellas; i++) {
                    estrellas += `<img class="estrella" src="/static/img/iconos/estrella.png" alt="Estrella">`;
                }
                // Estrellas vacías (hasta 5)
                for (let i = element.estrellas; i < 5; i++) {
                    estrellas += `<img class="estrella" src="/static/img/iconos/estrella_vacia.png" alt="Estrella vacía">`;
                }
                template += `<div class="card-hotel">
                <div class="container-informacion">
                    <div class="titulo">
                        <h2>${element.nombre}</h2>
                           <div class="container-estrellas">${estrellas}</div>
                    </div>
                    <div class="informacion_rapida">
                        <p class="habitaciones">${element.habitaciones_libres} habitaciones disponibles </p>
                        <p class="precio"> Desde ${element.precio_noche} COP por noche </p>
                        <p class="valoracion">⭐ ${element.estrellas}/5 (${element.resenas} reseñas)</p>
                    </div>

                </div>
                <div class="container-img">
                    <img class="img-hotel" src="${element['img_urls'][0]}" alt="">
                </div>
                <div class="informacion">
                    <div class="informacion_secundaria"><img class="iconos" src="/static/img/iconos/mensaje-destacado.png" alt=""><img class="iconos" src="/static/img/iconos/igual-que.png" alt=""></div>
                    <button class="info-hotel" id_hotel="${element.id}">Ver más</button>
                </div>
            </div>`
            });

            if (template == "") {
                document.querySelector('.container-hotel').innerHTML = `<div class='sin-resultado'><h1>Sin resultados</h1><img src="/static/img/img/loro_triste.png" alt=""></div>`
            } else {
                document.querySelector('.container-hotel').innerHTML = template
                document.querySelectorAll(".info-hotel").forEach(e => {

                    e.addEventListener("click", (e) => {
                        window.location.href = "/info_hoteles/" + e.target.getAttribute("id_hotel") + "/"
                    })

                })
            }

        })

}




document.querySelectorAll(".info-hotel").forEach(e => {
    e.addEventListener("click", (e) => {
        window.location.href = "/info_hoteles/" + e.target.getAttribute("id_hotel") + "/"
    })
})

console.log("hola")
document.querySelector(".buscador_hotel").addEventListener("click", (e) => {
    let valor = e.target.previousElementSibling.value
    window.location.href = "/buscar_hotel/" + valor
})

document.querySelectorAll(".filtros-estrellas button").forEach(e => {
    e.addEventListener("click", (e) => {
        let estrellas_activado = document.querySelectorAll(".filtros-estrellas-activado")
        estrellas_activado.forEach((e) => {
            e.classList.remove('filtros-estrellas-activado')
        })
        if (e.target.classList.contains('filtros-estrellas-activado')) {
            e.target.classList.remove('filtros-estrellas-activado')
        } else {
            e.target.classList.add('filtros-estrellas-activado')
            console.log()
            info["estrella"] = e.target.getAttribute('data-estrella')
            filtrar(info)
        }
    })
})

document.querySelectorAll(".filtros-precios button").forEach(e => {
    e.addEventListener("click", (e) => {
        let precios_activado = document.querySelectorAll(".filtros-precios-activado")
        precios_activado.forEach((e) => {
            e.classList.remove('filtros-precios-activado')
        })
        if (e.target.classList.contains('filtros-precios-activado')) {
            e.target.classList.remove('filtros-precios-activado')
        } else {
            e.target.classList.add('filtros-precios-activado')
            info["precio_rango"] = e.target.getAttribute('data-rango')
            filtrar(info)
        }
    })
})

