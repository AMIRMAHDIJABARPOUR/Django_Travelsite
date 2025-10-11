document.addEventListener('DOMContentLoaded', function() {
    const toasts = document.querySelectorAll('.xai-message-toast');
    toasts.forEach(toast => {
        setTimeout(() => {
            toast.classList.add('fade-out');
            setTimeout(() => toast.remove(), 300); // Matches fadeOut duration
        }, 5000); // 5 seconds
    });
});