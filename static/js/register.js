// Obtener referencias a los botones y formularios
const btnUsuario = document.getElementById('btn-usuario');
const btnEmpresario = document.getElementById('btn-empresario');
const userForm = document.getElementById('user-registration-form');
const businessForm = document.getElementById('business-registration-form');
const btnCancelar = document.querySelectorAll('.cancelar-button')

// Función para mostrar un formulario y ocultar el otro
function showForm(formToShow, formToHide, activeBtn, inactiveBtn) {
    // Remover la clase 'active' para iniciar la transición de ocultamiento
    formToHide.classList.remove('active');
    // Esperar a que la transición de ocultamiento termine antes de mostrar el nuevo formulario
    setTimeout(() => {
        formToShow.classList.add('active');
    }, 500); // Coincide con la duración de la transición de opacidad

    // Añadir clase 'active' al botón activo y removerla del inactivo
    activeBtn.classList.add('active');
    inactiveBtn.classList.remove('active');
}

// Event listener para el botón de Usuario
btnUsuario.addEventListener('click', () => {
    showForm(userForm, businessForm, btnUsuario, btnEmpresario);
});

// Event listener para el botón de Empresario
btnEmpresario.addEventListener('click', () => {
    showForm(businessForm, userForm, btnEmpresario, btnUsuario);
});

btnCancelar.forEach(e => {
    e.addEventListener("click", e => {
            const loginUrl = e.target.getAttribute('data-login-url');
            window.location.href = loginUrl;

    })

})