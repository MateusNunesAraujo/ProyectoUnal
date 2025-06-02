const parrot = document.getElementById('parrot');
const parrotMessage = document.getElementById('parrotMessage');

const mensajes = [
    "¿Sabías que Leticia es la capital del departamento del Amazonas en Colombia?",
    "En Leticia puedes encontrar el Parque Santander, famoso por sus bandadas de loros que llegan al atardecer.",
    "¿Sabías que el río Amazonas, uno de los más largos y caudalosos del mundo, bordea Leticia?",
    "Leticia forma parte de la 'Triple Frontera' con Tabatinga (Brasil) y Santa Rosa de Yavarí (Perú).",
    "La cultura de Leticia es una mezcla vibrante de influencias indígenas, colombianas, peruanas y brasileñas.",
    "¿Sabías que en los alrededores de Leticia puedes avistar el delfín rosado de río?",
    "El pulmón del mundo comienza en Leticia, ¡un lugar lleno de biodiversidad!",
    "La gastronomía de Leticia es exótica, con platos a base de pescado de río y frutas amazónicas.",
    "El clima en Leticia es tropical húmedo, ¡perfecto para una aventura amazónica!",
    "En Leticia se celebra anualmente el Festival Internacional de la Confraternidad Amazónica."
];

parrot.addEventListener('mouseenter', () => {
    let randomIndex = Math.floor(Math.random() * mensajes.length);
    parrotMessage.textContent = mensajes[randomIndex];
    parrotMessage.style.opacity = '1';
});

parrot.addEventListener('mouseleave', () => {
    parrotMessage.style.opacity = '0';
});

document.querySelector(".register button").addEventListener("click", (e) => {
    window.location.href = "/register/"
});