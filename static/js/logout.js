document.querySelector("#logout").addEventListener("click", () => {
    fetch("/logout/", {
        method: "POST",
        headers: {
            "X-CSRFToken": document.querySelector('input[name = "csrfmiddlewaretoken"]').value, // Asegúrate de incluir el token CSRF
        },
    }).then(() => {
        window.location.href = "/logout"; // Redirige después de cerrar sesión
    });
});