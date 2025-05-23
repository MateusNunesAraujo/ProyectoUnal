document.querySelectorAll(".info-hotel").forEach(e => {

    e.addEventListener("click", (e)=>{
        window.location.href = "/info_hoteles/" + e.target.getAttribute("id_hotel") + "/"
    })

})