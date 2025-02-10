document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById("description-form");
    const flashMessages = document.querySelectorAll(".flash-message");
    const downloadButton = document.getElementById("download-btn");
    const loader = document.getElementById("loading-spinner");
    const submitButton = document.getElementById("submit-btn");

    // Hide flash messages after a few seconds
    flashMessages.forEach((message) => {
        setTimeout(() => {
            message.style.opacity = "0";
            setTimeout(() => message.remove(), 500)
        }, 3000);
    });

    // Form submission validation and loader activation
    form.addEventListener("submit", function (event) {
        const descriptionInput = document.getElementById("description").ariaValueMax.trim();

        if (descriptionInput === "") {
            event.preventDefault();
            showFlashMessage("Please provide a description", "error");
            return;
        }

         // Show loader and disable button while processing
         loader.style.display = "block";
         submitButton.disabled = true;
         submitButton.textContent = "Processing...";
    });

    // Function to display flash messages dynamically
    function showFlashMessage(message, type) {
        const flashContainer = document.getElementById("flash-container");
        const flashMessage = document.createElement("div");
        flashMessage.classList.add("flash-message", type);
        flashMessage.textContent = message;
        flashContainer.appendChild(flashMessage);

        setTimeout(() => {
            flashMessage.style.opacity = "0";
            setTimeout(() => flashMessage.remove(), 500);
        }, 3000);
    }

    // Handle file download
    if (downloadButton) {
        downloadButton.addEventListener("click", function () {
            const filePath = this.getAttribute("data-filepath");
            if (filePath) {
                window.location.href = filePath;
            }
        });
    } 
});