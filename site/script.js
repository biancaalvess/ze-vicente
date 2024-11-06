document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('resumeForm');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        const formData = new FormData(form);

        try {
            const response = await fetch('/submit', {
                method: 'POST',
                body: formData
            });

            if (response.ok) {
                alert('Currículo enviado com sucesso!');
                form.reset();
            } else {
                alert('Erro ao enviar o currículo. Por favor, tente novamente.');
            }
        } catch (error) {
            console.error('Error:', error);
            alert('Erro ao enviar o currículo. Por favor, tente novamente.');
        }
    });
});