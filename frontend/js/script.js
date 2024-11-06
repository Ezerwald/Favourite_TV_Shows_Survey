// frontend/js/script.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("survey-form");

    form.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        data.favoriteShows = formData.getAll("favoriteShows[]");
        data.showTypes = formData.getAll("showTypes[]");

        try {
            const response = await fetch("http://localhost:5000/api/submit-survey", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(data)
            });

            const result = await response.json();
            document.getElementById("form-message").textContent = result.message;
        } catch (error) {
            console.error("Error:", error);
            document.getElementById("form-message").textContent = "Submission failed!";
        }
    });
});
