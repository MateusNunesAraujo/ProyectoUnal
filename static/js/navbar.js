const checkbox = document.getElementById('checkbox');
const navCelular = document.getElementById('nav-celular');
const contMenu = document.getElementById('cont-menu')

checkbox.addEventListener('change', function() {
    if (this.checked) {
        navCelular.style.left = "0px";
        contMenu.style.opacity = "1"
         contMenu.style.pointerEvents = "auto";

    } else {
        navCelular.style.left = "-1000px";
        contMenu.style.opacity = "0"
           contMenu.style.pointerEvents = "none";
    }
});