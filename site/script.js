        const slideTrack = document.querySelector('.slide-track');
        const images = slideTrack.querySelectorAll('img');
        let currentIndex = 0;

        function nextSlide() {
            currentIndex = (currentIndex + 1) % images.length;
            updateSlidePosition();
        }

        function updateSlidePosition() {
            slideTrack.style.transform = `translateX(-${currentIndex * 100}%)`;
        }

        // Inicia a transição automática a cada 3 segundos
        setInterval(nextSlide, 3000);