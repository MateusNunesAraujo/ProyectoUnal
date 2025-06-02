document.addEventListener('DOMContentLoaded', () => {
    const galleryItems = document.querySelectorAll('.gallery-item');
    const modal = document.getElementById('image-modal');
    const modalImage = document.getElementById('modal-image');
    const closeButton = document.querySelector('.close-button');

    galleryItems.forEach(item => {
        item.addEventListener('click', () => {
            const fullSrc = item.querySelector('img').getAttribute('data-full-src');
            modal.style.display = 'flex'; // Mostrar el modal
            modalImage.src = fullSrc;
        });
    });

    closeButton.addEventListener('click', () => {
        modal.style.display = 'none'; // Ocultar el modal
    });

    // Ocultar modal al hacer clic fuera de la imagen
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });
});