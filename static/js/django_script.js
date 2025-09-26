document.addEventListener("DOMContentLoaded", () => {
    const duration = 5000; // ۵ ثانیه
    const toasts = document.querySelectorAll("#contact-msg-container .contact-toast");

    toasts.forEach((toast) => {
        const progress = toast.querySelector(".contact-toast-progress");
        if (progress) {
            progress.style.animationDuration = duration + "ms";
        }

        // حذف بعد از مدت زمان مشخص
        setTimeout(() => {
            toast.style.animation = "contactToastOut 0.5s forwards";
            setTimeout(() => toast.remove(), 500);
        }, duration);
    });
});
