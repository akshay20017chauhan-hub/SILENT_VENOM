// Main JavaScript for SILENT VENOM app
function togglePasswordVisibility(inputId, iconId) {
    const input = document.getElementById(inputId);
    const icon = document.getElementById(iconId);
    if (input.type === "password") {
        input.type = "text";
        icon.classList.remove("bi-eye-slash");
        icon.classList.add("bi-eye");
    } else {
        input.type = "password";
        icon.classList.remove("bi-eye");
        icon.classList.add("bi-eye-slash");
    }
}
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    if (element) {
        element.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    document.querySelectorAll('.cat-pill').forEach(btn => btn.classList.remove('active'));
    event.currentTarget.classList.add('active');
}
function openGame(gameName) {
    if (gameName === 'ludo') {
        window.location.href = '/play/ludo';
    } else {
        alert(gameName.toUpperCase() + ' game coming soon!');
    }
}

