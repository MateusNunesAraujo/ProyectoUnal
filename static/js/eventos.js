document.addEventListener('DOMContentLoaded', () => {
    // Animación de aparición al hacer scroll (Scroll Reveal)
    const revealItems = document.querySelectorAll('.reveal-item');

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                observer.unobserve(entry.target); // Dejar de observar una vez que es visible
            }
        });
    }, {
        threshold: 0.1, // El 10% del elemento debe ser visible para activar
        rootMargin: '0px 0px -50px 0px' // Reduce el margen inferior para que aparezca un poco antes
    });

    revealItems.forEach(item => {
        observer.observe(item);
    });

    // Funcionalidad de filtrado (ejemplo básico para las categorías)
    const categoryCards = document.querySelectorAll('.category-card');
    const eventCards = document.querySelectorAll('.event-card'); // Todas las tarjetas de evento

    categoryCards.forEach(card => {
        card.addEventListener('click', (e) => {
            e.preventDefault();
            const category = card.dataset.category;

            // Lógica de filtrado (esto es un ejemplo muy básico)
            // En una aplicación real, probablemente harías una solicitud al servidor
            // o manejarías un conjunto de datos más grande.
            eventCards.forEach(eventCard => {
                // Aquí deberías tener una forma de asociar eventos con categorías
                // Por ejemplo, añadiendo un data-category="musica" a cada event-card
                // Para este ejemplo, solo ocultamos/mostramos todas las tarjetas.
                // Esto es solo para demostrar la interactividad del botón.
                console.log(`Filtrando por categoría: ${category}`);
                // En una implementación real, tendrías una lógica como:
                // if (eventCard.dataset.categories.includes(category) || category === 'all') {
                //     eventCard.style.display = 'block';
                // } else {
                //     eventCard.style.display = 'none';
                // }
            });

            // Opcional: Resaltar la categoría activa
            categoryCards.forEach(c => c.classList.remove('border-4', 'border-accent'));
            card.classList.add('border-4', 'border-accent');
        });
    });
});