/* ==========================================================================
   MAIN JS INTERACTIONS & NAVIGATION
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
    // Mobile Hamburger Navigation
    const hamburger = document.getElementById('hamburger');
    const navMenu = document.getElementById('nav-menu');

    if (hamburger && navMenu) {
        hamburger.addEventListener('click', () => {
            hamburger.classList.toggle('active');
            navMenu.classList.toggle('active');
        });

        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                hamburger.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }

    // Scroll Navbar blur effect
    const header = document.querySelector('.header');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            header.style.background = 'rgba(10, 25, 47, 0.95)';
            header.style.boxShadow = '0 10px 30px rgba(0,0,0,0.5)';
        } else {
            header.style.background = 'rgba(10, 25, 47, 0.85)';
            header.style.boxShadow = 'none';
        }
    });
});

// Fast Consultation Form Handler
function handleFormSubmit(event) {
    event.preventDefault();
    const name = document.getElementById('contact-name').value;
    const email = document.getElementById('contact-email').value;
    const feedback = document.getElementById('form-feedback');

    feedback.className = 'form-feedback success';
    feedback.innerHTML = `✅ Terima kasih <strong>${name}</strong>! Pesan Anda telah kami terima. Tim PT INCAP akan menghubungi <strong>${email}</strong> dalam rentang 1x24 jam kerja.`;
    feedback.classList.remove('hidden');

    document.getElementById('lead-form').reset();
}
